from p5 import *
import random

WIDTH, HEIGHT = 800, 600

class Ball:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.x_speed = random.uniform(-1, 1)
        self.y_speed = random.uniform(-1, 1)
        self.color = (random.uniform(0, 255), random.uniform(0, 255), random.uniform(0, 255))

        x0 = self.x - self.r / 2
        y0 = self.y - self.r / 2
        x1 = self.x + self.r / 2
        y1 = self.y + self.r / 2

    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        x0 = self.x - self.r / 2
        y0 = self.y - self.r / 2
        x1 = self.x + self.r / 2
        y1 = self.y + self.r / 2
        if x0 <= 0 or x1 >= WIDTH:
            self.x_speed = -self.x_speed

        if y0 <= 0 or y1 >= HEIGHT:
            self.y_speed = -self.y_speed 

    def show(self):
        fill(self.color[0], self.color[1], self.color[2])
        circle((self.x, self.y), self.r)
           

#--------------------------------------------------------------------

def setup():
    size(WIDTH, HEIGHT)
    no_stroke()

def draw():
    background(255)
    
    for ball in balls:
        ball.update()
        ball.show()

balls = []
def mouse_clicked(event):
    balls.append(Ball(event.x, event.y, 50))

run()