import cv2
import numpy as np

def face_detection(img : np.ndarray, title : str) -> np.ndarray:
    """
    >>> face_detection('gambar.jpg',"Gambarku")
    """
    face_cascade = cv2.CascadeClassifier('requirement/haarcascade_frontalface_default.xml')
    image = cv2.imread(img)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    model = face_cascade.detectMultiScale(grayscale, 1.1, 4)
    for (x,y,w,h) in model:
        cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow(title,image)
    cv2.waitKey()