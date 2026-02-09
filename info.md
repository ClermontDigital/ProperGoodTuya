[![](https://img.shields.io/github/release/ClermontDigital/ProperGoodTuya/all.svg?style=for-the-badge)](https://github.com/ClermontDigital/ProperGoodTuya/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)
[![](https://img.shields.io/badge/MAINTAINER-%40ClermontDigital-green?style=for-the-badge)](https://github.com/ClermontDigital)

![logo](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/logo-small.png)

# ProperGoodTuya

A Home Assistant custom integration for **local** handling of Tuya-based devices. Forked from [rospogrigio/localtuya](https://github.com/rospogrigio/localtuya) with active maintenance, bug fixes for latest Home Assistant versions, and expanded device support.

- Status updates via push (not polling) -- fast, even when manually operated
- Tuya IoT Cloud API support for automatic local_key retrieval
- Tuya protocols 3.1 through 3.5 (including AES-GCM encryption for 3.5)
- Device profiles for one-click auto-configuration of known devices

## Supported Platforms

Switches, Lights, Covers, Fans, Climates, Vacuums, Sensors, Binary Sensors, Numbers, Selects -- plus energy monitoring for compatible devices.

## Device Profiles

Known devices are automatically detected during setup and can be configured with a single click:

- Smart Kettle (WiFi temperature control)
- Hydro Garden / Smart Grow System
- Water Quality Monitor (8-in-1)
- Ceiling Fan with Light (Grid Connect / Deta)
- Roller Blind / Curtain Motor

See [SUPPORTED_DEVICES.md](https://github.com/ClermontDigital/ProperGoodTuya/blob/main/SUPPORTED_DEVICES.md) for full DP mappings and planned device support.

## Installation

See [GETTING_STARTED.md](https://github.com/ClermontDigital/ProperGoodTuya/blob/main/GETTING_STARTED.md) for detailed instructions.

**Note:** The Cloud API account is not mandatory but is strongly recommended for easy local_key retrieval and auto-update after re-pairing devices.
