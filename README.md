# Sky Tonight Integration

[![GH-release](https://img.shields.io/github/v/release/wwwescape/sky-tonight-integration.svg?style=flat-square)](https://github.com/wwwescape/sky-tonight-integration/releases)
[![GH-last-commit](https://img.shields.io/github/last-commit/wwwescape/sky-tonight-integration.svg?style=flat-square)](https://github.com/wwwescape/sky-tonight-integration/commits/master)
[![GH-code-size](https://img.shields.io/github/languages/code-size/wwwescape/sky-tonight-integration.svg?color=red&style=flat-square)](https://github.com/wwwescape/sky-tonight-integration)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=flat-square)](https://github.com/hacs/default)
[![Codecov Coverage](https://img.shields.io/codecov/c/github/wwwescape/sky-tonight-integration/main.svg?style=flat-square)](https://codecov.io/gh/wwwescape/sky-tonight-integration/)
[![CodeFactor](https://www.codefactor.io/repository/github/wwwescape/sky-tonight-integration/badge?style=flat-square)](https://www.codefactor.io/repository/github/wwwescape/sky-tonight-integration)

#### Get list of visible planetary bodies in your sky.

A Home Assistant custom intergration that provides information of visible planetary bodies in your sky.

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

| Param                 | Default                   | Description                                                                   |
| --------------------- | ------------------------- | ----------------------------------------------------------------------------- |
| Sky Tonight API URL   | **Required**              | URL of the Sky Tonight API                                                    |
| Latitude              | Home Assistant latitude   | Latitude of the observer                                                      |
| Longitude             | Home Assistant longitude  | Longitude of the observer                                                     |
| Elevation             | Home Assistant elevation  | Elevation of the observer in meters above sea level                           |
| Update Interval       | 15                        | Specifies how often the Sky Tonight API is polled for updates (in minutes)    |

## Sensors Created By This Integration
Sensors will be created for The Sun, Mercury, Venus, The Moon, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto.

For example: `sensor.sky_tonight_sun`.

## TODO
- [ ] Provide ability to update config options
- [ ] Eliminate the need for the Sky Tonight API and instead integrate the Python implementation from [Don Cross' JS Astronomy Engine](http://cosinekitty.com/astronomy.js)