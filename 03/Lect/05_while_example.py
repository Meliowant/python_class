# -*- encoding:utf-8 -*-

a = float(input("A bigger than 0: "))
a = a if a > 0 else 1
while a > 0:
    print("+", end='')
    a = a - 1
print('')
