import time
import sys


def sleep_time(seconds):
    for i in range(seconds, 0, -1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
