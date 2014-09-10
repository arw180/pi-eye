"""
Interface for the PIR motion detector
"""

"""
Is motion actively being detected?
"""
def motion_detected():
    return False

"""
How long was the PIR sensor active the last time it detected motion?
"""
def get_last_active_duration():
    return 0