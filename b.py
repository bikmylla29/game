# class Rectangle:
#     def __init__(self, width, height):
#         self.n1 = width
#         self.n2 = height
#
#     def get_area(self):
#         return self.n1 * self.n2
#
# o = Rectangle(6, 10)
# l = o.get_area()
# print(l)

import turtle as t
# screen = t.Screen()
# screen.setup(800, 600)
#
# car = t.Turtle()
# car.shape('square')
# car.color('red')
#
# def move(speed, direction):
#     car.setposition(direction)
#     car.forward(speed)
#
# s = int(input('введите скорость движения: '))
# d = int(input('введите направление от 0 до 360 градусов: '))
#
# move(s, d)
# t.mainloop()
t.bgcolor('dark gray')
t.color('dark blue')
def move_forward(speed):
    t.forward(speed)
def move_backward(speed):
    t.backward(speed)
def turn_left(direction):
    t.left(direction)
def turn_right(direction):
    t.right(direction)

s = int(input('введите скорость движения: '))
d = int(input('введите направление от 0 до 360 градусов: '))

car = t.Turtle()

car.penup()
car.goto(0,0)
car.pendown()

t.onkey(move_forward, 'u')
t.onkey(move_backward, 'd')
t.onkey(turn_left, 'l')
t.onkey(turn_right, 'r')

t.listen()
t.mainloop()