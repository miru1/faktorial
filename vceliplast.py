# import s * by se neměl používat
from turtle import *

def bunka(stred, lr):
    penup()
    forward(stred)
    pendown()
    for s in range(6):
        forward(60)
        if lr=='L':
            left(60)
        else:
            right(60)

bunka(-120,'L')
bunka(0,'R')

penup()
forward(60)
left(60)
forward(60)
right(60)
pendown()
bunka(0,'L')
bunka(0,'R')

penup()
left(240)
forward(60)
left(60)
forward(60)
right(300)
pendown()
bunka(0,'R')

penup()
forward(60)
right(60)
forward(60)
left(60)
bunka(0,'L')

penup()
left(120)
forward(60)
right(60)
forward(60)
left(60)
bunka(0,'R')


exitonclick()