#!/bin/python
# -*- coding: utf-8 -*-

import sys

try:
        l = float(input("Podaj kąt "))

except ValueError:
        print('Ej, no weź się nie wygłupiaj i podaj liczbę')
        sys.exit()

if l < 0:
        print('W prawo nie skręcamy!')
        sys.exit()
        
else:
        import turtle

        screen = turtle.Screen()
        screen.setup(1800, 900)


        colors = ['red', 'purple', 'green', 'orange', "blue", 'yellow', ]
        t = turtle.Pen()

        turtle.bgcolor("black")

        for x in range(1360):
                t.pencolor(colors[x%6])
                t.width(x/100 + 0.5)
                t.forward(x*2+1)
                t.left(l)
                t.speed("fastest")

