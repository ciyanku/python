# OBJECT ORIENTED PROGRAMMING (OOP)

class Factory:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Factory Name:", self.name)

f1 = Factory("ABC Factory")
f1.show()


# INHERITANCE

class Factory:
    def work(self):
        print("Factory is working")

class FactoryMumbai(Factory):
    def location(self):
        print("Located in Mumbai")

f = FactoryMumbai()
f.work()
f.location()


# METHOD OVERRIDING

class Animal:
    def sound(self):
        print("Animal makes sound")

class Human(Animal):
    def sound(self):
        print("Human speaks")

h = Human()
h.sound()


# ENCAPSULATION

class Factory:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

f = Factory()
print(f.get_salary())


# ABSTRACTION

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def area(self):
        print("Area of Square")

s = Square()
s.area()


# POLYMORPHISM / OPERATOR OVERLOADING

class Animal:

    def __str__(self):
        return "Animal Object"

a = Animal()
print(a)


# PROPERTY DECORATOR

class Student:

    def __init__(self):
        self._marks = 90

    @property
    def marks(self):
        return self._marks

s = Student()
print(s.marks)


# DECORATORS

def decorate(func):

    def wrapper():
        print("Before Function")
        func()
        print("After Function")

    return wrapper

@decorate
def hello():
    print("Hello")

hello()


# KWARGS

def information(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)

information(name="Prashant", age=22)


# DICTIONARY COMPREHENSION

d = {i: i**2 for i in range(1, 6)}
print(d)


# MAP FUNCTION

def double(x):
    return x * 2

a = [1, 2, 3, 4, 5]

result = list(map(double, a))
print(result)


# PATTERN PROGRAMS

for i in range(1, 6):
    print("*" * i)

"""
*
**
***
****
*****
"""


# STRONG NUMBER

num = 145
temp = num
sum_fact = 0

while temp > 0:

    digit = temp % 10

    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print("Strong Number")
else:
    print("Not Strong Number")


# PRIME NUMBERS FROM 2 TO 20

for num in range(2, 21):

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)


# MAXIMUM OCCURRENCE IN LIST

a = [1, 2, 3, 2, 4, 2, 5, 3]

max_element = max(set(a), key=a.count)

print("Maximum Occurrence:", max_element)
print("Frequency:", a.count(max_element))