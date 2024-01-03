# DSC510
# Week 10
# Programming Assignment 10.1 - Week 10
# Author - Eric Vance
# 11/04/2021

# Change Control Log
# Change#: 0
# Change(s) Made: N/A
# Date of Change(s): N/A
# Author: Eric Vance
# Change Approved by: N/A
# Date Moved to Prod: N/A

import requests
import sys

def main():
    print("Hello - and welcome to my Chuck Norris joke generator.")
    user_input = input("Would you like to hear a Chuck Norris Joke? Press Y for yes, or any other key to exit.\n")
    while True:
        if user_input.lower() == 'y':
            response = requests.get("https://api.chucknorris.io/jokes/random")
            new_response = response.json()
            for k,v in new_response.items():    #parses the json response looking for value only
                if k == 'value':
                    print(v)
                    input2 = input("Would you like to hear another joke? Press Y for yes, or any other key to exit.\n")
                    if input2.lower() == 'y':    #simple error handling instead of using try/except
                        continue
                    else:
                        print("Thank you!")
                        #exits out of the program with exit message
                        sys.exit()

        else:
            print("Thanks - have a good day!")
            break

if __name__ == "__main__":
    main()

