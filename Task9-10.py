
import numpy as np
from PIL import ImageOps
from skimage import io
from skimage import transform as tf
import cv2


im = cv2.imread('merve.jpeg')


def menu():

    x = ""
    while x != "6":
        print("Rotate Image   -->  PRESS 1 ")
        print("Shearing Image -->  PRES 2 ")
        print("Reflection of  Image --> PRESS 3 ")

        print("To exit press 6")
        x = input("Please select one of them")

        if x == "1":
            F1()
        elif x == "2":
            F2()
        elif x == "3":
            F3()

        elif x == "6":
            print("Good bye!")
            break
        else:
            print("TRY AGAIN!")
def F1():
    image = cv2.imread("merve.jpeg")
    image_norm = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)


    cv2.imshow('original Image', image)
    cv2.imshow('Rotated Image', image_norm)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def F2():
    # Load the image as a matrix
    image = io.imread("merve.jpeg")

    # Create Afine transform
    afine_tf = tf.AffineTransform(shear=0.2)

    # Apply transform to image data
    modified = tf.warp(image, inverse_map=afine_tf)

    # Display the result
    io.imshow(modified)
    io.show()
def F3():
    # Read input image
    img = cv2.imread('merve.jpeg')

    # Mirror in x direction (flip horizontally)
    imgX = np.flip(img, axis=1)
    # imgX = imgX = img[:, ::-1, :]

    # Mirror in y direction (flip vertically)
    imgY = np.flip(img, axis=0)
    # imgY = img[::-1, :, :]

    # Mirror in both directions (flip horizontally and vertically)
    imgXY = np.flip(img, axis=(0, 1))
    # imgXY = img[::-1, ::-1, :]

    # Outputs
    cv2.imshow('img', img)
    cv2.imshow('imgX', imgX)
    cv2.imshow('imgY', imgY)
    cv2.imshow('imgXY', imgXY)
    cv2.waitKey(0)

menu()

