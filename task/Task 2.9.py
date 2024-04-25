a=int(input("введите пятизначное число "))
l = list(str(a))
print(l)
b=int(input("введите на сколько сдвинуть в право "))
n = b # сдвиг
print(''.join(l[-n:] + l[:-n]))

