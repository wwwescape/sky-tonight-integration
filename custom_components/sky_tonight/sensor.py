import logging
from datetime import timedelta

import aiohttp
import asyncio
import async_timeout

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed
)
from homeassistant.helpers.aiohttp_client import async_get_clientsession

_LOGGER = logging.getLogger(__name__)

from .const import DOMAIN

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    pass

async def async_setup_entry(hass, config_entry, async_add_entities):
    url = config_entry.data["url"]
    latitude = config_entry.data["latitude"]
    longitude = config_entry.data["longitude"]
    elevation = config_entry.data["elevation"]
    update_interval = config_entry.data["update_interval"]
    api_url = f"{url}?latitude={latitude}&longitude={longitude}&elevation={elevation}&aboveHorizon=false&showCoords=true"
    coordinator = SkyTonightDataUpdateCoordinator(hass, api_url, update_interval, async_add_entities, _LOGGER)
    await coordinator.async_refresh()
    async_add_entities(coordinator.entities, True)

class SkyTonightSensor(CoordinatorEntity):
    def __init__(self, coordinator, name, state, attributes):
        super().__init__(coordinator)
        self._name = name
        self._state = state
        self._attributes = attributes

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return f"{DOMAIN}_{self._name}"

    @property
    def state(self):
       return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

class SkyTonightDataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api_url, update_interval, async_add_entities, logger):
        self.hass = hass
        self.api_url = api_url
        self.entities = []
        self.update_interval = timedelta(minutes=update_interval)
        super().__init__(
            hass,
            logger,
            name=DOMAIN,
            update_method=self._async_update,
            update_interval=self.update_interval,
        )
        self.async_add_entities = async_add_entities
        self._session = async_get_clientsession(self.hass)

    async def _async_update(self):
        try:
            with async_timeout.timeout(10):
                response = await self._session.get(self.api_url)
                json_response = await response.json()
                self._process_data(json_response)
        except (asyncio.TimeoutError, aiohttp.ClientError) as error:
            raise UpdateFailed(f"Error fetching data: {error}") from error

    def _process_data(self, json_response):
        new_entities = []
        raw_data = json_response.get("data", [])
        for obj in raw_data:
            obj_name = obj.get("name")
            name = f"Sky Tonight {obj_name}"
            obj_above_horizon = obj.get("aboveHorizon")
            state = "above_horizon" if obj_above_horizon else "below_horizon"
            attributes = {
                key: value for key, value in obj.items() if key not in ["name", "aboveHorizon"]
            }
            
            entity = next(
                (
                    entity
                    for entity in self.entities
                    if entity.name == name
                ),
                None,
            )
            if entity:                
                if (
                    entity.state != state
                    or entity.extra_state_attributes != attributes
                ):
                    entity._state = state
                    entity._attributes = attributes
            else:
                new_entities.append(
                    SkyTonightSensor(
                        self, name, state, attributes
                    )
                )

        self.entities.extend(new_entities)