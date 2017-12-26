#!/bin/python

import turtle as t
from sys import argv
from math import sqrt
from time import sleep

def koch_curve(size, order):
    if order == 0:
        t.forward(size)
    else:
        for rot in [60,-120,60,0]:
            koch_curve(size/3, order-1)
            t.left(rot)
         
def koch_snowflake(size, order):
    #t.speed(0)
    t.tracer(0, 0)
    
    t.penup()
    t.setpos(-size/2,(sqrt(3)/6)*size)
    t.pendown()
    
    koch_curve(size, order)
    t.rt(120)
    koch_curve(size, order)
    t.rt(120)
    koch_curve(size, order)
    
    t.update()

def koch_snowflake_iterator(size=500, order_start=0, order_end=6):
    for i in range(order_start, order_end+1): 
        koch_snowflake(size, i)
        sleep(1)
        t.reset()

def main():
    size = int(argv[1])
    order_start = int(argv[2])
    order_end = int(argv[3])
    
    koch_snowflake_iterator(size, order_start, order_end)
    t.done()

if  __name__ == '__main__':
    main()
