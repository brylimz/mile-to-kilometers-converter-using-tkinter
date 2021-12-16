import random


def add(*args):
    sum = 0
    for num in args:
        sum = sum+num
    print(sum)


add(random.randint(1, 10))
