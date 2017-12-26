#!/bin/python 

from turtle import *
from sys import argv

#----------------- TOOLKIT ----------------#

def spiral(width=1,steps=20):
    for i in range(steps):
        fd(i*width)
        rt(90)
        fd(i*width)

def cube(width=10):
    #FRONT
    seth(270)
    for rot in [90,90,90,0]:
        fd(width)
        rt(rot)

    #RIGHT
    seth(45)
    for widthScale,rot in [(1.5,135),(1,45),(1.5,135),(1,0)]: 
        fd(width/widthScale)
        rt(rot)

    #TOP
    seth(180)
    for widthScale,rot in [(1,135),(1.5,45),(1,135),(1.5,0)]: 
        fd(width/widthScale)
        rt(rot)

    seth(0)

def cubeSpiral(width=25,steps=3):
    turnAngle = 0
    for i in range(steps):
        for j in range(i+1):
            cube(width) 
            rt(turnAngle)
            fd(width)
        turnAngle = (turnAngle + 90) % 360

#------------------ SETUP ------------------#
try:
    a1 = int(argv[1])
    a2 = int(argv[2])
except:
    pass

speed(0)

#------------------ MAIN -------------------#
cubeSpiral(a1,a2)

#------------------ END --------------------#
done()
