import numpy as np
import cv2
import pytesseract as pt
import matplotlib.pyplot as plt

foto = cv2.imread('./foto/Netflix.png')

plt.imshow(foto)
plt.show()

metin = pt.image_to_string(foto)
print(metin)