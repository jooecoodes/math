import turtle
import math

# hello :), this is the combination of all i have learned from module 1 up to 3, this simple program that i made will graph the coordinates, calculate the slope, the y-intercept, the x-intercept, the midpoint, and the distance between 2 coordinates in the cartesian plane
# the cartesian plane is made out of many invisible turtles and each unit is multiplied by 100 from x and y axes

# formula used
# the slope formula, m = (y2 - y1)/(x2 - x1) gets the rate of change for every unit
# the point-slope formula, y - y1 = m(x - x1), where m is the slope to get the function for the graph, y = ((slope * (startX - x1)) + y1) 
# the pythagorean theorem, c^2 = a^2 + b^2 to get the length of a and b where c is the distance, d = math.sqrt((x2-x1)^2 + (y2 - y1)^2)
# the midpoint formula, mid = (x1+x2/2, y1+y2/2) to get the middle coordinate of both coordinates

# deriving the standard form Ax + By + C = 0 using the point-slope formula to get the x and y intercept
# y - y1 = m(x - x1)
# y - y1 = mx - mx1
# y = mx - mx1 + y1
# 0 = mx - y + (y1 - mx1) = Ax + By + C = 0
# A = m, B = -1, C = (y1 - mx1)



# set up (constants)
startX = -10
endX = 10
unit = 50
deg = 90
speed = 0
axisScaler = 8

# slope and intercept

x1, y1, x2, y2 = eval(input("Give 2 coordinates to calculate the slope, x and y intercepts, the distance, and the midpoint of the function, input it this way x1, y1, x2, y2 make sure to separate them with commas (Please limit your coordinates on 7x6 grid): "))

# m slope formula
slope = (y2 - y1)/(x2 - x1)

distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)

midpointX = ((x1+x2)/2)
midpointY = ((y1+y2)/2)

# standard form, mx - y + (y1 - mx1) = 0, where m is the slope

# x = 0
# y = mx + (y1 - mx1)
yIntercept = slope * 0 + (y1 - (slope*x1))
# y = 0
# x = - y/m + (y1 - mx1)/m
xIntercept = x1 - (y1/slope)

print(x1, y1, x2, y2)
print(f'the slope of the coordinates ({x1},{y1}) and ({x2},{y2}) is: {round(slope, 1)}')
print(f"the distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")
print(f"the midpoint of the coordinates ({x1}, {y1}) and ({x2}, {y2}) is: ({midpointX}, {midpointY})")
print(f"the y-intercept of the function is: {round(yIntercept, 1)}")
print(f"the x-intercept of the function is: {round(xIntercept, 1)}")

# set window title
screen = turtle.Screen()
screen.title("Villacorta")

# cartesian plane

# axis

yAxis1 = turtle.Turtle()
yAxis1.pensize(2.5)
yAxis1.speed(speed)
yAxis1.left(90)
yAxis1.forward(axisScaler*unit)

yAxis2 = turtle.Turtle()
yAxis2.pensize(2.5)
yAxis2.speed(speed)
yAxis2.right(90)
yAxis2.forward(axisScaler*unit)

xAxis1 = turtle.Turtle()
xAxis1.pensize(2.5)
xAxis1.speed(speed)
xAxis1.left(180)
xAxis1.forward(axisScaler*unit)

xAxis2 = turtle.Turtle()
xAxis2.pensize(2.5)
xAxis2.speed(speed)
xAxis2.right(0)
xAxis2.forward(axisScaler*unit)




# initiation

# initiation x right
t1xr = turtle.Turtle()
t2xr = turtle.Turtle()
t3xr = turtle.Turtle()
t4xr = turtle.Turtle()
t5xr = turtle.Turtle()
t6xr = turtle.Turtle()
t7xr = turtle.Turtle()
t8xr = turtle.Turtle()


t1xr.hideturtle()
t2xr.hideturtle()
t3xr.hideturtle()
t4xr.hideturtle()
t5xr.hideturtle()
t6xr.hideturtle()
t7xr.hideturtle()
t8xr.hideturtle()

t1xr.speed(speed)
t2xr.speed(speed)
t3xr.speed(speed)
t4xr.speed(speed)
t5xr.speed(speed)
t6xr.speed(speed)
t7xr.speed(speed)
t8xr.speed(speed)

# initiation x left
t1xl = turtle.Turtle()
t2xl = turtle.Turtle()
t3xl = turtle.Turtle()
t4xl = turtle.Turtle()
t5xl = turtle.Turtle()
t6xl = turtle.Turtle()
t7xl = turtle.Turtle()
t8xl = turtle.Turtle()

t1xl.hideturtle()   
t2xl.hideturtle()
t3xl.hideturtle()
t4xl.hideturtle()
t5xl.hideturtle()
t6xl.hideturtle()
t7xl.hideturtle()
t8xl.hideturtle()

t1xl.speed(speed)
t2xl.speed(speed)
t3xl.speed(speed)
t4xl.speed(speed)
t5xl.speed(speed)
t6xl.speed(speed)
t7xl.speed(speed)
t8xl.speed(speed)

# initiation y top
t1yt = turtle.Turtle()
t2yt = turtle.Turtle()
t3yt = turtle.Turtle()
t4yt = turtle.Turtle()
t5yt = turtle.Turtle()
t6yt = turtle.Turtle()
t7yt = turtle.Turtle()
t8yt = turtle.Turtle()



t1yt.hideturtle()
t2yt.hideturtle()
t3yt.hideturtle()
t4yt.hideturtle()
t5yt.hideturtle()
t6yt.hideturtle()
t7yt.hideturtle()
t8yt.hideturtle()   


t1yt.speed(speed)
t2yt.speed(speed)
t3yt.speed(speed)
t4yt.speed(speed)
t5yt.speed(speed)
t6yt.speed(speed)
t7yt.speed(speed)
t8yt.speed(speed)   

# initiation y bottom
t1yb = turtle.Turtle()
t2yb = turtle.Turtle()
t3yb = turtle.Turtle()
t4yb = turtle.Turtle()
t5yb = turtle.Turtle()
t6yb = turtle.Turtle()
t7yb = turtle.Turtle()
t8yb = turtle.Turtle()

t1yb.hideturtle()
t2yb.hideturtle()
t3yb.hideturtle()
t4yb.hideturtle()
t5yb.hideturtle()
t6yb.hideturtle()
t7yb.hideturtle()
t8yb.hideturtle()

t1yb.speed(speed)
t2yb.speed(speed)
t3yb.speed(speed)
t4yb.speed(speed)
t5yb.speed(speed)
t6yb.speed(speed)
t7yb.speed(speed)
t8yb.speed(speed)

# x axis

# x right


t1xr.goto(-1*unit,0)
t2xr.goto(-2*unit,0)
t3xr.goto(-3*unit,0)
t4xr.goto(-4*unit,0)
t5xr.goto(-5*unit,0)
t6xr.goto(-6*unit,0)
t7xr.goto(-7*unit,0)
t8xr.goto(-8*unit,0)

t1xr.left(deg)
t2xr.left(deg)
t3xr.left(deg)
t4xr.left(deg)
t5xr.left(deg)
t6xr.left(deg)
t7xr.left(deg)
t8xr.left(deg)

t1xr.forward(axisScaler*unit)
t2xr.forward(axisScaler*unit)
t3xr.forward(axisScaler*unit)
t4xr.forward(axisScaler*unit)
t5xr.forward(axisScaler*unit)
t6xr.forward(axisScaler*unit)
t7xr.forward(axisScaler*unit)
t8xr.forward(axisScaler*unit)

t1xr.backward(2*axisScaler*unit)
t2xr.backward(2*axisScaler*unit)
t3xr.backward(2*axisScaler*unit)
t4xr.backward(2*axisScaler*unit)
t5xr.backward(2*axisScaler*unit)
t6xr.backward(2*axisScaler*unit)
t7xr.backward(2*axisScaler*unit)
t8xr.backward(2*axisScaler*unit)


# x left

t1xl.goto(1*unit,0)
t2xl.goto(2*unit,0)
t3xl.goto(3*unit,0)
t4xl.goto(4*unit,0)
t5xl.goto(5*unit,0)
t6xl.goto(6*unit,0)
t7xl.goto(7*unit,0)
t8xl.goto(8*unit,0)

t1xl.left(deg)
t2xl.left(deg)
t3xl.left(deg)
t4xl.left(deg)
t5xl.left(deg)
t6xl.left(deg)
t7xl.left(deg)
t8xl.left(deg)

t1xl.forward(axisScaler*unit)
t2xl.forward(axisScaler*unit)
t3xl.forward(axisScaler*unit)
t4xl.forward(axisScaler*unit)
t5xl.forward(axisScaler*unit)
t6xl.forward(axisScaler*unit)
t7xl.forward(axisScaler*unit)
t8xl.forward(axisScaler*unit)

t1xl.backward(2*axisScaler*unit)
t2xl.backward(2*axisScaler*unit)
t3xl.backward(2*axisScaler*unit)
t4xl.backward(2*axisScaler*unit)
t5xl.backward(2*axisScaler*unit)
t6xl.backward(2*axisScaler*unit)
t7xl.backward(2*axisScaler*unit)
t8xl.backward(2*axisScaler*unit)

# y axis

# y top

t1yt.goto(0,1*unit)
t2yt.goto(0,2*unit)
t3yt.goto(0,3*unit)
t4yt.goto(0,4*unit)
t5yt.goto(0,5*unit)
t6yt.goto(0,6*unit)
t7yt.goto(0,7*unit)
t8yt.goto(0,8*unit)

t1yt.forward(axisScaler*unit)
t2yt.forward(axisScaler*unit)
t3yt.forward(axisScaler*unit)
t4yt.forward(axisScaler*unit)
t5yt.forward(axisScaler*unit)
t6yt.forward(axisScaler*unit)
t7yt.forward(axisScaler*unit)
t8yt.forward(axisScaler*unit)

t1yt.backward(2*axisScaler*unit)
t2yt.backward(2*axisScaler*unit)
t3yt.backward(2*axisScaler*unit)
t4yt.backward(2*axisScaler*unit)
t5yt.backward(2*axisScaler*unit)
t6yt.backward(2*axisScaler*unit)
t7yt.backward(2*axisScaler*unit)
t8yt.backward(2*axisScaler*unit)

# y bottom

t1yb.goto(0,-1*unit)
t2yb.goto(0,-2*unit)
t3yb.goto(0,-3*unit)
t4yb.goto(0,-4*unit)
t5yb.goto(0,-5*unit)
t6yb.goto(0,-6*unit)
t7yb.goto(0,-7*unit)
t8yb.goto(0,-8*unit)

t1yb.forward(axisScaler*unit)
t2yb.forward(axisScaler*unit)
t3yb.forward(axisScaler*unit)
t4yb.forward(axisScaler*unit)
t5yb.forward(axisScaler*unit)
t6yb.forward(axisScaler*unit)
t7yb.forward(axisScaler*unit)
t8yb.forward(axisScaler*unit)


t1yb.backward(2*axisScaler*unit)
t2yb.backward(2*axisScaler*unit)
t3yb.backward(2*axisScaler*unit)
t4yb.backward(2*axisScaler*unit)
t5yb.backward(2*axisScaler*unit)
t6yb.backward(2*axisScaler*unit)
t7yb.backward(2*axisScaler*unit)
t8yb.backward(2*axisScaler*unit)

# graphing and plotting

graph = turtle.Turtle()
coord1 = turtle.Turtle()
coord2 = turtle.Turtle()
slopeDraw = turtle.Turtle()
midpointDraw = turtle.Turtle()
xInterceptDraw = turtle.Turtle()
yInterceptDraw = turtle.Turtle()

coord1.hideturtle()
coord2.hideturtle()
slopeDraw.hideturtle()
midpointDraw.hideturtle()
xInterceptDraw.hideturtle()
yInterceptDraw.hideturtle()

graph.penup()
graph.pensize(2)
graph.color('blue')
graph.goto(startX * unit, ((slope * (startX - x1)) + y1) * unit)
graph.pendown()
graph.goto(endX * unit, ((slope * (endX - x1)) + y1) * unit)

coord1.penup()
coord1.goto(x1*unit, y1*unit)
coord1.dot(8, 'red')
coord2.penup()
coord1.write(f"({x1},{y1})")
coord2.goto(x2*unit, y2*unit)
coord2.dot(8, 'red')
coord2.write(f"({x2},{y2})")

# slope draw
slopeDraw.penup()
slopeDraw.goto(x1*unit, y1*unit)
slopeDraw.pensize(2)
slopeDraw.color('red')
slopeDraw.pendown()
slopeDraw.right(0)
slopeDraw.forward((x2 - x1) * unit)
slopeDraw.write(f"m = {round(slope, 1)}", align='center')
slopeDraw.left(90)
slopeDraw.forward((y2 - y1) * unit/2)
slopeDraw.write(f"d = {round(distance, 1)} ", align='right') 

slopeDraw.forward((y2 - y1) * unit/2)
# draw distance

# midpoint draw
midpointDraw.penup()
midpointDraw.goto(midpointX*unit, midpointY*unit)
midpointDraw.dot(8, 'dark green')
midpointDraw.write(f" mp = ({midpointX}, {midpointY})",align='right')

# intercepts 
# y = 0
xInterceptDraw.penup()
xInterceptDraw.goto(xIntercept*unit, 0)
xInterceptDraw.dot(8, 'yellow')
xInterceptDraw.write(f"({round(xIntercept)}, 0)")

# x = 0
yInterceptDraw.penup()
yInterceptDraw.goto(0, yIntercept*unit)
yInterceptDraw.dot(8, 'yellow')
yInterceptDraw.write(f"(0, {round(yIntercept, 1)})")

turtle.done()