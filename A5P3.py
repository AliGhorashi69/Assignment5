import turtle
turtle.title("Ali Ghorashi")

#Start----------------------------------------------
tu = turtle.Pen()
tu.speed(5)
tu.shape("turtle")
turtle.bgcolor('white')
i=0
j= 0
s=0
while i < 10:
    s=106+s
    tu.left(180-((((i+3-2)*180)/(i+3))/2))
    
    while j <= i+2:
        tu.width(1.5)
        tu.pencolor('blue')
        
        tu.forward(s/(i+3))
        tu.left(180-(((i+3-2)*180)/(i+3)))
        j= 1+j
    tu.penup()
    tu.right(180-(((i+3-2)*180)/(i+3)))
    tu.right((((i+3-2)*180)/(i+3))/2)
    tu.forward(15)
    tu.pendown()
    j=0
    i=1+i