from obrtester.common.clicking import *


def obr_connect():
    move_command([(40, 88), (207, 357)])
    sleep_time(4)
    if pyautogui.locateOnScreen('C:\\Users\\JacksonX\\PycharmProjects\\OBRTester\\obrtester\\common\\error.png') is None:
        print("Imager connected")
    else:
        print("Error connecting to imager, please try again")
        quit(0)


def obr_disconnect():
    move_command([(40, 88), (368, 359)])
