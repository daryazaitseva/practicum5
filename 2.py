import turtle as t

xc = int(input('Ввведите координату X центра окружности: '))
yc = int(input('Введите координату Y центра окружности: '))
r = int(input('Введите значение радиусы окружности: '))
x = int(input('Введите координату точки по оси X: '))
y = int(input('Введите координату точки по оси Y: '))

t.color('black')
t.penup()
t.penup()
t.goto(xc, yc)
t.forward(r)
t.left(90)
t.pendown()
t.circle(r)

t.penup()
t.color('red')
t.goto(x, y)
t.pendown()
t.dot(5)

t.penup()
t.goto(xc - r - 100, yc - r - 50)
if (abs(xc - x)) ** 2 + (abs(yc - y)) ** 2 == r ** 2:
    t.write('точка на окружности')
elif (abs(xc - x)) ** 2 + (abs(yc - y)) ** 2 <= r ** 2:
    t.write('точка внутри окружности')
elif (abs(xc - x)) ** 2 + (abs(yc - y)) ** 2 >= r ** 2:
    t.write('точка вне окружности')

t.done()
