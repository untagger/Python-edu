import random

lower = 0

upper = 100

lists = []

A = []

B = []

for num in range(lower, upper + 1):

  if num > 1:

      for i in range(2, num):

          if (num % i) == 0:

              break

      else:

          lists.append(num)

x = 5

for x in range(0,x):

  a = random.randint(0,100)

  A.append(a)

s = 0

for t in lists:

  for h in A:

     if h == t:

        B.append(t)

print(f"Massiv A:n{A}")

print(f"Massiv B:n{B}")