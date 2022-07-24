from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import cv2

def makeHis(filename):
    img = cv2.imread(filename, 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

def normalizeRed(intensity):
    iI = intensity
    minI = 86
    maxI = 230
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def normalizeGreen(intensity):
    iI = intensity
    minI = 90
    maxI = 225
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO

def normalizeBlue(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    iO = (iI - minI) * (((maxO - minO) / (maxI - minI)) + minO)
    return iO


img = cv2.imread('merve.jpeg', 0)
plt.imshow(img, cmap='gray')


def make_histogram(image, bins=256):
    histogram = np.zeros(bins)
    for pixel in image:
        histogram[pixel] += 1


    return histogram
def cumsum(values):
    result = [values[0]]
    for i in values[1:]:
        result.append(result[-1] + i)
    return result


def normalize(entries):
    numerator = (entries - np.min(entries)) * 255
    denorminator = np.max(entries) - np.min(entries)
    result = numerator / denorminator
    result.astype('uint8')
    return result


def equalizeHist(img):
    flatten_img = img.flatten()
    cumulativeSum = cumsum(make_histogram(flatten_img))
    cumulativeSum_norm = normalize(cumulativeSum)
    img_new_his = cumulativeSum_norm[flatten_img]
    img_new = np.reshape(img_new_his, img.shape)
    return img_new, cumulativeSum_norm


def drawImage(im, sonuc):
    f, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].imshow(im, cmap='gray')
    axes[0, 0].set_title('image with non Histogram equalization')

    axes[1, 0].hist(im.flatten(), 256, [0, 256])

    axes[0, 1].imshow(sonuc, cmap='gray')
    axes[0, 1].set_title('image with Histogram equalization')

    axes[1, 1].hist(sonuc.ravel(), 256, [0, 256]);
    f.savefig('sonuc.png')
    plt.show()

#-------
i2 = cv2.imread('merve.jpeg', 0)
plt.imshow(i2, cmap='gray')
result, normalized_cumsum = equalizeHist(i2)
drawImage(i2, result)
#-------
i = Image.open("merve.jpeg")
i.show()
A = i.split()
normRed = A[0].point(normalizeRed)
normBlue = A[1].point(normalizeGreen)
normGreen = A[2].point(normalizeBlue)
normalize = Image.merge("RGB", (normRed, normBlue, normGreen))
normalize.show()
normalize.save("normalize.jpg")
makeHis("normalize.jpg")
