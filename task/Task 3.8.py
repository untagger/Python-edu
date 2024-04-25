print("Введите время в секундах(но не более 28800): ")
seconds = 28800 - int(input())
hours = seconds // 3600
seconds -= 3600 * hours
minutes = seconds // 60
seconds -= 60 * minutes
if hours: print(hours, "Час(ов)", end = '')
if minutes: print(minutes, "Минут(ы)", end = '')
if seconds: print(seconds, "Секунда(ы)", end = '')
print()
input("Осталось прибывать на работе")