"""
Interface with the GPIO
"""

import RPi.GPIO as GPIO

from pieye.singleton import Singleton


class GpioInterface(object):
    __metaclass__ = Singleton

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def set_pin_as_input(self, pin):
        GPIO.setup(pin, GPIO.IN)

    def set_pin_as_output(self, pin):
        GPIO.setup(pin, GPIO.OUT)

    def read_input(self, pin):
        return GPIO.input(pin)

    def set_output(self, pin, value):
        GPIO.output(pin, value)