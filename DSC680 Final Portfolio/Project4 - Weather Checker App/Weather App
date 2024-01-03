# DSC510
# Week 12
# Programming Assignment 12.1 - Week 12 (Final Project)
# Author - Eric Vance
# 11/17/2021

# Change Control Log
# Change#: 0
# Change(s) Made: N/A
# Date of Change(s): N/A
# Author: Eric Vance
# Change Approved by: N/A
# Date Moved to Prod: N/A

import requests
import sys

#function to connect to API, zip code method
def zip_code_input(zip, tempType):
    while True:
        try:
            if tempType == 'K' or tempType == 'k':
                url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=45de28cf0b633575561935eac21ac9e7&units=standard'.format(zip)
                response = requests.get(url)
            elif tempType == 'C' or tempType == 'c':
                url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=45de28cf0b633575561935eac21ac9e7&units=metric'.format(zip)
                response = requests.get(url)
            elif tempType == 'F' or tempType == 'f':
                url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid=45de28cf0b633575561935eac21ac9e7&units=imperial'.format(zip)
                response = requests.get(url)
            else:
                sys.exit("Thank you! Goodbye.")
        except:
            print("Not a valid zip or failure to connect to API. Please try again!")
            continue
        else:
            new_response = response.json()
            return new_response


#function to connect to API, city/state method. need to add append US- method
def city_state_input(city, state, tempType):
    while True:
        try:
            if tempType == 'K' or tempType == 'k':
                url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=45de28cf0b633575561935eac21ac9e7&units=standard'.format(city,'us-'+state)
                response = requests.get(url)
            elif tempType == 'C' or tempType == 'c':
                url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=45de28cf0b633575561935eac21ac9e7&units=metric'.format(city,'us-'+state)
                response = requests.get(url)
            elif tempType == 'F' or tempType == 'f':
                url = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&appid=45de28cf0b633575561935eac21ac9e7&units=imperial'.format(city,'us-'+state)
                response = requests.get(url)
            else:
                sys.exit("Thank you! Goodbye.")
        except:
            print("Not a valid city/state combo or failure to connect to API. Please try again!")
            continue
        else:
            new_response = response.json()
            return new_response

#takes json data and puts it into a clean dictionary
def dict_maker(dictionary):
        new_dict = {
        'Current temperature (degrees): ': dictionary['main']['temp'],
        'High temperature (degrees): ': dictionary['main']['temp_max'],
        'Low temperature (degrees): ': dictionary['main']['temp_min'],
        'Pressure (hPa): ': dictionary['main']['pressure'],
        'Humidity %: ': dictionary['main']['humidity'],
        'Cloud Cover %: ': dictionary['clouds']['all']
        }
        return new_dict

#prints the dictionary from dict_maker() in a clean, easy to read format
def pretty_print(d):
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    print("{:<32} {:>10}".format("Category","Value"))
    print("-------------------------------------------")
    for key, value in d.items():
        print("{:<32} {:>10}".format(key, value))

def main():
    while True:
        choice_input = input("Press 1 to look up city by Zip Code, or 2 to look up by City name. Any other key will exit. ")
        if choice_input == "1":
            while True:
                    inputZip = input("Please enter a 5-digit zip code: ")  #user inputs 5 digit zip code
                    if (len(inputZip) == 5) & inputZip.isdigit():
                        break
                    else:
                        print("Sorry - enter a valid zip please.")
                        continue
            inputTempType = input("Enter temperature type: 'K' for Kelvin, 'C' for Celsius, 'F' for Fahrenheit. Any other key to exit.")
            zipCode = zip_code_input(inputZip, inputTempType)    #user input is plugged into zip_code_input function
            clean_dict = dict_maker(zipCode)
            pretty_print(clean_dict)

        elif choice_input == "2":
            cityInput = input("City: ")
            stateInput = input("State (2 char state code): ")
            inputTempType = input("Enter temperature type: 'K' for Kelvin, 'C' for Celsius, 'F' for Fahrenheit. Any other key to exit.")
            cityState = city_state_input(cityInput, stateInput, inputTempType)
            clean_dict = dict_maker(cityState)
            pretty_print(clean_dict)
        else:
            print("Thank you!")
            sys.exit()
        again = input("\nWould you like to look up another area? 'Y' for yes, any other key for no.")
        if again == 'Y' or again == 'y':
            continue
        else:
            print("Thank you!")
            break


if __name__ == "__main__":
    main()
#Professor Eller - thanks for being so helpful this semester. I feel like my skills have improved immensely because of you!
