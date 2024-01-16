import math

def calculate_circle_area(r):
    return math.pi * pow(r, 2)

def calculate_triangle_area(b, h):
    return (b * h) / 2

def calculate_equilateral_triangle_area(s):
    return pow(s, 2) * math.sqrt(3) / 4

def calculate_square_area(s):
    return s * s

def calculate_rectangle_area(b, h):
    return b * h

def calculate_rhombus_area(D, d):
    return (D * d) / 2

def calculate_trapezoid_area(B, b, h):
    return (B + b) * h / 2

def calculate_penthagon_area(s):
    return 5 * pow(s, 2) / (4 * math.tan(math.pi / 5))
