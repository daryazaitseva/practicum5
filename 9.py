height1, height2, height3 = map(int, input('Введите значания 3 высот: ').split(' '))
summ = height1 + height2 + height3
print(min(height1, height2, height3), summ - max(height1, height2, height3) -
      min(height1, height2, height3), max(height1, height2, height3))
