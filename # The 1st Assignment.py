                                    #   Name  : -     Mena Monir Helal
                                    #   Course: -       Python & AI
                                    #                The 1st Assignment

# Task No.(1)
# This is a Python program that asks the user to input the current temperature in Celsius.
#  Based on the input, the program should display an appropriate message:

Temp = float(input("Enter the current temperature in Celsius:"))
if Temp >= 30 :
    print("It's a hot day. Stay hydrated!")
elif Temp >=20 :
    print("It's a warm day. Enjoy the weather!")
elif Temp >=10 :
    print("It's a cool day. Wear a jacket!")
else :
    print("It's a cold day. Stay warm!")

#..........................................................................................................

# Task No.(2)
# Write a Python program that processes a list of numbers that are divisible by 3 in range (1:20):

for i in range(1,21):
    if i%3 == 0 :
        print(i,"is divisible by 3",f"this is a trial No.{i} ")
    else:
        print("N/A~",f"this is a trial No.{i} ")