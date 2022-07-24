import cv2
import numpy
import numpy as np
def main():
    x = ""
    while x != "6":
        print("Smoothing Filter (Averaging) -->  PRESS 1 ")
        print("Median Filter -->  PRES 2 ")
        print("Edge Detection Filter (Sobel) --> PRESS 3 ")
        print("High Pass Filter Sharpen --> PRESS 4 ")
        print("Gaussian Blur Filter --> PRESS 5")
        print("To exit press 6")
        x = input("Please select one of them")

        if x == "1":
            Averaging()
        elif x == "2":
            MedianFilter()
        elif x == "3":
            EdgeDetection()
        elif x == "4":
            HighPass()
        elif x == "5":
            GaussianBlur()
        elif x == "6":
            print("Good bye!")
            break
        else:
            print("TRY AGAIN!")

def EdgeDetection():
    """
        # here is the Sobel Edge images
        sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
        sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
        sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
        # Display Sobel Edge Detection Images
        cv2.imshow('Sobel X', sobelx)
        cv2.waitKey(0)
        cv2.imshow('Sobel Y', sobely)
        cv2.waitKey(0)
        cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
        cv2.waitKey(0)
    """

    i = cv2.imread('merve.jpeg')
    img_gray = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
    edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
    cv2.imshow('Non Filter', i)
    cv2.waitKey(0)
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def HighPass():
    image = cv2.imread('merve.jpeg')
    kernel = np.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
    sharpened = cv2.filter2D(image, -1, kernel)

    cv2.imshow('Image Sharpening', numpy.hstack((image, sharpened)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def GaussianBlur():
    src = cv2.imread('merve.jpeg', cv2.IMREAD_UNCHANGED)

    # apply guassian blur on src image
    dst = cv2.GaussianBlur(src, (5, 5), cv2.BORDER_DEFAULT)

    cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def MedianFilter():
    img_noisy1 = cv2.imread('MedFilt.jpg', 0)
    m, n = img_noisy1.shape
    img_new1 = np.zeros([m, n])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = [img_noisy1[i - 1, j - 1],
                    img_noisy1[i - 1, j],
                    img_noisy1[i - 1, j + 1],
                    img_noisy1[i, j - 1],
                    img_noisy1[i, j],
                    img_noisy1[i, j + 1],
                    img_noisy1[i + 1, j - 1],
                    img_noisy1[i + 1, j],
                    img_noisy1[i + 1, j + 1]]

            temp = sorted(temp)
            img_new1[i, j] = temp[4]

    img_new1 = img_new1.astype(np.uint8)
    cv2.imshow("Median Filter", numpy.hstack((img_noisy1, img_new1)))
    cv2.waitKey(0)


def Averaging():
    img = cv2.imread('merve.jpeg', 0)
    m, n = img.shape

    mask = np.ones([3, 3], dtype=int)
    mask = mask / 9

    img_new = np.zeros([m, n])

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            temp = img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + img[
                i, j - 1] * mask[1, 0] + img[i, j] * mask[1, 1] + img[i, j + 1] * mask[1, 2] + img[i + 1, j - 1] * mask[
                       2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]

            img_new[i, j] = temp

    img_new = img_new.astype(np.uint8)
    cv2.imshow("Averaging", numpy.hstack((img, img_new)))
    cv2.waitKey(0)

main()
