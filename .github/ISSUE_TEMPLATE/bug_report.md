---
name: Bug report
about: Create a report to help us improve ProperGoodTuya
title: ''
labels: 'bug'
assignees: ''

---
<!-- READ THIS FIRST:
  - Check SUPPORTED_DEVICES.md for known DP mappings for your device type
  - Try to update to the latest release, your problem may already be fixed
  - Do not report issues for already existing problems. Check that an issue is not already opened and enrich it.
  - Provide as many details as possible. Paste logs, configuration samples and code into the backticks.
-->
## The problem
<!--
  Describe the issue you are experiencing here to communicate to the
  maintainers. Tell us what you were trying to do and what happened.
-->


## Environment
<!--
  Provide details about your environment.
-->
- ProperGoodTuya version: <!-- plugin version from HACS or manifest.json -->
- Home Assistant Core version: <!-- Configuration => Info -->
- [ ] Does the device work using the Home Assistant Tuya Cloud component?
- [ ] Does the device work using TinyTuya (https://github.com/jasonacox/tinytuya) command line tool?
- [ ] Was the device working with earlier versions of ProperGoodTuya/LocalTuya? Which one?
- [ ] Are you using the Tuya/SmartLife App in parallel?

## Steps to reproduce
<!--
  Clearly define how to reproduce the issue.
-->
1.
2.
3.


## DP dump
<!--
  Paste here the DPs detected for your device. You can find these in the
  device configuration screen or in the debug logs.
-->

## Provide Home Assistant traceback/logs
<!--
  Provide logs if they are relevant. Enable debug logging:

  logger:
    default: warning
    logs:
      custom_components.localtuya: debug
      custom_components.localtuya.pytuya: debug

  Then edit the device and check "Enable debugging for this device".
-->
```
put your log output between these markers
```


## Additional information
<!-- Put here any information that you think it may be relevant -->
