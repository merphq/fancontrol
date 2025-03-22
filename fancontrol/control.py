# fancontrol/control.py
import subprocess
import logging
logger = logging.getLogger(__name__)


def set_manual_fan_control():
    subprocess.run(["ipmitool", "raw", "0x30", "0x30", "0x01", "0x00"], check=True)


def set_fan_speed(percent: int):
    import subprocess
    if not 0 <= percent <= 100:
        raise ValueError("Fan speed must be between 0 and 100")

    raw_value = int(255 * (percent / 100))  # Range: 0–255
    subprocess.run([
        "ipmitool", "raw", "0x30", "0x30", "0x02", "0xff", str(raw_value)
    ], check=True)



def set_auto_fan_control():
    subprocess.run(["ipmitool", "raw", "0x30", "0x30", "0x01", "0x01"], check=True)
