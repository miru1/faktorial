from turtle import *
for i in range(0,6):
    forward(50)
    left(60)

shape('turtle')
penup()
forward(300)
pendown()

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 10:
        break
end_fill()
done()

for j in range(0,int(360/5)):
    for i in range(0,4):
        forward(60)
        left(90)
    left(5)


exitonclick