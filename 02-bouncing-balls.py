from tkinter import *
import random
import time

WIDTH, HEIGHT = 800, 600

root = Tk()

class Ball:
    def __init__(self, x, y, r, x_speed, y_speed):
        self.x = x
        self.y = y
        self.r = r
        self.x_speed = x_speed
        self.y_speed = y_speed

        x0 = self.x - self.r//2
        y0 = self.y - self.r//2
        x1 = self.x + self.r//2
        y1 = self.y + self.r//2

        # random hex color
        color = '#' + "%06x" % random.randint(0, 0xFFFFFF)
        self.shape = canvas.create_oval(x0, y0, x1, y1, fill=color, outline=color)

    def update(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

        x0 = self.x - self.r//2
        y0 = self.y - self.r//2
        x1 = self.x + self.r//2
        y1 = self.y + self.r//2
        if x0 <= 0 or x1 >= WIDTH:
            self.x_speed = -self.x_speed

        if y0 <= 0 or y1 >= HEIGHT:
            self.y_speed = -self.y_speed 

        canvas.move(self.shape, self.x_speed, self.y_speed)

balls = []
def MouseClick(event):
    b = Ball(event.x, event.y, 50, random.random(), random.random()) 
    balls.append(b)

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.bind("<ButtonPress>", MouseClick)
canvas.pack()

while True:
    for ball in balls:
        ball.update()
    root.update()
    time.sleep(0.001)

mainloop()