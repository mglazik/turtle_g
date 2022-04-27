#!/bin/python
# -*- coding: utf-8 -*-

import sys


try:
        l = float(input("Podaj kąt: "))
        s = float(input('Podaj skok: '))
        m = float(input('Podaj mnożnik: '))

except ValueError:
        print('Ej, no weź się nie wygłupiaj i podaj liczbę')
        sys.exit()


import turtle

screen = turtle.Screen()
screen.setup(1800, 900)


colors = ["brown", "brown1", "brown2", "brown3", "brown4", "indianred4",]
t = turtle.Pen()

turtle.bgcolor("black")

for x in range(1360):
        t.pencolor(colors[x%6])
        t.width(x/1000 + 0.5)
        t.forward(x*m+s)
        t.left(l)
        t.speed("fastest")

