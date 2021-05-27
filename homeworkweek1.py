import random

#funkcja 1
words = ["hello", "darkness", "my", "old", "friend"]

a = random.randint(0, 4)


def random_word(a):
    # print(random.randint(1, 5))

    print(words[a])


random_word(a)
#funkcja 2

def quadratic_function(x, a, b, c):
    print((a*x) ** 2 + b*x + c)

quadratic_function(1,3,5,2)

#funkca 3

a = "mama"
b = "tata"


def make_tuple(a, b, c=3, d=4):
    print(a, b, c, d)


make_tuple(a, b)

#funkcja 4
a = 0
b = 0
c = 0
d = 0


def make_tuple(a, b, c=3, d=4):
    print(a, b, c, d)


make_tuple(a, b, c, d)

funkcja 5

import random


def d6(num):
    l = []
    for i in range(1, num + 1):
        rzut = random.randint(1, 6)
        l.append(rzut)

    print(l, sum(l))


d6(9)

#funkcja 6
l = (4, 2, 'dwa')


def histogram(l):
    for i in l:
        if type(i) == str:
            return
        if type(i) == int:
            print(i * "#")
    print()


histogram(l)

#funkca 7
l = [1, 7, 6, 8, 3]


def find_first_and_last():
    k = []
    k.append(l[0])
    k.append(l[-1])

    print(k)


find_first_and_last()

