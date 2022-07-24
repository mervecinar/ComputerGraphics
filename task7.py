import numpy as np
import cv2
from PIL.Image import Image

im = cv2.imread('merve.jpeg')


def menu():

    x = ""
    while x != "6":
        print("Selection 1 -->  PRESS 1 ")
        print("Selection 2 -->  PRES 2 ")
        print("Selection 3 --> PRESS 3 ")
        print("Selection 4 --> PRESS 4 ")

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
        elif x == "6":
            print("Good bye!")
            break
        else:
            print("TRY AGAIN!")
def F1():
    th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
    cv2.imshow("aa", im_th)
    cv2.waitKey(0)
def F2():
    th, im_th_tz = cv2.threshold(im, 128, 255, cv2.THRESH_TOZERO)
    cv2.imshow("aa",  im_th_tz)
    cv2.waitKey(0)

def F3():
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)


    cv2.imshow("aa", im_gray_th_otsu)
    cv2.waitKey(0)
def F4():
    im_gray = np.array(Image.open('test_gray.jpg').convert('L'))
    im_bin = (im_gray > 128) * 255
    Image.fromarray(np.uint8(im_bin)).save('deneme.jpg')
    img = cv2.imread('deneme.jpg', 0)
    cv2.imshow("aa", img)
    cv2.waitKey(0)



menu()
