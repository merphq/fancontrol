# fancontrol/decorators.py
import logging
from functools import wraps
from fancontrol.control import set_manual_fan_control, set_fan_speed, set_auto_fan_control

logger = logging.getLogger(__name__)

def with_fan_control(speed=100):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info("[FanControl] Enabling manual fan mode...")
                set_manual_fan_control()
                logger.info(f"[FanControl] Setting fan speed to {speed}%...")
                set_fan_speed(speed)
                return func(*args, **kwargs)
            finally:
                try:
                    logger.info("[FanControl] Reverting to automatic fan control...")
                    set_auto_fan_control()
                except Exception as e:
                    logger.warning(f"[FanControl] Failed to reset fan control: {e}")
        return wrapper
    return decorator
