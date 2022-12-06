#!/usr/bin/env python3
from functools import reduce

def admin_login(username, password):
    username = username.upper()
    if username == "ADMIN" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 40 and temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def add_str_nums(val_a, val_b):
    return int(val_a) + int(val_b)     

def fizzbuzz(num):
    num_str = str(num)
    if len(num_str) == 1:
        if num == 0:
            print(f"returning {num_str} in top")
            return "FizzBuzz"
        if num % 3 == 0:
            return "Fizz"
        elif num == 5:
            return "Buzz"
        else:
            return num
    else :
        total = reduce(add_str_nums, num_str,0)
        if (total % 3 == 0) and (num % 3 == 0) and (total % 3 == 0) and (num % 5 == 0):
            print("returning in bottom")
            return "FizzBuzz"
        elif total % 5 == 0 or num % 5 == 0:
            return "Buzz"
        elif total % 3 == 0 or num % 3 == 0:
            return "Fizz"
        else:
            return num

print(fizzbuzz(3))
print(fizzbuzz(33))
print(fizzbuzz(42))
        
def calculator(operation, num1, num2):
    lookup = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2
    }

    if lookup.get(operation) or lookup.get(operation) == 0:
        return lookup.get(operation)
    else:
        print("Invalid operation!")
        return None

