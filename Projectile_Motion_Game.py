import pygame
import math

wScreen = 1200
hScreen = 500

win = pygame.display.set_mode((wScreen,hScreen))
pygame.display.set_caption('Projectile Motion')

class ball(object):
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
    def draw(self, win):
        pygame.draw.circle(win, (0,0,0), (self.x,self.y), self.radius)          # Draw a black Circle
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius-1)     # Draw a white circle on top of it

    @staticmethod
    def ballPath(startx, starty, power, ang, time):         # Determine the path of the ball when mouse button pressed
        angle = ang
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power
        distX = velx * time
        distY = (vely * time) + ((-4.9 * (time ** 2)) / 2)      # distY = vt - 1/2gt^2
        newx = round(distX + startx)
        newy = round(starty - distY)

        return (newx, newy)

def redrawWindow():
    win.fill((64,64,64))
    golfBall.draw(win)
    pygame.draw.line(win, (0,0,0),line[0], line[1])         # Line connecting the ball and the mouse cursor
    pygame.display.update()

def findAngle(pos):
    sX = golfBall.x
    sY = golfBall.y
    try:
        angle = math.atan((sY - pos[1]) / (sX - pos[0]))        # angle = taninverse((y2 - y1)/(x2 - x1))
    except:
        angle = math.pi / 2
    if pos[1] < sY and pos[0] > sX:
        angle = abs(angle)
    elif pos[1] < sY and pos[0] < sX:
        angle = math.pi - angle
    elif pos[1] > sY and pos[0] < sX:
        angle = math.pi + abs(angle)
    elif pos[1] > sY and pos[0] > sX:
        angle = (math.pi * 2) - angle
    return angle

golfBall = ball(300,494,5,(255,255,255))

run = True
time = 0
power = 0
angle = 0
shoot = False
clock = pygame.time.Clock()
while run:
    clock.tick(200)
    if shoot:
        if golfBall.y < 500 - golfBall.radius:
            time += 0.05
            po = ball.ballPath(x, y, power, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            shoot = False
            time = 0
            golfBall.y = 494
    line = [(golfBall.x, golfBall.y), pygame.mouse.get_pos()]
    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not shoot:
                x = golfBall.x
                y = golfBall.y
                pos =pygame.mouse.get_pos()
                shoot = True
                power = math.sqrt((line[1][1]-line[0][1])**2 +(line[1][0]-line[0][1])**2)/8
                angle = findAngle(pos)

pygame.quit()
quit()
