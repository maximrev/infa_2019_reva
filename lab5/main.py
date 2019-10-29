from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __iadd__(self, point):
        self.x+=point.x
        self.y+=point.y
        return self

class Ball():
    def __init__(self, point, speed, r):
        self.r = r
        self.point = point
        self.speed = speed
        self.ball = new_ball(point, r)
        self.move()

    def move(self):
        if(self.point.x>=800 or self.point.x<=0):
            self.speed.x = -self.speed.x
        if(self.point.y>=600 or self.point.y<=0):
            self.speed.y = -self.speed.y
        self.point += self.speed
        canv.move(self.ball, self.speed.x, self.speed.y)

class World:
    def __init__(self, num):
        self.ball = []
        self.num=num
        for i in range(self.num):
            self.ball.append(Ball(Point(rnd(0,800),rnd(0,600)), Point(rnd(8,20),rnd(5,15)), rnd(15,30)))
        self.update()

    def update(self):
        self.distance = [[0] * self.num for i in range(self.num)]
        for i in range(self.num):
            for b in range(self.num):
                self.distance[i][b] = ((self.ball[i].point.x - self.ball[b].point.x)**2 + (self.ball[i].point.y - self.ball[b].point.y)**2)**(1/2)
        stolk = [[0] * self.num for i in range(self.num)]
        for i in range(self.num):
            for b in range(self.num):
                if(self.distance[i][b]<=self.ball[i].r + self.ball[b].r and stolk[i][b] == 0):
                    stolk[i][b] = 1
                    stolk[b][i] = 1
                    buf = self.ball[i].speed
                    self.ball[i].speed = self.ball[b].speed
                    self.ball[b].speed = buf
            self.ball[i].move()
        for i in range(self.num):
            for b in range(self.num):
                stolk[i][b] = 0
                stolk[b][i] = 0
        root.after(10, self.update)
        
def new_ball(point, r):
    return canv.create_oval(point.x-r,point.y-r,point.x+r,point.y+r,fill = choice(colors), width=0)

def click(event):
    print('click')

world = World(30)

canv.bind('<Button-1>', click)
mainloop()
