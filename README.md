![logo](img/logo-small.png)

# ProperGoodTuya

A Home Assistant custom integration for **local** handling of Tuya-based devices. Forked from [rospogrigio/localtuya](https://github.com/rospogrigio/localtuya) with active maintenance, bug fixes for latest Home Assistant versions, and expanded device support.

- Status updates via push (not polling) -- fast, even when manually operated
- Tuya IoT Cloud API support for automatic local_key retrieval
- Tuya protocols 3.1 through 3.5 (including AES-GCM encryption for 3.5), with auto-discovery on all of them

## Supported Devices

Switches, Lights, Covers, Fans, Climates, Vacuums, Sensors, Binary Sensors, Numbers, Selects -- plus energy monitoring for compatible devices.

See [SUPPORTED_DEVICES.md](SUPPORTED_DEVICES.md) for the full list including DP mappings and planned device support (water quality monitors, hydroponics controllers, pet feeders, and more).

## Installing alongside other LocalTuya forks

> **Uninstall any other LocalTuya fork first.**

ProperGoodTuya keeps the original `localtuya` domain, so it installs to the same
`custom_components/localtuya/` directory as [rospogrigio/localtuya](https://github.com/rospogrigio/localtuya)
and [xZetsubou/hass-localtuya](https://github.com/xZetsubou/hass-localtuya). Installing two of
them silently overwrites the other - there is no warning, and which one you end up running
depends on install order.

Keeping the domain is deliberate: it means existing LocalTuya config entries and entity IDs
keep working, so you do not have to re-add your devices. The trade-off is that this fork can
only ever be installed as a HACS **custom repository**, never from the default HACS store.

## Quick Start

1. Install via [HACS](https://hacs.xyz/) or manually copy the `custom_components/localtuya` folder to your HA config
2. Add the integration from **Settings > Integrations > + Add Integration > ProperGoodTuya**
3. Configure your Tuya IoT Cloud API credentials (optional but recommended)
4. Add your devices

See [GETTING_STARTED.md](GETTING_STARTED.md) for detailed installation, Cloud API setup, and device configuration instructions.

## Key Notes

- The Cloud API account is **not mandatory** but is strongly recommended for easy local_key retrieval and auto-update after re-pairing devices. Cloud API calls only happen at startup and when a key update is needed.
- Do not declare anything as "tuya" (e.g. `switch.tuya`) -- this launches Home Assistant's built-in cloud-based Tuya integration instead of ProperGoodTuya.
- If blocking device internet access, you must also block DNS requests. See [GETTING_STARTED.md](GETTING_STARTED.md#network-notes) for details.

## Debugging

Enable debug logs by adding this to your `configuration.yaml`:

```yaml
logger:
  default: warning
  logs:
    custom_components.localtuya: debug
    custom_components.localtuya.pytuya: debug
```

Then edit the device showing problems and check "Enable debugging for this device".
