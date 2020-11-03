#Maksim stserbakov 03.11.2020 Задача 2
a = int(input('Введите число:a'))
b = int(input('Введите число:b'))
c = int(input('Введите число:c'))
perimeter = a+b+c
print("Периметр треугольника = ", perimeter)

#Maksim stserbakov 03.11.2020 Задача 9
a=int(input('Ввести литры топлива '))
b=int(input('Ввести пройденные километры '))
result = (a/b) * 100
print(round(result,2))

#Maksim stserbakov 03.11.2020 Задача 6
import math
a=int(input('Введите число:a '))
b=int(input('Введите число:b '))
c=math.sqrt(a**2 + b**2)
print(round(c,2))

#Maksim stserbakov 03.11.2020 Задача 3
a=36.75
c=a / 100 * (100-40) * 3
print(c)

#Maksim stserbakov 03.11.2020 Задача 4
pizza=12.90
tips=10
c=pizza/100*10
summa=(pizza+c)/3
print('каждый должен заплатить',round(summa,2))

#Maksim stserbakov 03.11.2020 Задача 7
print('введите целое число')
dec=int(input())
b=bin(dec)
o=oct(dec)
h=hex(dec)
print(f'bin {b}| oct{0}|hex{h}')

#Maksim stserbakov 03.11.2020 Задача 5
a=29.9/60*24
print('проедит за 24 мин, при средней скорости 29.9км/ч')
print(round(a,2))

