import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
smiley = turtle.Turtle()

# Draw the face
smiley.penup()
smiley.goto(0, -100)  # Center the face on the screen
smiley.pendown()
smiley.circle(100)

# Draw the eyes
smiley.penup()
smiley.goto(-40, 50)  # Position for the left eye
smiley.pendown()
smiley.dot(25)
smiley.penup()
smiley.goto(40, 50)  # Position for the right eye
smiley.pendown()
smiley.dot(25)

# Draw the mouth
smiley.penup()
smiley.goto(57, 10)  # Position for the mouth
smiley.pendown()
smiley.right(90)
for i in range(60):
    smiley.forward(3.4)
    smiley.right(3)

smiley.penup()
smiley.goto(0, -100)  # Center the face on the screen
smiley.pendown()
smiley.forward(10)


# Hide the turtle
smiley.hideturtle()

# Keep the window open
turtle.done()