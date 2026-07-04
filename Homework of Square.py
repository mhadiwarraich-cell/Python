import turtle

# Create a turtle
pen = turtle.Turtle()

# Draw a square
for i in range(4):
    pen.forward(100)
    pen.right(90)

# Keep the window open
turtle.done()