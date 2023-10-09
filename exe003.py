"""
Exercícios

1) Mude/defina a forma da tartaruga
2) Mude a ordem das cores
3) Mude a largura da linha
4) Faça a tartaruga desenhar dois quadrados
"""

import turtle

turtle = turtle.Turtle()
turtle.pensize(2)

for _ in range(2):

    for color in ['purple', 'green', 'blue', 'orange']:
     turtle.color(color)
     turtle.forward(50)
     turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()