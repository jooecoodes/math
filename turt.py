# # import turtle
# # import math

# # # Set up turtle screen
# # screen = turtle.Screen()
# # screen.bgcolor("black")

# # # Create a turtle object
# # t = turtle.Turtle()
# # t.speed(10)  # Fastest speed
# # t.width(2)
# # t.hideturtle()

# # # Colors for the pattern
# # colors = ["red", "blue", "green", "yellow", "purple", "cyan", "white"]

# # # Function to draw Lissajous curves
# # def draw_lissajous(A, B, a, b, delta, steps=1000, scale=200):
# #     t.penup()  # Lift the pen
# #     for i in range(steps):
# #         t_value = i * (2 * math.pi) / steps
# #         x = A * math.sin(a * t_value + delta)
# #         y = B * math.sin(b * t_value)
# #         t.goto(scale * x, scale * y)
# #         t.pendown()

# # # Draw multiple Lissajous curves with different parameters for variety
# # for i in range(7):
# #     t.pencolor(colors[i % len(colors)])
# #     A = 1 + i * 0.2
# #     B = 1 + i * 0.1
# #     a = 3 + i
# #     b = 2 + i
# #     delta = math.pi / 2  # Phase shift
# #     draw_lissajous(A, B, a, b, delta, steps=1000, scale=200)
# #     t.right(45)  # Rotate slightly for a layered effect

# # # Close the window on click
# # screen.mainloop()
# import turtle
# import math

# # Set up the turtle
# t = turtle.Turtle()
# turtle.bgcolor("black")
# t.speed(0)  # Fastest drawing speed
# t.color("cyan")

# # Geometric pattern parameters
# num_circles = 36  # Number of circles to draw
# radius = 150  # Radius of each circle
# num_lines = 18  # Number of lines in each circle

# # Function to draw a circle with lines inside it
# def draw_circle_with_lines(radius, num_lines):
#     angle_gap = 360 / num_lines
#     for i in range(num_lines):
#         t.forward(radius)
#         t.backward(radius)
#         t.left(angle_gap)

# # Draw the pattern
# for i in range(num_circles):
#     draw_circle_with_lines(radius, num_lines)
#     t.left(360 / num_circles)  # Rotate to start next circle

# # Finish the drawing
# turtle.done()
import turtle

# Set up turtle
t = turtle.Turtle()
t.speed(0)  # Fastest speed for drawing
turtle.bgcolor("black")
t.color("magenta")
t.hideturtle()


# Parameters for the spiral
num_squares = 50  # Number of squares
side_length = 600  # Initial side length of the square
angle = 10  # Rotation angle for each step
scale = 0.9  # Scaling factor for each square

# Function to draw a square
def draw_square(length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

# Draw spiral pattern
for i in range(num_squares):
    draw_square(side_length)
    t.left(angle)  # Rotate the square
    side_length *= scale  # Scale down the square size

