import pyautogui
from obrtester.common.wait import sleep_time

dur = .5


def move_command(arr):
    for x ,y in arr:
        pyautogui.moveTo(x, y, dur)
        pyautogui.click()


def d_click(x, y):
    pyautogui.moveTo(x, y, dur)
    pyautogui.doubleClick()


def click_it(x, y):
    pyautogui.click(x, y)
    sleep_time(1)
