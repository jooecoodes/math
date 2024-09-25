# seconds =  int(input("Input seconds"))

# # for every minute there are 60 seconds, and for every hours there are 60 minutes which is ( 60 * 60 seconds)

# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# remainingSeconds = seconds % 60

# print(f"{seconds} is {hours} hour/s, {minutes} minute/s, and {remainingSeconds} second/s")

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(40, steps=4)
turtle.end_fill()

turtle.penup()
turtle.goto(0,0)