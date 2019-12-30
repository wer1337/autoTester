from obrtester.basic.openOBR import *
from obrtester.common.connection import *
from obrtester.tabs.printtest import *


def tester(version):
    pyautogui.PAUSE = .5
    obr_disconnect()
    obr_status(0)
    obr_status(1)
    obr_connect()
    prev_setup()
    print_settings()
    barcode_test(version)
    print("Tests have ran.")
