import turtle as t
color1 = "midnightblue"
color2 = "silver"

#t.speed(0)
#t.hideturtle()
t.color(color1)
#upper parellelogram
t.penup()
t.left(90)
t.forward(210)
t.pendown()
t.begin_fill()
t.right(90)
t.forward(150)
t.right(110) #angle right
t.forward(40)
t.right(70)
t.forward(240)
t.right(110)
t.forward(40)
t.right(70)
t.forward(130)
t.end_fill()

#start bottom
t.penup()
t.right(90)
t.forward(20)
t.pendown()
t.begin_fill()
t.forward(230)
t.right(90)
t.forward(40)
t.right(90)
t.forward(230)
t.end_fill()
#starting S
t.color(color2)
t.penup()
t.backward(60)
t.right(90)
#part1
t.forward(41)
t.pendown()
t.begin_fill()
t.forward(70)
t.right(110)#angle right
t.forward(30)
t.right(70)
t.forward(60)
t.right(90)
t.forward(27)
t.end_fill()
#part 2
t.penup()
t.left(90)
t.forward(42)
t.pendown()
t.begin_fill()
t.forward(28)
t.circle(40,110)#curve 1
t.circle(30,60)
t.circle(15,30)
t.left(-20)
t.forward(35)
t.left(90)
t.forward(25)
#insider curve 1
t.left(90)
t.forward(20)
t.circle(-11,172)
t.forward(1)
t.circle(-90,13)
t.left(94)
t.forward(26)
t.end_fill()



#part 2
t.penup()
t.backward(47)
t.right(89)
t.pendown()
t.begin_fill()
t.forward(60)
t.circle(-46,180)
t.forward(130)#/ /

t.right(120)
t.forward(30)
t.right(60)
t.forward(110)

t.circle(20,170)
t.left(10)
t.forward(60)
t.end_fill()
t.penup()
#eye

t.color(color1)
t.right(90)
t.forward(50)
t.right(90)
t.forward(95)
t.left(90)
t.forward(10)
t.pendown()
t.begin_fill()
t.circle(5,360)
t.end_fill()
t.hideturtle()
t.exitonclick()


"""
___START  MOTHERBOARD
t.penup()
t.color(color2)
t.forward(40)
t.left(95)
t.forward(50)


t.forward(15)
t.pendown()
t.begin_fill()
t.right(5)
t.forward(15)
t.left(90)
t.forward(30)
t.left(90)
t.forward(15)
t.left(90)
t.forward(30)
t.end_fill()
t.left(90)
t.forward(3)
t.right(90)
t.pensize(2)
t.forward(20)
t.right(50)
t.forward(15)
t.left(50)
t.forward(20)
t.right(10)
t.circle(2,360)
----- END




userAnswer = input("Question: ")
if userAnswer == "Tech Squad":
    t.speed(0)
    t.hideturtle()
    t.color(color1)
    #upper parellelogram
    t.penup()
    t.left(90)
    t.forward(210)
    t.pendown()
    t.begin_fill()
    t.right(90)
    t.forward(150)
    t.right(110) #angle right
    t.forward(40)
    t.right(70)
    t.forward(240)
    t.right(110)
    t.forward(40)
    t.right(70)
    t.forward(130)
    t.end_fill()

    #start bottom
    t.penup()
    t.right(90)
    t.forward(20)
    t.pendown()
    t.begin_fill()
    t.forward(230)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(230)
    t.end_fill()
    #starting S
    t.color(color2)
    t.penup()
    t.backward(60)
    t.right(90)
    #part1
    t.forward(41)
    t.pendown()
    t.begin_fill()
    t.forward(70)
    t.right(110)#angle right
    t.forward(30)
    t.right(70)
    t.forward(60)
    t.right(90)
    t.forward(27)
    t.end_fill()
    #part 2
    t.penup()
    t.left(90)
    t.forward(42)
    t.pendown()
    t.begin_fill()
    t.forward(28)
    t.circle(40,110)#curve 1
    t.circle(30,60)
    t.circle(15,30)
    t.left(-20)
    t.forward(35)
    t.left(90)
    t.forward(25)
    #insider curve 1
    t.left(90)
    t.forward(20)
    t.circle(-11,172)
    t.forward(1)
    t.circle(-90,13)
    t.left(94)
    t.forward(26)
    t.end_fill()
    #part 2
    t.penup()
    t.backward(47)
    t.right(89)
    t.pendown()
    t.begin_fill()
    t.forward(60)
    t.circle(-50,180)
    t.forward(110)

    t.right(120)
    t.forward(30)
    t.right(60)
    t.forward(90)
    t.circle(24,170)
    t.left(10)
    t.forward(60)
    t.end_fill()
    t.penup()
    #eye
    t.color(color1)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(95)
    t.left(90)
    t.forward(10)
    t.pendown()
    t.begin_fill()
    t.circle(5,360)
    t.end_fill()
    t.exitonclick()
else:
    print("Incorrect")
"""