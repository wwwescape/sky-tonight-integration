# Skt Tonight Integration

## A Home Assistant custom intergration that provide information of visible planetary bodies in your sky.

Requires the [Sky Tonight API](https://github.com/wwwescape/sky-tonight-api).

## Install

### Manual installation

- Copy `sky_tonight` folder  to your `<config dir>/custom_components/` directory.
- Restart the Home Assistant.

## Configuration

### Manual Configuration

* Navigate to your Home Assistant instance.
* In the sidebar, click Settings.
* From the Setup menu, select: Devices & Services.
* In the lower right corner, click the Add integration button.
* In the list, search and select `Sky Tonight`.
* Follow the on-screen instructions to complete the setup.

## Options

| Param | Description |
| ----- | ------------- |
| Sky Tonight API URL | The URL of the Sky Tonight API |
| Latitude | Latitude of the observer |
| Longitude | Longitude of the observer  |
| Elevaltion | Elevaltion of the observer |
| Update Interval | Specifies how of the Sky Tonight API is polled for updates |

## Sensors Created By This Integration
Sensors will be created for The Sun, Mercury, Venus, The Moon, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto.

For example: `sensor.sky_tonight_sun`.

## TODOs and Known Issues:
- Provide ability to update config options.
- Eliminate the need for the Sky Tonight API and instead use Python integration of [Don Cross' JS Astronomy Engine](http://cosinekitty.com/astronomy.js).