import turtle
import random


# reads in input and checks for numeric input
def numeric_input(num_str):
    input_string = input('input ' + num_str + ': ')
    while not input_string.isnumeric():
        print(num_str + ' must be an integer')
        input_string = input('input ' + num_str + ': ')
    return int(input_string)


# generates random rgb color
def generate_color():
    random.seed()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# draw a pattern with specified angle and iteration number
def draw_specific_pattern(angle, iterations):
    turtle.title('Patterns')
    turtle.setup(1280, 1200)
    turtle.hideturtle()
    turtle.bgcolor('black')
    turtle.colormode(255)
    turtle.speed(40)

    print('drawing pattern...')
    for i in range(0, iterations):
        turtle.color(generate_color())
        turtle.forward(2 * i)
        turtle.right(angle)

    print('pattern drawn')
    turtle.done()


# draw a pattern with a random angle
def draw_random_pattern():
    ang = random.randint(0, 360)
    draw_specific_pattern(ang, 400)


angle_ = numeric_input('angle')
iterations_ = numeric_input('iterations')
draw_specific_pattern(angle_, iterations_)

# draw_random_pattern()
