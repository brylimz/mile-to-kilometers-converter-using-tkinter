import random


#
# def foo(a, b=4, c=6):
#     print(a, b, c)
#
#
# foo(20, c=7)

#
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(add(1, 10)))
#
#
# def calculate(**kwargs):
#     print(kwargs)
#     print([kwargs])
#
#
# calculate(add=3, multiply=5)
#
#
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw["model"]
#

# quiz
def all_aboard(a, *args, **kwargs):
    print(a, args, kwargs)


all_aboard(4, 7, 3, 0, x=10, y=64)
