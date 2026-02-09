"""Device profiles for known Tuya device types.

Provides pre-defined DP mappings and entity configurations for known devices,
enabling one-click auto-configuration during device setup.
"""

from homeassistant.const import (
    CONF_FRIENDLY_NAME,
    CONF_ID,
    CONF_PLATFORM,
    CONF_UNIT_OF_MEASUREMENT,
)

from .const import (
    CONF_COMMANDS_SET,
    CONF_CURRENT_POSITION_DP,
    CONF_FAN_DPS_TYPE,
    CONF_FAN_ORDERED_LIST,
    CONF_FAN_SPEED_CONTROL,
    CONF_FAN_SPEED_MAX,
    CONF_FAN_SPEED_MIN,
    CONF_MAX_VALUE,
    CONF_MIN_VALUE,
    CONF_OPTIONS,
    CONF_OPTIONS_FRIENDLY,
    CONF_PASSIVE_ENTITY,
    CONF_POSITIONING_MODE,
    CONF_POSITION_INVERTED,
    CONF_RESTORE_ON_RECONNECT,
    CONF_SCALING,
    CONF_SET_POSITION_DP,
    CONF_STEPSIZE_VALUE,
)

# Sentinel value indicating user chose manual configuration
PROFILE_MANUAL = "_manual_"

# Each profile defines:
#   "name":      str - Human-readable display name
#   "match_dps": set[int] - DP IDs that must ALL be present (subset match)
#   "entities":  list[dict] - Complete entity configs, same shape as stored in
#                config_entry.data[CONF_DEVICES][dev_id][CONF_ENTITIES]

DEVICE_PROFILES = {
    "smart_kettle": {
        "name": "Smart Kettle (WiFi Temperature Control)",
        "match_dps": {1, 2, 3, 12, 13, 14, 15, 16},
        "entities": [
            {
                CONF_ID: 1,
                CONF_PLATFORM: "switch",
                CONF_FRIENDLY_NAME: "Power",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 2,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Current Temperature",
                CONF_UNIT_OF_MEASUREMENT: "\u00b0C",
            },
            {
                CONF_ID: 3,
                CONF_PLATFORM: "number",
                CONF_FRIENDLY_NAME: "Target Temperature",
                CONF_MIN_VALUE: 40.0,
                CONF_MAX_VALUE: 100.0,
                CONF_STEPSIZE_VALUE: 1.0,
                CONF_RESTORE_ON_RECONNECT: True,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 12,
                CONF_PLATFORM: "select",
                CONF_FRIENDLY_NAME: "Temperature Unit",
                CONF_OPTIONS: "c;f",
                CONF_OPTIONS_FRIENDLY: "Celsius;Fahrenheit",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 13,
                CONF_PLATFORM: "switch",
                CONF_FRIENDLY_NAME: "Keep Warm",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 14,
                CONF_PLATFORM: "number",
                CONF_FRIENDLY_NAME: "Keep Warm Duration",
                CONF_MIN_VALUE: 1.0,
                CONF_MAX_VALUE: 180.0,
                CONF_STEPSIZE_VALUE: 1.0,
                CONF_RESTORE_ON_RECONNECT: True,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 15,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Status",
            },
            {
                CONF_ID: 16,
                CONF_PLATFORM: "select",
                CONF_FRIENDLY_NAME: "Work Mode",
                CONF_OPTIONS: "temp_setting;boil",
                CONF_OPTIONS_FRIENDLY: "Temperature Setting;Boil",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
        ],
    },
    "hydro_garden": {
        "name": "Hydro Garden / Smart Grow System",
        "match_dps": {101, 102, 104, 105, 106, 107},
        "entities": [
            {
                CONF_ID: 101,
                CONF_PLATFORM: "switch",
                CONF_FRIENDLY_NAME: "Main Power",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 102,
                CONF_PLATFORM: "switch",
                CONF_FRIENDLY_NAME: "Water Pump",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 104,
                CONF_PLATFORM: "switch",
                CONF_FRIENDLY_NAME: "Grow Light",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 105,
                CONF_PLATFORM: "select",
                CONF_FRIENDLY_NAME: "Light Mode",
                CONF_OPTIONS: "grow;enjoy;standard",
                CONF_OPTIONS_FRIENDLY: "Grow;Enjoy;Standard",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 106,
                CONF_PLATFORM: "number",
                CONF_FRIENDLY_NAME: "Countdown Timer",
                CONF_MIN_VALUE: 0.0,
                CONF_MAX_VALUE: 1440.0,
                CONF_STEPSIZE_VALUE: 1.0,
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 107,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Countdown Remaining",
                CONF_UNIT_OF_MEASUREMENT: "min",
            },
        ],
    },
    "water_quality_monitor": {
        "name": "Water Quality Monitor (8-in-1)",
        "match_dps": {8, 106, 111, 116, 121, 131},
        "entities": [
            {
                CONF_ID: 8,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Water Temperature",
                CONF_UNIT_OF_MEASUREMENT: "\u00b0C",
                CONF_SCALING: 0.1,
            },
            {
                CONF_ID: 106,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "pH Level",
                CONF_UNIT_OF_MEASUREMENT: "pH",
                CONF_SCALING: 0.01,
            },
            {
                CONF_ID: 111,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "TDS",
                CONF_UNIT_OF_MEASUREMENT: "ppm",
            },
            {
                CONF_ID: 116,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Electrical Conductivity",
                CONF_UNIT_OF_MEASUREMENT: "mS/cm",
                CONF_SCALING: 0.001,
            },
            {
                CONF_ID: 121,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Salinity",
                CONF_UNIT_OF_MEASUREMENT: "ppm",
            },
            {
                CONF_ID: 126,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Specific Gravity",
                CONF_UNIT_OF_MEASUREMENT: "S.G",
            },
            {
                CONF_ID: 131,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "ORP",
                CONF_UNIT_OF_MEASUREMENT: "mV",
            },
            {
                CONF_ID: 136,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "CF",
                CONF_UNIT_OF_MEASUREMENT: "CF",
                CONF_SCALING: 0.01,
            },
            {
                CONF_ID: 141,
                CONF_PLATFORM: "sensor",
                CONF_FRIENDLY_NAME: "Humidity",
                CONF_UNIT_OF_MEASUREMENT: "%",
            },
        ],
    },
    "ceiling_fan_light": {
        "name": "Ceiling Fan with Light (Grid Connect / Deta)",
        "match_dps": {1, 9},
        "entities": [
            {
                CONF_ID: 1,
                CONF_PLATFORM: "fan",
                CONF_FRIENDLY_NAME: "Fan",
                CONF_FAN_SPEED_CONTROL: 1,
                CONF_FAN_ORDERED_LIST: "1,2,3",
                CONF_FAN_DPS_TYPE: "str",
                CONF_FAN_SPEED_MIN: 1,
                CONF_FAN_SPEED_MAX: 3,
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
            {
                CONF_ID: 9,
                CONF_PLATFORM: "light",
                CONF_FRIENDLY_NAME: "Light",
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
        ],
    },
    "roller_blind_motor": {
        "name": "Roller Blind / Curtain Motor",
        "match_dps": {1, 2, 3, 7},
        "entities": [
            {
                CONF_ID: 1,
                CONF_PLATFORM: "cover",
                CONF_FRIENDLY_NAME: "Blind",
                CONF_COMMANDS_SET: "open_close_stop",
                CONF_POSITIONING_MODE: "position",
                CONF_CURRENT_POSITION_DP: 3,
                CONF_SET_POSITION_DP: 2,
                CONF_POSITION_INVERTED: False,
                CONF_RESTORE_ON_RECONNECT: False,
                CONF_PASSIVE_ENTITY: False,
            },
        ],
    },
}


def match_profiles(detected_dp_ids):
    """Return list of (profile_key, profile) tuples that match detected DPs.

    A profile matches when ALL of its match_dps are present in the
    detected DP ID set (subset matching). Multiple profiles may match
    if a device has a superset of DPs. Profiles are returned sorted
    by match quality (most DPs matched first).
    """
    matches = []
    for key, profile in DEVICE_PROFILES.items():
        if profile["match_dps"].issubset(detected_dp_ids):
            matches.append((key, profile))
    matches.sort(key=lambda x: len(x[1]["match_dps"]), reverse=True)
    return matches
