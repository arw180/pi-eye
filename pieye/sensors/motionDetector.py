"""
Interface for the PIR motion detector
"""
import RPi.GPIO as GPIO

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

        self.gpioIface.set_pin_as_input(self.gpio_pin)

    def is_motion_detected(self):
        """
        Read value from motion detector
        """
        # TODO: read sensor and set motion_detected appropriately
        sensor_reading = self.gpioIface.read_input(self.gpio_pin)
        if sensor_reading and not self.motion_detected:
            # new motion detected - start timer
            pass
        self.motion_detected = sensor_reading
        return self.motion_detected

    def get_last_active_duration(self):
        """
        How long was the PIR sensor active the last time it detected motion?
        """
        return self.last_active_duration
