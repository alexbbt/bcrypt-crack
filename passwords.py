import os
from progress import printProgressBar

# get window with
rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns)

import sys
from passlib.hash import bcrypt

choice = input('check common passwords or whole english dictionary? (p/d): ')

if (choice != "p" and choice != "d"):
    sys.exit('Invalid Option')

passwords = (choice == "p")

if (passwords):
    text_file = open("passwords.txt", "r")
else:
    text_file = open("words.txt", "r")

words = text_file.read().splitlines()

hash = input('hash to crack: ')
length = len(words)

correct_word = ""
for (index, word) in enumerate(words):
    printProgressBar(index, length, prefix = 'Progress:', suffix = 'Complete', length = columns)
    correct = bcrypt.verify(word, hash)
    if (correct):
        correct_word = word
        print()
        break

print("correct word is:", correct_word)
