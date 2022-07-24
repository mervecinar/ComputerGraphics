import cv2
import numpy as np
from PIL import Image
import colorsys

def mainpanel():
    x = ""
    while x != "3":
        print(" -->> if you want RGB  -->  CMYK PRESS 1")
        print(" ")
        print("-->>  if you want CMYK --> RGB PRESS 2")
        print(" ")
        print("-->>  if you want RGB --> HSV PRESS 3")
        print(" ")
        print("-->>  if you want exit PRESS 4")
        x = input("Please select one of them" )

        if x == "1":
            makeCMYK()
        elif x == "2":
            makeRGB()
        elif x == "3":
            makeHSV()
        elif x == "4":
            print("--Program Terminated!--")
            break
        else:
            print("Please choose one of  them 1 - 2 - 3")

def makeRGB():
    i = cv2.imread('merve.jpeg')
    point = i.astype(np.float) / 255.

    k = 1 - np.max(point, axis=2)
    c = (1 - point[..., 2] - k) / (1 - k)
    m = (1 - point[..., 1] - k) / (1 - k)
    y = (1 - point[..., 0] - k) / (1 - k)

    r = 255 * (1.0 - (c + k) / float(100))
    g = 255 * (1.0 - (m + k) / float(100))
    b = 255 * (1.0 - (y + k) / float(100))

    RGB = (np.dstack((r,g,b)) * 255).astype(np.uint8)

    cv2.imshow('real', i)
    cv2.imshow('CMYK TO RGB ', RGB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def makeCMYK():

    i = cv2.imread('merve.jpeg')
    point = i.astype(np.float) / 255.

    k = 1 - np.max(point, axis=2)
    c = (1 - point[..., 2] - k) / (1 - k)
    m = (1 - point[..., 1] - k) / (1 - k)
    y = (1 - point[..., 0] - k) / (1 - k)

    CMYK = (np.dstack((c, m, y, k)) * 255).astype(np.uint8)

    cv2.imshow('real', i)
    cv2.imshow('RGB TO CMYK', CMYK)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def makeHSV():
    """
    #it's working but the picture is not true colors
    i = Image.open("merve.jpeg")
    renk = i.getpixel((320, 240))
    (r, g, b) = (renk)
    (r, g, b) = (r / 255, g / 255, b / 255)
    (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
    (h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
    HSV = (np.dstack((h, s, v)) * 255).astype(np.uint8)
    cv2.imshow('RGB TO HSV ', HSV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    """

    i = cv2.imread('merve.jpeg')
    HSV = cv2.cvtColor(i, cv2.COLOR_BGR2HSV)
    cv2.imshow('real', i)
    cv2.imshow('HSV ', HSV)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

mainpanel()

