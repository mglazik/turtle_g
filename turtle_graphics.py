#!/bin/python
# -*- coding: utf-8 -*-


# dlaczego nie rysuje?

import turtle

screen = turtle.Screen()
screen.setup(600, 600)


colors = ['red', 'purple', 'green', 'orange', "blue", 'yellow', ]
t = turtle.Pen()

turtle.bgcolor("black")

for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x/100 + 1)
        t.forward(x*2+150+x/50)
        t.left(590)
        t.speed("fastest")