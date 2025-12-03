import turtle

# --- Setup Turtle ---
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)      # 0 = kecepatan maksimum (turbo)


# =============================
#         FUNCTION LABEL
# =============================
def write_label(x, y, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.write(text, align="center", font=("Arial", 14, "bold"))


# =============================
#       ALGORITMA DDA
# =============================
def draw_line_dda(x1, y1, x2, y2, color="black"):
    t.color(color)
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1

    for _ in range(steps):
        t.penup()
        t.goto(round(x), round(y))
        t.pendown()
        t.dot(4)
        x += x_inc
        y += y_inc


# =============================
#     ALGORITMA BRESENHAM
# =============================
def draw_line_bresenham(x1, y1, x2, y2, color="blue"):
    t.color(color)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x, y = x1, y1
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        err = dx / 2
        while x != x2:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(4)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2
        while y != y2:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.dot(4)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy


# =============================
#   ALGORITMA MIDPOINT CIRCLE
# =============================
def draw_circle_midpoint(x_center, y_center, radius, color="red"):
    t.color(color)
    x = 0
    y = radius
    p = 1 - radius

    def plot(px, py):
        t.penup()
        t.goto(px, py)
        t.pendown()
        t.dot(4)

    while x <= y:
        pts = [
            (x_center + x, y_center + y),
            (x_center - x, y_center + y),
            (x_center + x, y_center - y),
            (x_center - x, y_center - y),
            (x_center + y, y_center + x),
            (x_center - y, y_center + x),
            (x_center + y, y_center - x),
            (x_center - y, y_center - x),
        ]

        for px, py in pts:
            plot(px, py)

        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1


# =============================
#          POLIGON
# =============================
def draw_polygon(points, color="green"):
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]
        draw_line_dda(x1, y1, x2, y2, color)


# =============================
#       OUTPUT DIPISAH
# =============================

# Label
write_label(-250, 200, "GARIS")
write_label(0, 200, "LINGKARAN")
write_label(250, 200, "POLIGON")

# Garis DDA dan Bresenham (kiri)
draw_line_dda(-350, 150, -150, 150, "black")
draw_line_bresenham(-350, 100, -150, 10, "blue")

# Lingkaran (tengah)
draw_circle_midpoint(0, 40, 80, "red")

# Poligon (kanan)
hexagon = [
    (200, 150),
    (270, 100),
    (270, 0),
    (200, -50),
    (130, 0),
    (130, 100)
]
draw_polygon(hexagon, "green")

turtle.done()
