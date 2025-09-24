import turtle
from random import randint, choice


def get_random_color():
    """Generate a random color in hex format."""
    return f"#{randint(0, 255):02x}{randint(0, 255):02x}{randint(0, 255):02x}"


def create_lights(number=100, angle=20, forward=100):
    screen = turtle.Screen()
    screen.bgcolor('black')  # Set background color to black
    screen.screensize(-300, 300)

    lights = turtle.Turtle()
    lights.speed(0)  # Fastest speed
    lights.hideturtle()  # Hide the turtle cursor for a clean look

    for _ in range(number):  # Loop to draw 'number' lights
        x, y = randint(-300, 300), randint(-300, 300)  # Random position
        lights.penup()
        lights.goto(x, y)  # Move to random position
        lights.pendown()

        # Random color and drawing
        lights.pensize(4)
        lights.pencolor(get_random_color())
        lights.setheading(randint(0, 360))  # Random direction
        lights.forward(forward)  # Draw a line of random length

        # Optionally, draw a circle for each light
        lights.dot(randint(10, 30), get_random_color())  # Draw a dot as a light

    turtle.done()


if __name__ == '__main__':
    create_lights()
