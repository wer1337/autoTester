import pyautogui


def getSS():
    image = pyautogui.screenshot(region=(93, 341, 914, 203))
    image.save('C:\\Users\\JacksonX\\PycharmProjects\\OBRTester\\temp2.png')


def main():
    getSS()

    # print(pyautogui.locateOnScreen('temp2.png'))


if __name__ == '__main__':
    main()