"""
Interface for the Raspberry Pi camera
"""
import time

import picamera

def take_lowdef_picture():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('img.jpg')
        time.sleep(10)
    return

def take_highdef_picture():
    return

def record_video(duration):
    return

