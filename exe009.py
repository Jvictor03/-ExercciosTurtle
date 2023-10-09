"""
Exercicios:

1) Faça cada passo da tartaruga ter uma cor diferente
2) Aumente/diminua o diâmetro do círculo
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(3)

colors = ['blue', 'violet', 'yellow', 'green', 'pink', 'orange', 'grey', 'purple']
for c in range(360):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(2)
    turtle.right(1)