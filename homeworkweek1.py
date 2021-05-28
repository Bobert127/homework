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

#funkca 8

a = [1, 3]
def find_boundaries(a):
    li = []
    for i in a:
        li.append(i)
    minli = min(li)
    maxli = max(li)
    print([minli, maxli])
find_boundaries([7,8,10,2, 62])


#funkcja 9
a = [1, 3]
def find_boundaries(a):
    li = []
    for i in a:
        if type(i) == int:
            li.append(i)
        else:
            ""
    minli = min(li)
    maxli = max(li)
    print([minli, maxli])
find_boundaries([7,8,10, "robert", 5, 17])

#funkcja 10

a = [1, 3]

if len(a) == 0:
    none
else:
    def find_boundaries(a):
        li = []
        for i in a:
            if type(i) == int:
                li.append(i)
            elif type(i) != int:
                ""
            minli = min(li)
            maxli = max(li)

        print([minli, maxli])
    find_boundaries([1,5,9,4])

#funkcja 11

my_list = [1, 2]
print(my_list * 4)

my_list_2 = [True, False]
print(my_list_2 * 4)

find_short_words = []
l = ('Litwo', 'ojczyzno', 'moja', 'ty', 'jesteś', 'jak', 'zdrowie')
for i in l:
   if len(i) < 5:
       print(i)

numbers = [7, 2, 11, 5.77]
print(sum(numbers))

#funkcja 12
def mean(numbers=[]):
   numbers = [17.12, 19.19, 13.98, 45.34]
   a = len(numbers)
   b = sum(numbers)
   c = b/a
   print(f"Średnia wynos {c}")
mean()


d = {
    "ulica": "Królewny Śnieżki",
    "dom": 40,
    "miasto": "Olsztyn"
}

#funkcja 13
def list_keys(d):
    for key in d:
        print(key)


list_keys(d)

#funkcja 14
dictionary = {
    "name": "Władysław Hańcza",
    "role": "Kargul",
    "movie": "Sami swoi"
}

def message(dictionary):


    print("In " + dictionary["movie"] + ", " + dictionary["name"] + "is a " + dictionary["role"] + "." )

message(dictionary)


dictionary = {
    "name": "Władysław Hańcza",
    "role": "Kargul"

}

#funkcja 15

def message(dictionary):

    # if dictionary.get("movie"):
    #     print("In " + dictionary["movie"] + ", " + dictionary["name"] + "is a " + dictionary["role"] + ".")
    # else:
    #     print("none")
    print(dictionary.get("movie") or "None")
message(dictionary)

#funkcja 16

dlugosc = 7
szerokosc = 13

def square_area(dlugosc, szerokosc):
    return dlugosc * szerokosc

print(f"pole prostokąta wynosi:" ,square_area(dlugosc, szerokosc))

#funkcja 17

diamater = 17.22

def circle_circuit(diamater):
    return 3.14 * diamater

print(f"Obwód koła wynosi", circle_circuit(diamater))


#funkcja 18

yers = 5
dog = "burek"
if yers <= 2:
    a = yers * 10.5
elif yers > 2:
    a = 21 + (yers - 2) * 4

def dogs_age(yers):
    return a
print(f"{dog} = {a} lat")

#funkcja 19

def chessboard(n=8):
    for i in range(n):
        for j in range(n-4):
            print("#", end='*')
        print()

chessboard(8)


#funkcja 20

def is_divisible_by_4(liczba):

    if liczba % 4 == 0:
        print(True)
    else:
        print(False)
        #return liczba % 4


is_divisible_by_4(8)

#funkcja 21

l = (4, 2, 'dwa')


def histogram(l):
    for i in l:
        if type(i) == str:
            return
        elif type(i) == int:
            print(i * "#")
    print()


histogram(l)

#funkcja 22

def fib(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(17))

num = 2

#funkcja 23

def square(num):
    return num


# poniższe linijki przetestują Twoją funkcję:
print("2 podniesione do potęgi drugiej, to:", square(2))  # powinno być 4
print("16^2=", square(16))  # powinno być 256
print("256 do potęgi 2 =", square(256))  # powinno być 65536


#funkcja 24
subject = 10
times = 11

def multiply(subject, times):
    return subject * times

# poniższe linijki przetestują Twoją funkcję:
print("100 * 100 =", multiply(100, 100))  # 10000
print("2 razy 2 to", multiply(2, 2))  # 5? ;-)
print("15 * 10 =", multiply(15, 10))  # 150

#funkcja 25

base = 17
exponent = 2

def power(base, exponent=2):
    return base ** exponent
# poniższe linijki przetestują Twoją funkcję:
print("2 do potęgi 6 to", power(2, 6))  # 64
print("4 do potęgi 8 to", power(4, 8))  # 65536

#funkcja 26

zlotys = 1007
change = 3.85

def convert_to_usd(zlotys):
    return zlotys / change
# poniższe linijki przetestują Twoją funkcję:
print("385PLN = ", convert_to_usd(385), "USD")
print("100PLN = ", convert_to_u sd(100), "USD")

#funkcja 27
fahrenheit = 95

def to_celsius (fahrenheit):
    return (((fahrenheit - 32) * 5)/9)

print((((fahrenheit - 32) * 5)/9))

#funkcja 28

gross = 1230

vat = 0.23


def calculate_net(gross, vat):
    return gross / (1 + vat)


print(gross / (1 + vat))



number = 17

def is_even(number):
    return number % 2 == 0

print (number % 2 == 0)

#funkcja 29

number = 11

def is_even(number):
    return number % 2 == 0
print (number % 2 == 0)

number = 5


def iterate_through(number):
    for item in range(1, number + 1):
        if item % 2 == 0:
            a = True
        else:
            a = False
    print(item, a)


#funkcja 29

def add(a, b=2):
    return a + b
add(5)