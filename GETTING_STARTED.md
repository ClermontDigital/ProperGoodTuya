# Installation & Getting Started

## Installation

### Via HACS (Custom Repository)

Since ProperGoodTuya is not yet in the default HACS store, you need to add it as a custom repository:

1. Open Home Assistant and go to **HACS** in the sidebar
2. Click the **three dots menu** (top right) and select **Custom repositories**
3. In the **Repository** field, enter: `https://github.com/ClermontDigital/ProperGoodTuya`
4. In the **Category** dropdown, select **Integration**
5. Click **Add**
6. The integration will now appear in HACS -- click on it and press **Download**
7. **Restart Home Assistant**

After restart, the integration will be available to configure.

### Manual Installation

1. Download or clone this repository
2. Copy the `custom_components/localtuya` folder into your Home Assistant `config/custom_components/` directory
   - **Hass.io / Home Assistant OS:** Use the Samba or SSH add-on to access the config folder
   - **Home Assistant Supervised:** The folder is typically at `/usr/share/hassio/homeassistant/custom_components/`
   - **Home Assistant Core:** Copy to `~/.homeassistant/custom_components/`
3. Create the `custom_components` directory if it doesn't already exist
4. **Restart Home Assistant**

---

## Setting Up the Tuya IoT Cloud API

The Cloud API is optional but strongly recommended. It automatically retrieves and updates your device local_keys, so you don't have to manually extract them.

Cloud API calls are only made at startup and when a local_key update is needed -- devices are still controlled entirely locally.

### Step 1: Create a Tuya IoT Platform Account

1. Go to the [Tuya IoT Platform](https://iot.tuya.com/) and create an account
2. Follow the official Home Assistant Tuya setup guide: https://www.home-assistant.io/integrations/tuya/
3. Create a **Cloud Project** (must be created after May 25, 2021 for Tuya 2.0 compatibility)

![project_date](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/6-project_date.png)

### Step 2: Get Your Credentials

You need three values from the Tuya IoT Platform:

- **Client ID** and **Client Secret**: Found at `Cloud > Development > Overview`
- **User ID**: Found in the "Link Tuya App Account" subtab within your Cloud project

![user_id](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/8-user_id.png)

### Step 3: Link Your Tuya App Account

1. In the Tuya IoT Platform, go to your Cloud project
2. Click the **Link Tuya App Account** tab
3. Open the Tuya or Smart Life app on your phone
4. Scan the QR code to link your account

This allows the Cloud API to see all devices registered in your Tuya app.

---

## Adding the Integration

1. In Home Assistant, go to **Settings > Devices & Services > + Add Integration**
2. Search for **ProperGoodTuya** (or **LocalTuya**) and select it
3. Enter your Cloud API credentials (or tick "Do not configure a Cloud API account" to skip)

![cloud_setup](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/9-cloud_setup.png)

4. Press **Submit** -- the integration is now added

> Starting from v4.0.0, YAML configuration is no longer supported. Use the config flow only.

---

## Configuring Devices

After the integration is set up, press the **Configure** button on the integration card:

![integration_configure](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/10-integration_configure.png)

### Configuration Menu

![config_menu](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/11-config_menu.png)

From here you can:
- **Add or Edit a device** -- add new devices or modify existing ones
- **Reconfigure Cloud API account** -- update your Tuya Cloud credentials

### Adding a Device

1. Select "Add or Edit a device"
2. Choose a discovered device from the dropdown, or select "..." to manually enter parameters

![discovery](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/1-discovery.png)

> **Important:** Close the Tuya app on your phone before proceeding -- it can interfere with local connections.

3. Enter the device's **Friendly Name** and **Local Key** (auto-filled if Cloud API is configured)

**Optional settings:**
- **Scan Interval** -- only needed if energy/power values don't update frequently enough (30s recommended, 10s minimum)
- **Manual DPS To Add** -- only if the device doesn't advertise DPS correctly. Try initialising with the Tuya app first. Added DPS will show -1 during setup.
- **DPIDs to send in RESET command** -- for devices stuck in zombie state after power cycle (typically "18,19,20"). Only use sensor DPIDs here.

4. Press **Submit** to test the connection

![device](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/2-device.png)

### Device Profiles (Auto-Configuration)

If the detected DPs match a known device profile (e.g. smart kettle, ceiling fan + light, roller blind motor), you will be offered a **one-click auto-configuration** option. Select the matching profile to automatically create all entities, or choose "Configure manually" to set them up individually.

### Adding Entities Manually

If no profile matches, or you chose manual configuration, add entities one at a time:

1. Select the entity type (switch, light, sensor, etc.)

![entity_type](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/3-entity_type.png)

2. Select the DP (datapoint) for this entity -- the dropdown shows all available DPs with their current values

![entity](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/4-entity.png)

3. Configure entity-specific options
4. Repeat for each entity you want to add
5. When done, leave "Do not add more entities" checked and submit

![success](https://github.com/rospogrigio/localtuya-homeassistant/blob/master/img/5-success.png)

---

## Getting Device Local Keys (Without Cloud API)

If you choose not to use the Cloud API, you can obtain local_keys using:

- **TinyTuya**: https://pypi.org/project/tinytuya/
- **TuyAPI**: https://github.com/codetheweb/tuyapi/blob/master/docs/SETUP.md

---

## Migration from LocalTuya v.3.x.x

If upgrading from v3.x.x, the config entry will automatically migrate. You'll see a single LocalTuya integration instead of separate ones per device. Once migrated, add your Cloud API credentials to enable automatic local_key management.

If you previously used YAML configuration, you can remove those entries -- they are no longer used (keep the `logger` section for debugging).

---

## Network Notes

If you plan to block your Tuya devices' internet access:

1. First connect devices with an active internet connection
2. Extract each device's local_key
3. Block both **outbound internet** and **DNS requests** (to your local DNS server, e.g. 192.168.1.1)

If you only block outbound internet without blocking DNS, devices will enter a zombie state and refuse local connections.
