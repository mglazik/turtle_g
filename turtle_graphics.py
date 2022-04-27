#!/bin/python
# -*- coding: utf-8 -*-

try:
        l = int(input("Podaj kąt "))

        if l < 0:
                print('W prawo nie skręcamy!')

                
        else:
                import turtle

                screen = turtle.Screen()
                screen.setup(1800, 900)


                colors = ['red', 'purple', 'green', 'orange', "blue", 'yellow', ]
                t = turtle.Pen()

                turtle.bgcolor("black")

                for x in range(360):
                        t.pencolor(colors[x%6])
                        t.width(x/100 + 0.5)
                        t.forward(x)
                        t.left(l)
                        t.speed("fastest")
except ValueError:
        print('Ej, no weź się nie wygłupiaj i podaj liczbę')