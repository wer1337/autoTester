from obrtester.common.clicking import *


def prev_setup():
    # Moves to tab
    # Moves to reset
    move_command([(497, 86), (631, 133)])
    # Edits Fields
    d_click(193, 165)
    pyautogui.typewrite(['backspace', '1', 'tab', 'backspace', '1', 'tab', 'backspace', '1'], .1)
    move_command([(268, 232), (149, 126)])


def get_preview(file_name, image_folder, type):
    move_command([(497, 86)])
    sleep_time(10)
    image = pyautogui.screenshot(region=(93, 341, 914, 203))
    image_name = f'{image_folder}\\{type}_{file_name[:-4]}.png'
    image.save(f'{image_name}')
    image.save('C:\\Users\\JacksonX\\PycharmProjects\\OBRTester\\temp.png')
    # pyautogui.screenshot(f'C:\\Users\\JacksonX\\PycharmProjects\\OBRTester\\images\\{file_name[:-4]}png', region=(93, 341, 914, 203))

