day1 = int(input('Введите количество подданых, которые видели улыбку в 1 день: '))
day2 = int(input('Введите количество подданых, которые видели улыбку во 2 день: '))
day3 = int(input('Введите количество подданых, которые видели улыбку в 3 день: '))
if day1 != day2 and day1 != day3 and day2 != day3:
    print(1)
elif day1 == day2 == day3:
    print(3)
else:
    print(2)
