import cv2
import mediapipe as mp
import pyautogui
import math
import numpy as np
import time

cap = cv2.VideoCapture(0)
hand = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
draw = mp.solutions.drawing_utils
screen_w, screen_h = pyautogui.size()
prev_x, prev_y = 0, 0
smoothening = 5
click_down = False
click_start = 0

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand.process(rgb)

    if result.multi_hand_landmarks:
        for lm in result.multi_hand_landmarks:
            draw.draw_landmarks(frame, lm, mp.solutions.hands.HAND_CONNECTIONS)
            data = [(int(p.x * w), int(p.y * h)) for p in lm.landmark]
            index, thumb, middle, ring = data[8], data[4], data[12], data[16]

            # Smooth cursor movement
            x = np.interp(index[0], (0, w), (0, screen_w))
            y = np.interp(index[1], (0, h), (0, screen_h))
            final_x = prev_x + (x - prev_x) / smoothening
            final_y = prev_y + (y - prev_y) / smoothening
            pyautogui.moveTo(final_x, final_y)
            prev_x, prev_y = final_x, final_y

            # Click / Double Click
            dist_thumb_index = distance(index, thumb)
            if dist_thumb_index < 40:
                if not click_down:
                    click_start = time.time()
                    click_down = True
                elif time.time() - click_start > 1:
                    pyautogui.doubleClick()
                    click_down = False
            else:
                if click_down and 0 < time.time() - click_start <= 1:
                    pyautogui.click()
                click_down = False

            # 🔁 Smooth Scroll (speed = 100)
            index_middle_gap = distance(index, middle)
            if index_middle_gap < 40:
                if index[1] < middle[1]:  # scroll up
                    pyautogui.scroll(100)
                else:  # scroll down
                    pyautogui.scroll(-100)

            # 🧲 Zoom In (Thumb + Index pinch)
            if distance(index, thumb) < 30:
                pyautogui.hotkey('ctrl', '+')

            # 🧲 Zoom Out (Thumb + Middle pinch)
            if distance(middle, thumb) < 30:
                pyautogui.hotkey('ctrl', '-')

            # Drag: thumb + ring
            if distance(thumb, ring) < 40:
                pyautogui.mouseDown()
            else:
                pyautogui.mouseUp()

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
