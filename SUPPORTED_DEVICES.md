# Supported Devices

## Currently Supported Platforms

| Platform | Description |
|----------|-------------|
| Switch | On/off switches, smart plugs, power strips |
| Light | RGB, RGBW, colour temperature, dimmable bulbs |
| Cover | Curtains, blinds, garage doors |
| Fan | Ceiling fans, standing fans with speed/direction |
| Climate | Thermostats, heaters, air conditioners |
| Vacuum | Robot vacuums |
| Sensor | Temperature, humidity, energy monitoring, etc. |
| Binary Sensor | Contact, motion, fault detection |
| Number | Countdown timers, thresholds, numeric controls |
| Select | Mode selectors, power-on behaviour |

Energy monitoring (voltage, current, watts, kWh) is supported for compatible switch devices.

## Climate DP Mappings

Tuya climate devices vary significantly. Below are known working mappings:

| DP  | Moes BHT 002 | Qlima WMS S + SC52 | Avatto |
|-----|---|---|---|
| 1 | On/Off `{true, false}` | On/Off `{true, false}` | On/Off `{true, false}` |
| 2 | Target temp (scale: 0.5) | Target temp (scale: 1) | Target temp (scale: 1) |
| 3 | Current temp (scale: 0.5) | Current temp (scale: 1) | Current temp (scale: 1) |
| 4 | Mode `{0, 1}` | Mode `{hot, wind, wet, cold, auto}` | ? |
| 5 | Eco mode | Fan `{strong, high, middle, low, auto}` | ? |
| 19 | -- | Temp unit `{c, f}` | ? |
| 101 | -- | Outdoor temp (scale: 1) | ? |
| 102 | External sensor (scale: 0.5) | Unknown integer | ? |

Reference: [Moes BHT 002](https://community.home-assistant.io/t/moes-bht-002-thermostat-local-control-tuya-based/151953/47)

## Energy Monitoring

Energy values can be configured as individual sensor entities or accessed via switch attributes with template sensors:

```yaml
sensor:
  - platform: template
    sensors:
      tuya_voltage:
        value_template: "{{ states.switch.my_plug.attributes.voltage }}"
        unit_of_measurement: 'V'
      tuya_current:
        value_template: "{{ states.switch.my_plug.attributes.current }}"
        unit_of_measurement: 'mA'
      tuya_power:
        value_template: "{{ states.switch.my_plug.attributes.current_consumption }}"
        unit_of_measurement: 'W'
```

Note: Voltage and consumption values usually need scaling by 0.1. If energy values don't update frequently enough, set the scan interval (30 seconds recommended, minimum 10).

## Smart Kettle DP Mappings

Tuya WiFi smart kettles with temperature control and keep-warm functionality.

| DP | Value (example) | Description | Entity Type |
|----|----------------|-------------|-------------|
| 1 | `False` | Power on/off | Switch |
| 2 | `36` | Current temperature (°C) | Sensor |
| 3 | `97` | Target temperature (°C) | Number |
| 8 | `100` | Target temperature (°F scale) | Number |
| 9 | `212` | Current temperature (°F scale) | Sensor |
| 12 | `c` | Temperature unit (`c` / `f`) | Select |
| 13 | `False` | Keep warm toggle | Switch |
| 14 | `60` | Keep warm duration (minutes) | Number |
| 15 | `standby` | Status (`standby`, `heating`, `keep_warm`) | Sensor |
| 16 | `temp_setting` | Work mode (`temp_setting`, `boil`) | Select |
| 18 | `0` | Fault code | Sensor |
| 19 | `0` | Reserved / unknown | -- |

**Recommended entity setup:**
- **Switch** on DP 1 for power control
- **Sensor** on DP 2 for current temperature (unit: °C, scaling if needed)
- **Number** on DP 3 for target temperature
- **Select** on DP 12 for temperature unit with options `c;f`
- **Switch** on DP 13 for keep warm
- **Number** on DP 14 for keep warm duration (minutes)
- **Sensor** on DP 15 for device status

---

## Ceiling Fan + Light DP Mappings

Tuya-based ceiling fan controllers with integrated light (e.g. Grid Connect, Deta, Arlec). Protocol 3.3.

| DP | Value (example) | Description | Entity Type |
|----|----------------|-------------|-------------|
| 1 | `"1"` | Fan speed (`"1"` low, `"2"` medium, `"3"` high) | Fan |
| 9 | `True` | Light on/off | Light |

**Auto-profile:** When DPs 1 and 9 are detected, the "Ceiling Fan with Light" profile is offered for one-click setup.

**Entity setup:**
- **Fan** on DP 1 with speed control (ordered list: `1,2,3`)
- **Light** on DP 9 for light on/off

---

## Roller Blind / Curtain Motor DP Mappings

Tuya WiFi roller blind and curtain motors (e.g. Zemismart ZM25, generic Tuya tubular motors). Protocol 3.3.

| DP | Value (example) | Description | Entity Type |
|----|----------------|-------------|-------------|
| 1 | `"open"` | Control command (`open`, `close`, `stop`) | Cover |
| 2 | `50` | Set position (0-100) | Cover |
| 3 | `50` | Current position (0-100, read-only) | Cover |
| 5 | `"forward"` | Motor direction (`forward`, `back`) | -- |
| 7 | `"opening"` | Work state (`opening`, `closing`) | -- |

**Auto-profile:** When DPs 1, 2, 3, and 7 are detected, the "Roller Blind / Curtain Motor" profile is offered for one-click setup.

**Entity setup:**
- **Cover** on DP 1 with `open_close_stop` commands, position mode using DP 2 (set) and DP 3 (current)

---

## Additional Device Support (Planned / In Progress)

### Water Quality Monitors (8-in-1 Testers)

WiFi smart online water quality testers (e.g. PH-W218, Yieryi 8-in-1). Protocol 3.4.

**Sensors:**

| DP | Code | Description | Scale | Unit |
|----|------|-------------|-------|------|
| 8 | `temp_current` | Water Temperature | 0.1 | C |
| 106 | `ph_current` | pH Level | 0.01 | pH |
| 111 | `tds_current` | Total Dissolved Solids | 1 | ppm |
| 116 | `ec_current` | Electrical Conductivity | 0.001 | mS/cm |
| 121 | `salinity_current` | Salinity | 1 | ppm |
| 126 | `pro_current` | Specific Gravity | - | S.G |
| 131 | `orp_current` | Oxidation-Reduction Potential | 1 | mV |
| 136 | `cf_current` | Conductivity Factor | 0.01 | CF |
| 141 | `rh_current` | Relative Humidity | 1 | % |

**Warning Thresholds (configurable via Number entities):**

| DP Range | Parameter |
|----------|-----------|
| 102-103 | Temperature high/low |
| 107-108 | pH high/low |
| 112-113 | TDS high/low |
| 117-118 | EC high/low |
| 122-123 | Salinity high/low |
| 127-128 | Specific Gravity high/low |
| 132-133 | ORP high/low |
| 137-138 | CF high/low |
| 142-143 | Humidity high/low |

DP 101 (`sensor_list`) contains a Base64-encoded sensor configuration value.

### Mini Hydroponics / Smart Garden Controllers

Smart growing systems with pump, light, and timer control. Protocol 3.3.

| DP | Code | Description | Entity Type |
|----|------|-------------|-------------|
| 101 | `switch` | Main Power | Switch |
| 102 | `pump` | Water Pump | Switch |
| 103 | `pump_timer` | Pump Schedule (Base64 encoded) | Raw |
| 104 | `led` | Grow Light | Switch |
| 105 | `led_model` | Light Mode (GROW, etc.) | Select |
| 106 | `Countdown_set` | Timer Setting | Number |
| 107 | `Countdown_countdown` | Timer Remaining | Sensor |

### Unsupported Sensor Types

Sensors not covered by the official Tuya integration (reference: [tuya_unsupported_sensors](https://github.com/kattcrazy/tuya_unsupported_sensors)):

| Sensor Type | DP Codes |
|-------------|----------|
| Temperature | `temp`, `temperature`, `va_temperature`, `temp_current` |
| Humidity | `humidity`, `va_humidity`, `humidity_value` |
| Battery | `battery`, `battery_percentage`, `battery_state`, `battery_value` |
| Door/Contact | `contact`, `doorcontact_state`, `door_sensor_state` |
| PIR Motion | `motion`, `pir`, `pir_state` |
| Connectivity | `online` |

### Other Device Categories Under Investigation

| Category | Key Features | Status |
|----------|-------------|--------|
| Pet Feeders | Meal scheduling (Raw DP), portion control, feeding history | Investigating |
| Robot Mowers | HA `lawn_mower` entity, zone control, rain sensing | Investigating |
| Irrigation Controllers | Multi-zone scheduling, weather delay, per-zone timing | Investigating |
| Air Quality Monitors | PM2.5, PM10, CO2, VOC, formaldehyde | Investigating |
| Smart Locks | Lock/unlock, multiple unlock methods, door state, auto-lock | Investigating |
| Energy Monitors / Circuit Breakers | Raw Base64 DP decoding for voltage/current/power | Investigating |
| Pool/Spa Heat Pump Controllers | Temperature control, fault monitoring, multi-zone | Investigating |
