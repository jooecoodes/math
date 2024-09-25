# import math

# x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points separated by commas like x1, y1, x2, y2, x3, y3: ").replace(" ", ""))

# # calculating the length of sides
# a = math.sqrt((x2-x3)*(x2-x3) + (y2-y3)*(y2-y3))
# b = math.sqrt((x1-x3)*(x1-x3) + (y1-y3)*(y1-y3))
# c = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

# # there is a more common formula that is found in most textbooks than this one
# A = math.degrees(math.acos((a*a-b*b-c*c)/(-2*b*c)))
# B = math.degrees(math.acos((b*b-a*a-c*c)/(-2*a*c)))
# C = math.degrees(math.acos((c*c-b*b-a*a)/(-2*a*b)))

# print("The three angles are ", round(A * 100)/100.0, round(B * 100)/100.0, round(C * 100)/100.0)

import math

# Input for coordinates
x1, y1, x2, y2, x3, y3 = eval(input("Enter six coordinates of three points separated by commas like x1, y1, x2, y2, x3, y3: ").replace(" ", ""))

# Calculating the lengths of the sides of the triangle
a = math.sqrt((x2 - x3)**2 + (y2 - y3)**2)  # Length of side opposite to angle A
b = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)  # Length of side opposite to angle B
c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)  # Length of side opposite to angle C

# Calculating the angles using the Law of Cosines
A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))  # Angle at vertex A
B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))  # Angle at vertex B
C = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))  # Angle at vertex C

# Display the angles rounded to two decimal places
print(f"The three angles are: A = {round(A, 2)}°, B = {round(B, 2)}°, C = {round(C, 2)}°")
