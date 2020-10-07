import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

trackbar = np.zeros((100, 700), np.uint8)
cv2.namedWindow("trackbar")

cv2.createTrackbar("L - h", "trackbar", 0, 179, nothing)
cv2.createTrackbar("U - h", "trackbar", 179, 179, nothing)
cv2.createTrackbar("L - s", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U - s", "trackbar", 255, 255, nothing)
cv2.createTrackbar("L - v", "trackbar", 0, 255, nothing)
cv2.createTrackbar("U - v", "trackbar", 255, 255, nothing)
cv2.createTrackbar("S ROWS", "trackbar", 0, 480, nothing)
cv2.createTrackbar("E ROWS", "trackbar", 480, 480, nothing)
cv2.createTrackbar("S COLS", "trackbar", 0, 640, nothing)
cv2.createTrackbar("E COLS", "trackbar", 640, 640, nothing)

while True:
    ret, frame = cap.read()
    # print(frame.shape)

    s_r = cv2.getTrackbarPos("S ROWS", "trackbar")
    e_r = cv2.getTrackbarPos("E ROWS", "trackbar")
    s_c = cv2.getTrackbarPos("S COLS", "trackbar")
    e_c = cv2.getTrackbarPos("E COLS", "trackbar")

    roi = frame[s_r: e_r, s_c: e_c]

    frame_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - h", "trackbar")
    u_h = cv2.getTrackbarPos("U - h", "trackbar")
    l_s = cv2.getTrackbarPos("L - s", "trackbar")
    u_s = cv2.getTrackbarPos("U - s", "trackbar")
    l_v = cv2.getTrackbarPos("L - v", "trackbar")
    u_v = cv2.getTrackbarPos("U - v", "trackbar")

    lower_hsv = np.array([l_h, l_s, l_v])
    upper_hsv = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(frame_hsv, lower_hsv, upper_hsv)
    mask_inv = cv2.bitwise_not(mask)

    bg = cv2.bitwise_and(roi, roi, mask=mask)
    fg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("trackbar", trackbar)
    cv2.imshow("Background", bg)
    cv2.imshow("Foreground", fg)

    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
