from skimage.metrics import structural_similarity
import imutils
import cv2
import docx
import os
import datetime

from obrtester.tabs.printtest import find_files
from obrtester.common.wordocx import *


def compare2(imageA, imageB, img_dir, loc1, loc2, type):
    imgA = cv2.imread(f'{loc1}\\{imageA}')
    imgB = cv2.imread(f'{loc2}\\{imageB}')

    grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

    score, diff = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(imgA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imgB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite(f'{img_dir}\\{imageA[:-4]}_V1_{type}.png', imgA)
    cv2.imwrite(f'{img_dir}\\{imageB[:-4]}_V2_{type}.png', imgB)
    cv2.waitKey(0)


def compare_whole_folder(type, loc1, loc2, version, version2):
    month = datetime.datetime.now().strftime("%b")
    day = datetime.datetime.now().strftime("%d")

    base_path = 'C:\\Users\\JacksonX\\Desktop\\Testing'

    if not os.path.exists(f'{base_path}\\{month}_{day}\\{type}_{version}_{version2}'):
        os.makedirs(f'{base_path}\\{month}_{day}\\{type}_{version}_{version2}')

    img_dir = f'{base_path}\\{month}_{day}\\{type}_{version}_{version2}'
    document = docx.Document()
    doc_no_diff = docx.Document()

    dir_one = find_files(loc1, ".png")
    dir_two = find_files(loc2, ".png")

    for i, j in zip(dir_one, dir_two):
        print(f'{i} vs {j}')
        compare2(i, j, img_dir, loc1, loc2, type)
    comp_to_doc(document, img_dir, version, version2, base_path, month, day, type)
    add_to_doc(doc_no_diff, loc1, loc2, version, version2, base_path, month, day, type)





