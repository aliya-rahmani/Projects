'''
Prerequisites:
pip install opencv-python opencv-contrib-python
pip install imutils

This script can be used to detect and extract text from a given image (co-ordinates are extracted).
As of right now the extracted ROI is put inside a rectangle.
The algorithm used is OpenCV EAST (Efficiend and Accurate Scene Text Detection)

Contributor's Note:
The recognition operation can also be performed using Tesseract API howevver it does perform well on real time video feed.
'''


from imutils.object_detection import non_max_suppression
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"]

print("Loading EAST text detector...")
net = cv2.dnn.readNet("frozen_east_text_detection.pb")


def decode_predictions(scores, geometry):
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []
    
    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]

        for x in range(0, numCols):
            if scoresData[x] < 0.5:
                continue

            (offsetX, offsetY) = (x * 4.0, y * 4.0)

            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)

            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])

    return (rects, confidences)


def detection_func(im):
    orig = im.copy()
    (origH, origW) = im.shape[:2]
    (newW, newH) = (320, 320)
    rW = origW / float(newW)
    rH = origH / float(newH)
    im = cv2.resize(im, (newW, newH))
    (H, W) = im.shape[:2]
    
    # construct a blob from the image and then perform a forward pass of
    # the model to obtain the two output layer sets
    blob = cv2.dnn.blobFromImage(im, 1.0, (W, H),
        (123.68, 116.78, 103.94), swapRB=True, crop=False)
    net.setInput(blob)
    (scores, geometry) = net.forward(layerNames)
    
    (rects, confidences) = decode_predictions(scores, geometry)
    boxes = non_max_suppression(np.array(rects), probs=confidences)

    results = list()
    for (startX, startY, endX, endY) in boxes:
        startX = int(startX * rW)
        startY = int(startY * rH)
        endX = int(endX * rW)
        endY = int(endY * rH)
        cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
        
        
    return orig


def main():
    while True:
        ret,frame = cam.read()
        frame = detection_func(frame)
        cv2.imshow("detection !",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":       
    main()