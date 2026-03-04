# 1. Write a function `greet(name)` that takes a person's name as input and prints a greeting message like `"Hello, <name>! Welcome to Python."`

def greet(name):
    print(f"Hello, {name}! welcome to python.")
s=input("Enter your name:")
greet(s)

# output:
# Enter your name:Manjunadh
# Hello, Manjunadh! welcome to python.

# 2. Write a function `add_numbers(a, b)` that takes two numbers as parameters and returns their sum.

def add_numbers(a, b):
    return a+b

print(add_numbers(123, 456))

# output:
# 579

# 3. Write a function `is_even(num)` that takes an integer as input and returns `True` if the number is even, otherwise returns `False`.

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
num=int(input("Enter a number:"))
print(is_even(num))

# output:
# Enter a number:24
# True

# # 4. Write a function `find_max(a, b, c)` that takes three numbers as arguments and returns the largest among them.

def find_max(a, b, c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c

a, b, c = map(int, input("Enter three numbers separated by comma:").split(","))

print(find_max(a, b, c))

# output:
# Enter three numbers separated by comma:2,56,234
# 234

# 5. Write a function `count_vowels(string)` that takes a string as input and returns the total number of vowels present in it.

def count_vowels(string):
    vowel="aeiouAEIOU"
    count=0
    for ch in string:
        if ch in vowel:
            count+=1
    return count
str=input("Enter a string:")
print(count_vowels(str))

# output:
# Enter a string:Manjunadh
# 3