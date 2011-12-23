import sys
import datetime

# patch timedelta in python 2.6 to behave like python 2.7
if sys.version_info < (2, 7):
    class timedelta_patched(datetime.timedelta):
        def total_seconds(self):
            return (float(self.microseconds) + (self.seconds + self.days * 24 * 3600) * 10**6) / 10**6
    datetime.timedelta = timedelta_patched
