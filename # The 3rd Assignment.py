                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #                The 3rd Assignment

# Task No.(1) Prime Number Checker
# This is a Python program that has a function called is_prime(n) that checks if a given number is prime or not.

print("This is a program that checks if a given number is prime or not. ")
n = int(input("Please Enter Your Number To Check \n"))

def is_prime (n) :
    if n%2==0 or n%3==0 :
        print(f"{n} isn't a prime number")
    else :
        print("It is a prime number")


if n < 0 :
    print("This is a (-ve)Number")
elif n == 0 :
    print("This is Zero")
elif n <= 3 :
    print("This is a prime number")
else :
    is_prime (n)

# ............................................................................................
print("Lets get the second task \n")
# Task No.(2) Custom Calculator
# This is a Python program that has a function called calculator that calculate numbers

print("This is a program that calculates 2 numbers")
operation = input("Please Enter Your operation [add,subtract,multiply,divide]\n")
a = float(input("Please insert your 1st number \n"))
b = float(input("Please insert your 2nd number \n"))

def calculator (a,b,operation) :
    if operation == "add" :
        return a+b
    elif operation == "subtract" :
        return a-b
    elif operation == "multiply" :
        return a*b
    elif operation == "divide" :
        return a/b
    
print (calculator (a,b,operation))