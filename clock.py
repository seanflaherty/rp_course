from datetime import datetime, timezone

class Clock:
    time_now = datetime.now()
    def __init__(self, alarm_time1, alarm_time2):
        self.alarm_time1 = alarm_time1
        self.alarm_time2 = alarm_time2

    # Instance method
    def set_clock_time(self):
        return datetime.now()