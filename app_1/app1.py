#!/usr/bin/python3.6

import json
from difflib import get_close_matches

data = json.load(open("/home/mark/Documents/Python_Course/data.json",'r'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %a instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist!"
        else:
            return "We didn't understand that"
    else:
        return "The word doesn't exist!"

word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
