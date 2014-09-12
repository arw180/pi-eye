"""
Interface for the Raspberry Pi camera
"""
# TODO: fix this garbage
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

import time
from datetime import datetime

import picamera


class PiCam:

    def __init__(self):
        """
        """
        self.img_count = 0
        self.busy = False

    def take_lowdef_picture(self):
        if self.busy:
            return
        else:
            self.busy = True
        t1 = datetime.now()

        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            camera.start_preview()
            # Camera warm-up time
            time.sleep(1)
            camera.capture('img-%d.jpg' % self.img_count)
            t2 = datetime.now()
            print 'Picture taken and saved in %d ms' % int((t2-t1).total_seconds()*1000)
            self.img_count += 1
        self.busy = False
        return

    def burst_mode(self, count):
        if self.busy:
            return
        else:
            self.busy = True
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            for filename in camera.capture_continuous(PiCam._get_img_name()):
                print('Captured %s' % filename)
                self.img_count += 1
                count -= 1
                if count == 0:
                    self.busy = False
                    break
                time.sleep(1)  # wait 1 second

    # def take_highdef_picture():
    #     return
    #
    # def record_video(duration):
    #     return

    def is_busy(self):
        return self.busy

    @staticmethod
    def _get_img_name():
        return 'img%s.jpg' % datetime.now().strftime('%H-%M-%S')

