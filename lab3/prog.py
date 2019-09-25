from graph import *
import numpy as np
from math import sin, cos, pi, sqrt

def ellipse_dot(t, a, b,x,y,f):
    return a*cos(t)*cos(f) + b*sin(t)*sin(f) + x, -a*cos(t)*sin(f) + b*sin(t)*cos(f) + y

def ellipse(a,b,x,y,f):
    points = [ellipse_dot(t, a, b,x,y,f) for t in np.linspace(0, 2*pi, num=100)]
    return points

def duga(a,b,x,y,f):
    points = [((np.dot(ellipse_dot_matrix(t, a, b),povorot(f))+ matrix_move(x,y)).item(0,0),(np.dot(ellipse_dot_matrix(t, a, b),povorot(f))+ matrix_move(x,y)).item(0,1)) for t in np.linspace(gtr(100), pi, num=100)]
    return points

def gtr(f):
    return f/180*pi

def ellipse_dot_matrix(t,a,b):
    return np.matrix([a*cos(t),b*sin(t)])

def matrix_move(x,y):
    matr = np.matrix([x,y])
    return matr

def povorot(f):
    return np.matrix([(cos(f),-sin(f)),(sin(f),cos(f))])

def ellipse_matrix(a,b,x,y,f):
    points = [((np.dot(ellipse_dot_matrix(t, a, b),povorot(f))+ matrix_move(x,y)).item(0,0),(np.dot(ellipse_dot_matrix(t, a, b),povorot(f))+ matrix_move(x,y)).item(0,1)) for t in np.linspace(0, 2*pi, num=100)]
    return points

def panda(s,x,y,f):
    brushColor("black")
    penColor("black")
    polygon(ellipse_matrix(s*60,s*30,x-s*120,y+s*60,f+gtr(90)))
    polygon(ellipse_matrix(s*25,s*15,x-s*110,y-s*80,f+gtr(45)))
    polygon(ellipse_matrix(s*25,s*15,x-s*50,y-s*80,f-gtr(45)))
    brushColor("white")
    penColor("white")
    polygon(ellipse_matrix(s*100,s*50,x,y,f))
    polygon(ellipse_matrix(s*70,s*60,x-s*75,y-s*20,f+gtr(90)))
    brushColor("black")
    penColor("black")
    polygon(ellipse_matrix(s*70,s*30,x+s*50,y+s*55,f+gtr(60)))
    polygon(ellipse_matrix(s*70,s*25,x-s*45,y+s*55,f+gtr(90)))
    polygon(ellipse_matrix(s*40,s*25,x-s*60,y+s*105,f+gtr(30)))
    polygon(ellipse_matrix(s*10,s*15,x-s*125,y-s*25,f-gtr(15)))
    polygon(ellipse_matrix(s*15,s*15,x-s*80,y-s*25,f))
    polygon(ellipse_matrix(s*15,s*10,x-s*115,y+s*25,f))    
    
def palma(s,x,y):
    brushColor("green")
    penColor("green")
    rectangle(x,y,x+s*25,y-s*75)
    rectangle(x,y-s*85,x+s*25,y-s*190)
    polygon([(x,y-s*200),(x+s*13,y-s*195),(x+s*40,y-s*235),(x+s*27,y-s*240)])
    polygon([(x+s*27,y-s*250),(x+s*35,y-s*245),(x+s*75,y-s*310),(x+s*67,y-s*315)])
    polyline(duga(s*200,s*100,x+s*130,y-s*160,gtr(240)))
    polyline(duga(s*150,s*100,x+s*110,y-s*100,gtr(240)))
    polyline(duga(s*100,s*200,x-s*50,y-s*160,gtr(240)))
    polyline(duga(s*100,s*150,x-s*50,y-s*100,gtr(240)))    

width, height = windowSize()


brushColor("black")
rectangle(0,0,width,height)

brushColor(255,175,128)
rectangle(0,75,width,height-75)

panda(0.75,400,400,0)
palma(1,250,450)
palma(0.6,150,450)

run()

    
