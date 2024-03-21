number = int(input('Введите число: '))
if number % 10 == number // 1000 and (number % 100) // 10 == (number // 100) % 10:
    print('настоящее')
else:
    print('кривое')