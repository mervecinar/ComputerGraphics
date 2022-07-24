import cv2
def controller(img, brightness=255,contrast=127):
    brightness = int((brightness - 0) * (255 - (-255)) / (510 - 0) + (-255))
    contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255 + brightness
        x = (max - shadow) / 255
        y = shadow

        a = cv2.addWeighted(img, x,img, 0, y)

    else:
        a = img
    if contrast != 0:
        Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        Gamma = 127 * (1 - Alpha)
        a = cv2.addWeighted(a, Alpha, a, 0, Gamma)
    return a
def ChangeBrig(brightness,contrast):

    result = controller(img, brightness,
                        contrast)
    cv2.imshow('New Picture', result)

if __name__ == '__main__':
    s1 = input("Please enter the value of Brightness")
    s2 = input("Please enter the value of Contrast")
    sayi1 = int(s1)
    sayi2 = int(s2)
    orginalPic = cv2.imread("merve.jpeg")
    img = orginalPic.copy()
    cv2.namedWindow('Picture')
    cv2.imshow('Picture', orginalPic)
    ChangeBrig(sayi1,sayi2)
cv2.waitKey(0)