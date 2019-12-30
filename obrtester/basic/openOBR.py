import subprocess
import os
from obrtester.common.wait import sleep_time


def open_obr():
    p = subprocess.Popen(r'C:\Users\JacksonX\Documents\OBR\OnBoardRIPTester.exe')
    sleep_time(1)
    if p.poll() is None:
        print("OBR is opened successfully")
    else:
        print("Cannot Open OBR. Quitting application")
        quit(0)


def quit_obr():
    os.system("TASKKILL /F /IM OnBoardRIPTester.exe")


def obr_status(code):
    if code == 0:
        quit_obr()
    else:
        open_obr()