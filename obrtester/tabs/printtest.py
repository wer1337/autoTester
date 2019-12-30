import os
import docx
import datetime
import pygetwindow as gw

from obrtester.common.wordocx import *
from obrtester.tabs.imgpreview import *


def find_files(directory, file_type):
    file_list = []
    for file in os.listdir(directory):
        if file.endswith(file_type):
            file_list.append(file)
    return file_list


def print_settings():
    move_command([(92, 87), (45, 208), (49, 493), (248, 521), (618, 455)])


def barcode_test(version):
    base_path = 'C:\\Users\\JacksonX\\Desktop\\Testing'

    job_dir = f'{base_path}\\Antares_Datamatrix_Test_Jobs'
    job_list = find_files(job_dir, ".xml")
    data_dir = f'{base_path}\\Antatres_Datamatrix_Test_Databases'
    data_list = find_files(data_dir, ".txt")

    move_command([(535, 492)])

    open_window = gw.getWindowsWithTitle("Open")[0]
    sleep_time(1)
    open_window.resizeTo(800, 800)
    open_window.moveTo(100, 100)
    pyautogui.press('esc')
    sleep_time(1)

    month = datetime.datetime.now().strftime("%b")
    day = datetime.datetime.now().strftime("%d")

    if not os.path.exists(f'{base_path}'):
        os.makedirs(f'{base_path}\\{month}_{day}')

    parent_dir = f'{base_path}\\{month}_{day}'

    for i in job_list:
        move_command([(535, 492), (600, 148)])
        pyautogui.typewrite(f'{job_dir}\n', .005)
        move_command([(633, 839)])
        print(i)
        pyautogui.typewrite(f'{i}\n', .1)

        document = docx.Document()

        type = i[:1]

        if not os.path.exists(f'{base_path}\\{month}_{day}\\{i[:-4]}_{version}'):
            os.makedirs(f'{base_path}\\{month}_{day}\\{i[:-4]}_{version}')

        image_folder = f'{base_path}\\{month}_{day}\\{i[:-4]}_{version}'

        curr_dir = job_dir
        for j in data_list:
            if curr_dir != data_dir:
                move_command([(114, 232), (600, 148)])
                pyautogui.typewrite(f'{data_dir}\n', .005)
                curr_dir = data_dir
            else:
                move_command([(114, 232)])
            move_command([(633, 839)])
            print(j)
            pyautogui.typewrite(f'{j}\n', .1)
            pyautogui.moveTo(855, 747, .05)
            pyautogui.rightClick()
            move_command([(913, 762), (76, 556)])
            # Go to Image Preview tab
            get_preview(j, image_folder, type)
            move_command([(92, 87), (146, 557)])










