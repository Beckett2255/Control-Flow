# Programmer: Beckett Jacobs
# Date: 10.11.2021
# Program: ATM Bank Transaction

"""
This program simulates an ATM If, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators
"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# set up account by asking users for their first & Last names using Variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us",first_name,last_name +", we will now set up a escurity PIN on your account.\n")

# set up a PIN - Personal Identification Number
pin = input("Please choose a 4-digit Personal Identifiaction Number: ")

print("\nThank you",first_name + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n*********************************************\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert yourATM card\n")
    print("Welcome to Cash-R-Us ATM",first_name,last_name,"\n")
    userPIN = input("What is your four digit PIN: ")

    if pin == userPIN:
        balance = 674
        print("\nYour Balance: $" + str(balance))


    else:
        print("Sorry",first_name,last_name,"your PIN doesn't match our records ")


else:
    print("\nHave a wonderful day",first_name,last_name + ", please come back to visit us soo,")
