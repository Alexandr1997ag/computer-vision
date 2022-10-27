import cv2 as cv
from matplotlib import pyplot as plt
import pyautogui
import numpy as np

cap = cv.VideoCapture("video.mp4")
while True:
	# Читать картинку
    ret, frame = cap.read()
    if ret == False:
        break
    im = cv.imshow("frame", frame)
    # Если вы введете 'c', он будет вырезан.
    if cv.waitKey(10) == ord("c"):
        image = pyautogui.screenshot()
        image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)
        cv.imwrite("1.png", image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    if cv.waitKey(10) == ord('q'):
        break