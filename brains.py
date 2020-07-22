from firebase import firebase
from flask import Flask

db = firebase.FirebaseApplication('https://web-scrapping-de6ca.firebaseio.com/')

# List of all the Majors
majors = db.get('/Major_and_Reqs', None).keys()

userClasses = []


def userInput():
    # global userClasses
    print("Hello World!")
    # userClasses = list


userInput()



<!--------------------pseudo Code---------------->

user_classes = []

possible = []

for i in user_classes:

    if #look for verificaiton of value - A && #extract the path in which the class has been verified -E:
        possible.append()


pprint(possible)
