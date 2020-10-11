import cv2 as cv

img = cv.imread('resources/testSubject.jpeg',0)
imgCanny = cv.Canny(img,100,150)

cv.namedWindow('Output2',cv.WINDOW_NORMAL)
cv.imshow("Output2",imgCanny)
cv.waitKey(0)
cv.destroyAllWindows()
