import random
import colorama
import time
from lorem_text import lorem
colorama.init(autoreset=True)

Red = '\033[91m'
Cyan = '\x1b[36m'
Green = '\033[32m'
Yellow = '\033[93m'


def my_countdown():
   for n in range(3, 0, -1):
       time.sleep(1)
       print(n, '...', sep='', end=' ')
       n -= 1
       if n == 0:
           print(Red + 'Начали!')


def my_input():
   generate_sentence = lorem.words(random.randint(5, 15))
   print(' ' + Cyan + generate_sentence)
   start_time = time.time()
   my_inp = input('Введите текст выше: ')
   end_time = time.time()
   total_time = end_time - start_time
   my_statistics(my_inp, round(total_time, 2), generate_sentence)


def my_statistics(user_sentense, user_time, sentense):
   while sentense == user_sentense:
       count_symbols = str(round((len(user_sentense)/user_time*60), 2))
       print(Green + '#'*36,
             Green + ' Вы отлично справились! '.center(36, '#'),
             Green + (' Время печати: ' + str(user_time) + ' c. ').center(36, '#'),
             Green + (' Скорость печати: ' + count_symbols + ' зн/м ').center(36, '#'),
             Green + '#'*36, sep='\n')
       break
   else:
       print(Yellow + ' Увы, в тексте вы допустили ошибки')


while True:
  my_countdown()
  my_input()
  if _ := input('Начать заного(д) или завершить програму(н)? ') == 'н':
      break
  else:
      continue

print('До новых встреч!')
