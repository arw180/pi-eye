"""
The Guardian does his job
"""
from datetime import timedelta
from datetime import datetime

import constants
import enum
import sensors.motionDetector as motionDetector
import sensors.picam as picam
import storage.evidenceCollector as evidenceCollector

States = enum.Enum(['ALL_CLEAR', 'READY', 'TAKING_PICTURES', 'SENDING_ALERTS',
                    'UPLOADING_EVIDENCE'])


class Guardian:
    """
    Guardian class
    """
    def __init__(self):
        self.motion_detector = motionDetector.MotionDetector()
        self.camera = picam.PiCam()
        self.evidence_collector = evidenceCollector.EvidenceCollector()
        self.state = States.ALL_CLEAR
        # just initialize to current time
        self.last_alert_time = datetime.now()
        self.see_motion = False

    def patrol(self):
        """
        Patrol the area
        """
        self.see_motion = self.motion_detector.is_motion_detected()
        # If we see motion and we aren't currently taking pictures, do so now
        if self.see_motion and not self.state == States.TAKING_PICTURES:
            self.state = States.TAKING_PICTURES
            print 'Guardian: %s' % self.state
            self.camera.burst_mode(constants.CAMERA_BURST_COUNT)
            self.state = States.READY    # only transition after previous state completes

        # If we see motion and enough time has elapsed since the last alert,
        #   send a new alert now (provided we aren't already doing so)
        if self.see_motion and not self.state == States.SENDING_ALERTS:
            if self._ok_to_alert():
                self.state = States.SENDING_ALERTS
                print 'Guardian: %s' % self.state
                # TODO: send alert
                self.last_alert_time = datetime.now()
                self.state = States.READY    # only transition after previous state completes

        # Check to see if there is evidence that has not been uploaded yet. If
        #   so, upload it now (provided we aren't doing so already)
        if self.evidence_collector.found_unsaved_evidence() and not self.state == States.UPLOADING_EVIDENCE:
            self.state = States.UPLOADING_EVIDENCE
            print 'Guardian: %s' % self.state
            # TODO: upload images/video/audio to cloud
            self.state = States.READY    # only transition after previous state completes

        # If no motion is detected, the coast is clear
        if not self.see_motion:
            self.state = States.ALL_CLEAR
            print 'Guardian: %s' % self.state

    def _ok_to_alert(self):
        """
        Is it time to send a new alert?
        """
        if datetime.now() - self.last_alert_time > timedelta(
                seconds=constants.MINIMUM_ALERT_PERIOD):
            return True
        else:
            return False