# DSC510
# Week 8
# Programming Assignment 8.1 - Week 8
# Author - Eric Vance
# 10/19/2021

# Change Control Log
# Change#:N/A
# Change(s) Made: First iteration of program
# Date of Change(s): N/A
# Author: Eric Vance
# Change Approved by: N/A
# Date Moved to Prod: N/A

#please note, my gettysburg.txt file is just in my downloads folder, which is the same location as this script
import string

#function to print in an easy-to-read format. used dictionary sorting instead of list as a challenge
def pretty_print(d):
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print("{:<12} {:>10}".format("Word","Count"))
    print("-----------------------")
    for key, value in d.items():
        print("{:<12} {:>10}".format(key, value))

#function to take word from process_line function and add to dictionary and increment
def add_word(word, d):
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

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
    print("Length of the dictionary: ", len(counts))
    pretty_print(counts)

if __name__ == "__main__":
    main()









