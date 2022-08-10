from turtle import *
L=0
R=1

def bunka(lr):
    pendown()
    for s in range(6):
        forward(60)
        if lr==L:
            left(60)
        else:
            right(60)
    penup()        

bunka(L)

if 0==1:  # kreslí kolem první bunky, jinak stred nekreslí
    left(120)
    bunka(L)
    left(120)
    bunka(L)

for i in range(5):
    left(120)
    forward(60)
    right(60)
    bunka(L)

exitonclick()