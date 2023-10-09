"""
Exercícios

1) Aumente o tamanho do envelope
2) Use formas diferentes da tartaruga enquanto faz a aba e enquanto faz o corpo
3) Deixe o envelope colorido
4) Reduza o aba do envelope
"""

import turtle
import random

turtle = turtle.Turtle()
colors = ['red', 'blue', 'purple', 'pink', 'green', 'orange']


for _ in [1, 2, 3]:
    turtle.color(random.choice(colors))
    turtle.forward(140)
    turtle.right(120)

for _ in [1, 2, 3, 4]:
    turtle.color(random.choice(colors))
    turtle.forward(170)
    turtle.right(90)