height1, height2, height3 = map(int, input('Введите значания 3 высот: ').split(' '))
sum = height1 + height2 + height3
print(min(height1, height2, height3), sum - max(height1, height2, height3) -
      min(height1, height2, height3), max(height1, height2, height3))