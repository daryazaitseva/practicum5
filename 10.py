pin = str(input(f'Введите PIN-код, который:\n1. Цифр должно быть ровно 4\n'
                f'2. Не содержит повторяющихся цифр\n'
                f'3. Не может быть годом рождения\n'
                f'Ваш PIN-код: '))
if (len(pin) == 4 and
        (pin[0] != pin[1] and pin[0] != pin[2] and pin[0] != pin[3]
         and pin[1] != pin[2] and pin[1] != pin[3] and pin[2] != pin[3])
        and (not (1900 <= int(pin) <= 2050))):
    print('OK')
else:
    print('ERROR')
