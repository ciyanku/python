# FACTORS OF A NUMBER
n = 12

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


# PERFECT NUMBER
n = 28
sum_factors = 0

for i in range(1, n):
    if n % i == 0:
        sum_factors += i

if sum_factors == n:
    print("Perfect Number")
else:
    print("Not Perfect Number")


# PRIME NUMBER
n = 13
is_prime = True

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")


# STRING REVERSE
a = "SHERYIANS"
print(a[::-1])


# PALINDROME STRING
a = "NAMAN"

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# COUNT DIGITS, ALPHABETS, SPECIAL CHARACTERS
s = "abc123@#"

digits = 0
alphabets = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        alphabets += 1
    else:
        special += 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Special:", special)


# WHILE LOOP
a = 1

while a <= 10:
    print(a)
    a += 1


# REVERSE A NUMBER
num = 1234
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10

print(rev)


# PALINDROME NUMBER
a = 121
copy = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a //= 10

if copy == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")


# NUMBER GUESSING GAME
import random

secret = random.randint(1, 10)
guess = int(input("Guess number (1-10): "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong! Number was", secret)


# FUNCTIONS
def hello():
    print("Hello World")

hello()


# LISTS
a = [10, 20, 30, 40]

a.append(50)
print(a)
print(a[0])


# TUPLES
a = (1, 2, 3, 4)

print(a)
print(a[1])


# SETS
a = {1, 2, 3, 4, 4, 5}

print(a)


# DICTIONARIES
d = {
    "name": "Prashant",
    "age": 22
}

print(d["name"])


# EXCEPTION HANDLING
try:
    a = 10
    b = 0
    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")


# FILE HANDLING
file = open("sample.txt", "w")
file.write("Hello Python")
file.close()

file = open("sample.txt", "r")
print(file.read())
file.close()