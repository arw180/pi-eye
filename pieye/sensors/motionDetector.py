"""
Interface for the PIR motion detector
"""
# TODO: fix this garbage
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from pieye import constants
from gpioIface import GpioInterface


class MotionDetector:

    def __init__(self):
        """
        initialization

        self.motion_detected: is motion currently being detected
        self.last_active_duration: time in ms that the last motion
            detection was active
        """
        self.motion_detected = False
        self.last_active_duration = 0

        self.gpioIface = GpioInterface()
        self.gpio_pin = constants.MOTION_SENSOR_GPIO
        self.indicator_gpio_pin = constants.MOTION_SENSOR_INDICATOR_GPIO

        self.gpioIface.set_pin_as_input(self.gpio_pin)
        self.gpioIface.set_pin_as_output(self.indicator_gpio_pin)

    def is_motion_detected(self):
        """
        Read value from motion detector
        """
        sensor_reading = self.gpioIface.read_input(self.gpio_pin)
        if sensor_reading and not self.motion_detected:
            self.gpioIface.set_output(self.indicator_gpio_pin, 1)
            # new motion detected - start timer
        self.motion_detected = sensor_reading
        if not self.motion_detected:
            self.gpioIface.set_output(self.indicator_gpio_pin, 0)
        return self.motion_detected

    def get_last_active_duration(self):
        """
        How long was the PIR sensor active the last time it detected motion?
        """
        return self.last_active_duration
