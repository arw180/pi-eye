"""
main.py

Main event loop for pi-eye

Event loop might look something like this:

- check to see if system is armed. If not, exit loop
- get light level from photosensor. If low light, turn on bright LED(s)
- if motion sensor is activated, take picture and send to sever (websockets?)
- maybe only alert on first pass through loop where detection changed from 0 to 1?
-

heartbeat loop (every ~15 seconds):

- communicate with server
- server should be actively looking for the communication. if not found,
    an alert is sent to the user

how to handle manual override (for instance, user wants to manually take
pictures or video)?

This event loop should be something like a Tornado event loop, and have
handlers for messages like:

arm
disarm
modify_detection_settings (sensitivity, resolution, light, etc)
modify_notification_settings(notification channel(s))
modify_storage_settings (storage_provider(s))
light_on
light_off
make_noise(duration)
get_status
take_picture (num_pics, duration)
take_video (duration)
heartbeat


modes/states:

armed-inactive: unit is armed but detects no motion
armed-active: unit is armed and actively detecting motion and/or sound
manual-override-taking-pics: taking picture(s) (and maybe sound) in manual override
manual-override-taking-video: taking video (and maybe sound) in manual override
disarmed: unit is not responding to or detecting motion or sound
disconnected: unit has lost connection to external server(s) (wifi, Internet, etc)
connecting: unit is attempting to establish connection with external server(s)

A note about scheduling armed/disarmed times:
this will be done through the front-end web app, which will then send the
arm/disarm commands as necessary. Might want to reconsider this eventually,
as this could prevent a connection failure from arming the unit at the right
time.

TODO:
Some sort of state machine class to handle state transitions


"""

import time

import picamera


def main_loop():
    counter = 0
    while True:
        # do something
        print 'doing stuff...'

        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            # Camera warm-up time
            time.sleep(2)
            camera.capture('img-%s.jpg' % counter)
            time.sleep(10)


if __name__ == "__main__": main_loop()