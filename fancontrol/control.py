# fancontrol/control.py
import subprocess


def set_manual_fan_control():
    subprocess.run(["ipmitool", "raw", "0x30", "0x30", "0x01", "0x00"], check=True)


def set_fan_speed(percent: int):
    hex_speed = hex(int(255 * (percent / 100)))
    subprocess.run(["ipmitool", "raw", "0x30", "0x30", "0x02", "0xff", hex_speed], check=True)


def set_auto_fan_control():
    subprocess.run(["ipmitool", "raw", "0x30", "0x30", "0x01", "0x01"], check=True)
