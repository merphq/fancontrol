fancontrol
----------

IPMI-based fan control module for Dell R730 and other BMC/IPMI-compatible servers.
Built for high-performance workloads where you need full manual control over server fan speeds from within Python code.

Features
--------

- Set fans to manual mode via raw IPMI
- Control fan speed in percent
- Return to iDRAC/BMC automatic mode
- Drop-in Python decorator for wrapping workloads
- Compatible with Loguru or built-in logging

Installation
------------

Using Poetry (recommended):
    poetry add git+https://github.com/merphq/fancontrol.git

Using pip:
    pip install git+https://github.com/merphq/fancontrol.git

Usage
-----

Example with the decorator:

    from fancontrol import with_fan_control

    @with_fan_control(speed=100)
    def run_heavy_task():
        # your workload here
        pass

This will:
- Set fans to manual mode
- Set speed to 100%
- Automatically revert to auto fan control after the function exits (even if it crashes)

Manual fan control example:

    from fancontrol import set_manual_fan_control, set_fan_speed, set_auto_fan_control

    set_manual_fan_control()
    set_fan_speed(80)  # Set to 80%
    ...
    set_auto_fan_control()

Requirements
------------

- ipmitool installed and in your system PATH
- IPMI-compatible server with fan control support (tested on Dell R730)
- Optionally uses loguru for enhanced logging (falls back to stdlib logging)

Safety
------

- Fan control is wrapped in try/finally to ensure reset on exit
- Decorator handles exceptions gracefully
- Keeps your server from staying in manual mode if your program crashes

Contributing
------------

Pull requests welcome. Especially for:
- Supporting more server models
- Adding a CLI wrapper
- Building temperature-based control logic

License
-------

MIT License
(c) merphq
