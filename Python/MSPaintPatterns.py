import pyautogui


#Open MS paint

x = 300 #Set (x,y) position
y = x
while(True):
        pyautogui.moveTo(x, y)
        x += 10
        y=x
        print (x,y)
        distance = 210
        distance -= 10
        while distance > 0:
                pyautogui.drag(distance, 0, duration=0)   # move right
                distance -= 5
                pyautogui.drag(0, distance, duration=0)   # move down
                pyautogui.drag(-distance, 0, duration=0)  # move left
                distance -= 5
                pyautogui.drag(0, -distance, duration=0)  # move up
#DO NOT RUN WITHOUT PAINT OPEN I REPEAT DO NOT OPEN WITHOUT PAINT OPEN
#EXIT OUT USING CTRL+ALT+DEL
