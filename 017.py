from random import randint

a = [randint(-10, 10) for x in range(20)]

print("Все числа: ",a)

a1=[i for i in a if i<0 and i % 2 == 0]

a2=[i for i in a if i>=0 or i % 2 != 0]

print("Массив А(все четные отрицательные числа): ")

print(a1)

print("Массив B(остальные): ")

print(a2)