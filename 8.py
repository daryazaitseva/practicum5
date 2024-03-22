knat = int(input('Введите количество кнатов: '))
galleon = knat // (17*29)
sikly = (knat % (17*29)) // 29
knats = (knat % (17*29)) % 29
if galleon != 0:
    print(f'{galleon} галлеонов')
if sikly != 0:
    print(f'{sikly} сиклей')
if knats != 0:
    print(f'{knats} кнатов')
