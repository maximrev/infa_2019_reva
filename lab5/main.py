from tkinter import *
from random import randrange as rnd, choice
import time, math
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
		self.x += point.x
		self.y += point.y
		return self

	def __sub__(self, point):
		return Point(self.x - point.x, self.y - point.y)

	def __isub__(self, point):
		self.x -= point.x
		self.y -= point.y
		return self

	def __truediv__(self, num):
		self.x /= num
		self.y /= num
		return self

	def __mul__(self, num):
		self.x *= num
		self.y *= num
		return self

	def module(self):
		return (self.x ** 2 + self.y ** 2) ** (1/2)

class Ball():
	def __init__(self, point, speed, r):
		self.r = r
		self.point = point
		self.speed = speed
		self.mass = self.r ** 3
		self.ball = new_ball(point, r)
		self.move()

	def move(self):
		if(self.speed.module() > 30):
			self.speed = self.speed * 30 / self.speed.module() 
		if(self.point.x > 800 or self.point.x < 0):
			self.speed.x = -self.speed.x
		if(self.point.y > 600 or self.point.y < 0):
			self.speed.y = -self.speed.y
		self.point += self.speed
		canv.move(self.ball, self.speed.x, self.speed.y)

class World: #My Best Creation In This World
	def __init__(self, dt, num, k, g):
		self.ball = []
		self.num=num
		self.k = k
		self.dt = dt
		self.g = g
		for i in range(self.num):
			self.ball.append(Ball(Point(rnd(0,800),rnd(0,600)), Point(rnd(5,15), rnd(5,15)), rnd(10, 20)))
		self.update()

	def update(self):
		self.hit()
		self.gravity()
		self.resistance()
		self.move()
		root.after(self.dt, self.update)

	def move(self):
		for i in range(self.num):
			self.ball[i].move()

	def gravity(self):
		for i in range(self.num):
			self.ball[i].speed += self.g * self.dt

	def resistance(self):
		for i in range(self.num):
			self.ball[i].speed = self.ball[i].speed * math.exp((-1) * self.k / self.ball[i].r * self.dt)

	def hit(self):
		self.distance = [[0] * self.num for i in range(self.num)]
		for i in range(self.num):
			for b in range(self.num):
				self.distance[i][b] = (self.ball[i].point - self.ball[b].point).module()
		stolk = [[0] * self.num for i in range(self.num)]
		for i in range(self.num):
			for b in range(self.num):
				if(self.distance[i][b] < self.ball[i].r + self.ball[b].r and stolk[i][b] == 0):
					stolk[i][b] = 1
					stolk[b][i] = 1
					self.ball[i].speed += (self.ball[i].point - self.ball[b].point) / (self.distance[i][b] + (self.ball[i].r + self.ball[b].r) / 2) * (self.ball[i].r + self.ball[b].r - self.distance[i][b]) / self.ball[i].mass * self.ball[b].mass * self.dt
					self.ball[b].speed += (self.ball[b].point - self.ball[i].point) / (self.distance[i][b] + (self.ball[i].r + self.ball[b].r) / 2) * (self.ball[i].r + self.ball[b].r - self.distance[i][b]) * self.dt 
		for i in range(self.num):
			for b in range(self.num):
				stolk[i][b] = 0
				stolk[b][i] = 0

def new_ball(point, r):
	return canv.create_oval(point.x-r,point.y-r,point.x+r,point.y+r,fill = choice(colors), width=0)

def click(event):
	print('click')

world = World(1, 100, 0.01 , Point(0,0.01))

canv.bind('<Button-1>', click)
mainloop()
