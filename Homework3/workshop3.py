import random

n = 500000000
count = 0

for i in range(n):
    x = random.random() / 2
    y = random.random() / 2

    if x ** 2 + y ** 2 <= 0.25:
        count += 1


pi = 4 * count / n 

print(pi)