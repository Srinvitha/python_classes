import datetime
import random

def give_response(user_text):

    s = random.randint(0,10000000)
    sa = "square area when side is" + str(s)
    if user_text == "hi":
        c = ("hello","hi","namaste","namaskar")
        response = random.choice(c)
    elif user_text == "what is the time":
        response  = str(datetime.datetime.now())
    elif user_text == "help":
        response = "I can help you find area of square, rectangle and circle.I can also help find the perimeter of square and rectangle and the circumference of a circle.Ok?"
    elif user_text == "ok":
        response = " :) "

    elif user_text == sa :
        n = [int(s) for s in str.split(user_text) if s.isdigit()]
        n = n[0]
        response = str(n*n)

        print(user_text)


    else:
        response =  "I did not understand"


    return response
