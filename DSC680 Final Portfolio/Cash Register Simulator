# DSC510
# Week 11
# Programming Assignment 11.1 - Week 11
# Author - Eric Vance
# 11/10/2021

# Change Control Log
# Change#: 0
# Change(s) Made: N/A
# Date of Change(s): N/A
# Author: Eric Vance
# Change Approved by: N/A
# Date Moved to Prod: N/A

import locale

class CashRegister():
    def __init__(self):
        self.total = 0.0
        self.items = 0

    def add_items(self):
        self.items = self.items + 1

    def add_price(self, price):
        self.total = self.total + price

    def get_total(self):
        return self.total

    def get_count(self):
        return self.items

def main():
    print("Welcome! I hope you enjoy using the cash register.")
    register = CashRegister()
    while True:
        user_input = input("Would you like to add an item? Press 'Y' for yes, or any other key to exit. ")
        #block below keeps track of number of items and price - user can choose to exit by key command
        if user_input.lower() == 'y':
            register.add_items()
            while True:
                try:
                    user_input2 = input("What is the price? Enter in xx.xx (float) format, please!")
                    register.add_price(price=float(user_input2))
                except ValueError:
                    print("Please try again, and enter numbers only in xx.xx (float) format.")    #requires float format
                    continue
                else:
                    break
        else:
            break
    #locale ensures currency symbol is used
    locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
    print("Thanks for using the cash register!")
    print("Total price: " + str(locale.currency(register.get_total())))
    print("Total item count: " + str(register.get_count()))

if __name__ == "__main__":
    main()


