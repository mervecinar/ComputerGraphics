import cv2 as cv
import numpy as np
import numpy as np
import cv2
import cv2
import sys
from PIL.Image import Image

im = cv2.imread('merve.jpeg')


def menu():

    x = ""
    while x != "6":
        print("Hit Or Miss  -->  PRESS 1 ")
        print("Dilation Filter -->  PRES 2 ")
        print("Erosion Image --> PRESS 3 ")
        print("Opening Image --> PRESS 4 ")
        print("Closing Image --> PRESS 5")
        print("To exit press 6")
        x = input("Please select one of them")

        if x == "1":
            F1()
        elif x == "2":
            F2()
        elif x == "3":
            F3()
        elif x == "4":
            F4()
        elif x == "5":
            F5()
        elif x == "6":
            print("Good bye!")
            break
        else:
            print("TRY AGAIN!")
def F1():
    input_image = np.array((
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 255, 255, 255, 0, 0, 0, 255],
        [0, 255, 255, 255, 0, 0, 0, 0],
        [0, 255, 255, 255, 0, 255, 0, 0],
        [0, 0, 255, 0, 0, 0, 0, 0],
        [0, 0, 255, 0, 0, 255, 255, 0],
        [0, 255, 0, 255, 0, 0, 255, 0],
        [0, 255, 255, 255, 0, 0, 0, 0]), dtype="uint8")
    kernel = np.array((
        [0, 1, 0],
        [1, -1, 1],
        [0, 1, 0]), dtype="int")
    output_image = cv.morphologyEx(input_image, cv.MORPH_HITMISS, kernel)
    rate = 50
    kernel = (kernel + 1) * 127
    kernel = np.uint8(kernel)
    kernel = cv.resize(kernel, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
    cv.imshow("kernel", kernel)
    cv.moveWindow("kernel", 0, 0)
    input_image = cv.resize(input_image, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
    cv.imshow("Original", input_image)
    cv.moveWindow("Original", 0, 200)
    output_image = cv.resize(output_image, None, fx=rate, fy=rate, interpolation=cv.INTER_NEAREST)
    cv.imshow("Hit or Miss", output_image)
    cv.moveWindow("Hit or Miss", 500, 200)
    cv.waitKey(0)
    cv.destroyAllWindows()


def F2():
    img=cv2.imread('merve.jpeg',1)
    cv2.imshow('Orginal',img)
    kernel=np.ones((5,5),'uint8')
    dilate_img=cv2.dilate(img,kernel,iterations=1)
    cv2.imshow('Dilated Image', dilate_img)
    cv2.waitKey(0)

def F3():
    img = cv2.imread('merve.jpeg', 0)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img,kernel,iterations = 1)
    cv2.imshow('Orginal Image', img)
    cv2.imshow('Erosion Image', erosion)
    cv2.waitKey(0)
def F4():
    img = cv2.imread('merve.jpeg', 0)
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Orginal Image', img)
    cv2.imshow('Opening Image', opening)
    cv2.waitKey(0)
def F5():
    img = cv2.imread('merve.jpeg', 0)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Orginal Image', img)
    cv2.imshow('Closing Image', closing)
    cv2.waitKey(0)
menu()

