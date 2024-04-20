import time
from typing import Sequence

import cv2
import numpy
from PIL import Image, ImageFilter
import mediapipe as mp
from PIL.ImageDraw import ImageDraw
from matplotlib import image

from DRAWER.drawer import Drawer


class VISION:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FPS, 24)  # Частота кадров
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)  # Ширина кадров в видеопотоке.
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Высота кадров в видеопотоке.

        self.update()

    def update(self):

        hands = mp.solutions.hands.Hands(max_num_hands=1)  # Объект ИИ для определения ладони
        draw = mp.solutions.drawing_utils  # Для рисование ладони
        ptime = 0
        RX1 = 100
        RX2 = RX1 + 100
        RY1 = 100
        RY2 = RY1 + 100

        FINGER4 = (0, 0)
        FINGER8 = (0, 0)
        F4P = (0, 0)
        while True:

            ret, CAMERAIMG = self.cap.read()

            CAMERAIMG = cv2.flip(CAMERAIMG, 1)  # Отражаем изображение для корекктной картинки

            results = hands.process(cv2.cvtColor(CAMERAIMG, cv2.COLOR_BGR2RGB))  # Работа mediapipe




            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = CAMERAIMG.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if id==4:
                            cv2.circle(CAMERAIMG, (cx, cy), 8,(0, 0, 255), 5)
                            FINGER4 = (cx, cy)
                        if id==8:
                            cv2.circle(CAMERAIMG, (cx, cy), 8,(0, 0, 255), 5)
                            FINGER8 = (cx, cy)

                    draw.draw_landmarks(CAMERAIMG, handLms, mp.solutions.hands.HAND_CONNECTIONS)  # Рисуем ладонь


            if FINGER4 != FINGER8 and abs(FINGER4[0]-FINGER8[0])<20 and abs(FINGER4[1]-FINGER8[1])<20:
                if abs(FINGER4[0] in range(RX1, RX2) and abs(FINGER4[1] in range(RY1, RY2))):
                    F4P = FINGER4
                else:
                    RX1 += FINGER4[0] - F4P[0]
                    RY1 += FINGER4[1] - F4P[1]

                    RX2 = RX1 + 100
                    RY2 = RY1 + 100


            ctime = time.time()

            cv2.putText(CAMERAIMG, f'FPS:{int(1/(ctime-ptime))}', (10, 15), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            ptime = ctime

            CAMERAIMG = cv2.rectangle(CAMERAIMG, (RX1, RY1), (RX2, RY2), (0, 255, 0), 2)



            cv2.imshow("camera", CAMERAIMG)
            if cv2.waitKey(10) == 27:  # Клавиша Esc
                break
        self.exit()

    def exit(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    vision = VISION()





