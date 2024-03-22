count = int(input('Введите число: '))
if count % 10 == 1 and count != 11:
    print(f'{count} попугай')
elif ((count % 10 == 2 or count % 10 == 3 or count % 10 == 4)
      and (count != 12 and count != 13 and count != 14)):
    print(f'{count} попугая')
else:
    print(f'{count} попугаев')
