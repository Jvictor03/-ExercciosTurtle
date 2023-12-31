"""
Exercicios

1) Acrescente cores
2) Mude a largura da linha
3) Aumente a quantidade de linhas
"""

import turtle
import random

turtle = turtle.Turtle()
turtle.pensize(3)

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'gray', 'red', 'violet']
for _ in range (15):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(30)