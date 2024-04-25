import re
a = input("Введите номер автомобиля РФ формата Е001КХ777: ")
b = re.compile(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}')
if re.match(b,a):
    print("Верно")
else:
    print("Не верно")