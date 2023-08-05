import turtle

screen = turtle.Screen()
screen.setup(400, 500)
t = turtle.Turtle()
t.hideturtle()

# Coordinates triangle
coord_triangles = [
    {
        "x": [0, -100, -100, 0],
        "y": [0, -100, 100, 0]
    },
    {
        "x": [0, 100, 100, 0],
        "y": [0, -100, 100, 0]
    }
]

def drawing_triangle(direction):
    coordinates = coord_triangles[direction]
    x_coords = coordinates["x"]
    y_coords = coordinates["y"]
    for x, y in zip(x_coords, y_coords):
        t.goto(x, y)
        t.dot(20)

def broken_line(x1, y1, x2, y2, segment_length=25, gap_length=25):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    dx = x2 - x1
    dy = y2 - y1
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5
    segment_count = distance // (segment_length + gap_length)
    segment_length_x = dx / segment_count
    segment_length_y = dy / segment_count
    for i in range(int(segment_count)):
        t.forward(segment_length)
        t.penup()
        t.forward(gap_length)
        t.pendown()

for direction in range(len(coord_triangles)):
    drawing_triangle(direction)

broken_line(-100, 100, 100, 100)
broken_line(-100, -100, 100, -100)

turtle.done()
