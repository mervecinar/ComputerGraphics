from PIL import Image
import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

im = Image.open('Campus.jpg').convert('HSV')
Hue = np.array(im.getchannel('H'))
mask = np.zeros_like(Hue, dtype=np.uint8)
mask[(Hue>80) & (Hue<90)] = 1
print((mask.mean()*100))
a=str(mask.mean()*100)
img = Image.open('Campus.jpg')
I1 = ImageDraw.Draw(img)
myFont =ImageFont.truetype("arial.ttf", 35)
I1.text((20, 50), "%"+ a + " is covered by green", font=myFont, fill=(255,69,0))
img.show()