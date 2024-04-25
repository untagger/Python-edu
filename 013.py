a, b = map(int, input("Введите два целых числа:").split())

for i in range(a, b + 1):

  print(f"{i} * {i} = {i**2}")