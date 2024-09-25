import turtle

# Set up the screen, scaling each unit by 100
scale = 100
screen = turtle.Screen()
screen.setworldcoordinates(-10 * scale, -10 * scale, 10 * scale, 10 * scale)

# Create a turtle object for drawing
graph = turtle.Turtle()
graph.speed(0)

# Draw x and y axes
def draw_axes():
    graph.penup()
    graph.goto(-10 * scale, 0)
    graph.pendown()
    graph.goto(10 * scale, 0)  # x-axis
    graph.penup()
    graph.goto(0, -10 * scale)
    graph.pendown()
    graph.goto(0, 10 * scale)  # y-axis

# Function to plot a point
def plot_point(x, y, color="red"):
    graph.penup()
    graph.goto(x * scale, y * scale)
    graph.dot(5, color)

# Function to calculate y for a given x using the equation x + 2y = 8
def calculate_y(x):
    return (8 - x) / 2

# Loop through values of x and plot corresponding y
def plot_line_dots(start_x, end_x, step=0.5):
    x = start_x
    while x <= end_x:
        y = calculate_y(x)
        plot_point(x, y)
        x += step

# Draw line through points and scale
def draw_line(start_x, end_x):
    graph.penup()
    graph.goto(start_x * scale, calculate_y(start_x) * scale)
    graph.pendown()
    graph.goto(end_x * scale, calculate_y(end_x) * scale)

# Call the functions to draw the graph
draw_axes()
plot_line_dots(-10, 10)  # Dots from x = -10 to 10
draw_line(-10, 10)       # Connect the dots with a line

# Keep the window open until clicked
screen.exitonclick()
