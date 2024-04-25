a = float(input("Введите сумму: "))
b = int(a)
print(b, end=' ')
a *= 10
ryb = a % 10
a *= 10
kop = a % 10
print(int(ryb), int(kop), sep='')