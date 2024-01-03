# DSC510
# Week 9
# Programming Assignment 9.1 - Week 9
# Author - Eric Vance
# 10/26/2021

# Change Control Log
# Change#: 1
# Change(s) Made: Added function to print to file
# Date of Change(s): 10/26/21
# Author: Eric Vance
# Change Approved by: N/A
# Date Moved to Prod: N/A

#please note, my gettysburg.txt file is just in my downloads folder, which is the same location as this script
import string

#function to print in an easy-to-read format. used dictionary sorting instead of list as a challenge
'''def pretty_print(d):
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print("{:<12} {:>10}".format("Word","Count"))
    print("-----------------------")
    for key, value in d.items():
        print("{:<12} {:>10}".format(key, value))'''

#function to print to file instead of console
def process_file(sorted_dict, file):
    sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    with open(file, 'a') as f:
        print("{:<12} {:>10}".format("Word","Count"), file=f)
        print("-----------------------", file=f)
        for key, value in sorted_dict.items():
            print("{:<12} {:>10}".format(key, value), file=f)


#function to take word from process_line function and add to dictionary and increment
def add_word(word, counts):
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

#function to make words uniform case and remove punctuation
def process_line(line, d):
    lineLower = line.lower()
    lineStrip = lineLower.translate(str.maketrans('', '', string.punctuation))
    for word in lineStrip.split():
        add_word(word, counts)

def main():
    global counts
    counts = {}
    try:
        gba_file = open("gettysburg.txt", "r")
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, counts)
    file_name = input("Please enter a file name including the extension: ")
    with open(file_name, 'w') as f:    #writing the length of the dict to file before rest of info appended
        print("Length of the dictionary: {}".format(len(counts)), file=f)
    process_file(counts, file_name)

if __name__ == "__main__":
    main()
