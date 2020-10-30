import cv2

capture_again=True
while capture_again:
    capture=cv2.VideoCapture(0)    
    status,photo=capture.read()
    cv2.imshow("here is your pic",photo)
                    
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    capture.release()

    user_input=int(input("would you like to captuer again?\n1.Yes\n2.No"))

    if user_input==1:
        continue
    else:
        capture_again=False
        break


    
            
    
