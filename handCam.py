import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(maxHands=2)
video = cv2.VideoCapture(0)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hand = detector.findHands(img, draw=False)
    if hand:
        lmlist = hand[0]
        if lmlist:
            fingerup = detector.fingersUp(lmlist)
            if fingerup == [0, 0, 0, 0, 0]:
                print("No Finger Detected")
            if fingerup == [1, 0, 0, 0, 0]:
                print("Thumb")
            if fingerup == [0, 1, 0, 0, 0]:
                print("Index Finger")
            if fingerup == [0, 0, 1, 0, 0]:
                print("Middle Finger")
            if fingerup == [0, 0, 0, 1, 0]:
                print("Ring Finger")
            if fingerup == [0, 0, 0, 0, 1]:
                print("Pinky")

    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)

video.release()
cv2.destroyAllWindows()