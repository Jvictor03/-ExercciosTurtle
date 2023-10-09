"""
Exercícios

1) Faça cada quadrado ter uma cor
2) Faça cada quadrado com um formato diferente da tartaruga
3) Faça os quadrados não se tocarem
4) Desenhe um quadrado maior ao redor dos demais quadrados
"""

import turtle

turtle = turtle.Turtle()

for _ in range(4):
    turtle.color('yellow')
    turtle.forward(100)
    turtle.right(90)

turtle.up()
turtle.bk(20)
turtle.left(90)
turtle.down()

for _ in range(4):
   turtle.color('blue')
   turtle.left(90)
   turtle.forward(100)

turtle.up()
turtle.fd(20)
turtle.left(90)
turtle.bk(20)
turtle.down()

for _ in range(4):
   turtle.color('grey')
   turtle.bk(100)
   turtle.left(90)

turtle.up()
turtle.fd(20)
turtle.left(90)
turtle.down()

for _ in range(4):
   turtle.color('orange')
   turtle.right(90)
   turtle.forward(100)

turtle.up()
turtle.bk(100)
turtle.right(90)
turtle.fd(120)
turtle.right(90)
turtle.fd(20)
turtle.left(180)
turtle.down()

turtle.color('green')
turtle.shape('arrow')

for _ in range(4):
    turtle.forward(260)
    turtle.left(90)
