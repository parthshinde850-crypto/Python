import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("BMW Logo")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(3)

# Function to draw filled quarter
def draw_quarter(color, start_angle):
    t.penup()
    t.goto(0, 0)
    t.setheading(start_angle)
    t.forward(120)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    t.circle(120, 90)
    t.goto(0, 0)

    t.end_fill()


# Outer white ring
t.color("white")
t.penup()
t.goto(0, -150)
t.setheading(0)
t.pendown()
t.circle(150)

# Inner white ring
t.penup()
t.goto(0, -120)
t.pendown()
t.circle(120)

# Blue quadrants
draw_quarter("#0066B1", 0)
draw_quarter("#0066B1", 180)

# White cross lines
t.pensize(5)

t.penup()
t.goto(-120, 0)
t.pendown()
t.goto(120, 0)

t.penup()
t.goto(0, 120)
t.pendown()
t.goto(0, -120)

# BMW text
t.penup()
t.goto(-55, 175)
t.color("white")
t.write("BMW", font=("Arial", 28, "bold"))

turtle.done()