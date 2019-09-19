from graph import *
import numpy as np
from math import sin, cos, pi, sqrt

def ellipse_dot(t, a, b,x,y,f):
    return a*cos(t)*cos(f) + b*sin(t)*sin(f) + x, -a*cos(t)*sin(f) + b*sin(t)*cos(f) + y

def ellipse(a,b,x,y,f):
    points = [ellipse_dot(t, a, b,x,y,f) for t in np.linspace(0, 2*pi, num=100)]
    return points

def duga(a,b,x,y,f):
    points = [ellipse_dot(t, a, b,x,y,f) for t in np.linspace(gtr(100), gtr(180), num=100)]
    return points

def gtr(f):
    return f/180*pi

def ellipse_dot_matrix(t,a,b):
    return a*cos(t),b*sin(t)

def ellipse_matrix(a,b):
    points = np.matrix([ellipse_dot_matrix(t, a, b) for t in np.linspace(0, 2*pi, num=100)])
    return points

width, height = windowSize()

def povorot(f):
    return np.matrix([(cos(f),-sin(f)),(sin(f),cos(f))])

brushColor("black")
rectangle(0,0,width,height)

brushColor(255,175,128)
rectangle(0,75,width,height-75)

brushColor("red")
polygon(np.dot(ellipse_matrix(150,100),povorot(gtr(30))).tolist())

penColor("green")
polyline(duga(200,100,300,400,180))

run()

    
