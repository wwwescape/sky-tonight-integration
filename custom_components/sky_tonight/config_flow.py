import voluptuous as vol
from homeassistant import config_entries
import urllib.parse

from .const import DOMAIN, DEFAULT_UPDATE_INTERVAL

class SkyTonightConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        
        errors = {}

        if user_input is not None:
            if "url" in user_input:
                url = user_input["url"]
                if not self._is_valid_url(url):
                    errors["url"] = "invalid_url"

            if not errors:
                for field in ["latitude", "longitude", "elevation", "update_interval"]:
                    if field in user_input and not user_input[field]:
                        user_input.pop(field)

                return self.async_create_entry(title="SkyTonight", data=user_input)

        schema = vol.Schema(
            {
                vol.Required(
                    "url",
                    description={"suffix": "Enter the URL for the Sky Tonight API"}
                ): str,
                vol.Required(
                    "latitude",
                    default=self._get_default_latitude(),
                    description={"suffix": "Enter the latitude of your location"}
                ): float,
                vol.Required(
                    "longitude",
                    default=self._get_default_longitude(),
                    description={"suffix": "Enter the longitude of your location"}
                ): float,
                vol.Required(
                    "elevation",
                    default=self._get_default_elevation(),
                    description={"suffix": "Enter the elevation of your location"}
                ): int,
                vol.Required(
                    "update_interval",
                    default=DEFAULT_UPDATE_INTERVAL,
                    description={"suffix": "Enter the update interval in seconds"},
                ): int,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=schema, errors=errors, description_placeholders={}
        )

    def _is_valid_url(self, url):
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
        
    def _get_default_latitude(self):
        return self.hass.config.latitude

    def _get_default_longitude(self):
        return self.hass.config.longitude

    def _get_default_elevation(self):
        return self.hass.config.elevation

    async def async_step_reauth(self, config_entry):
        return await self.async_step_user(config_entry.options)