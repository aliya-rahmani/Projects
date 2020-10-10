# OpenCV Python program for Vehicle detection in a Video frame -

# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV 
import cv2 

# capture frames from a video 
cap = cv2.VideoCapture('road.mp4') 

# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('required_haarCascade.xml') 

# loop runs if capturing has been initialized. 
while True:

	# reads frames from a video
    ret, frames = cap.read() 
	
	# convert to gray scale of each frames 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
	
	# Detects cars of different sizes in the input image 
    cars = car_cascade.detectMultiScale(gray, 1.1,4) 
	
	# To draw a rectangle in each cars 
    for (x ,y , w , h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 

    # Display frames in a window 
    cv2.imshow('Result_video', frames) 
	
	# Wait for Space key to stop 
    if cv2.waitKey(10) == 32: 
        break

# De-allocate any associated memory usage 
cv2.destroyAllWindows() 
