import string
from arithmetic import *

# perform calculation

while True:
    user_input = raw_input("> ")

    tokens = string.split(user_input)

    if tokens[0] == "+":
        if len(tokens) != 3:
            print "Please enter two numbers to add. For example:"
            print "+ 1 2"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print add(tokens[1], tokens[2])
    elif tokens[0] == "-":
        if len(tokens) != 3:
            print "Please enter two numbers to subtract. For example:"
            print "- 3 1"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print subtract(tokens[1], tokens[2])
    elif tokens[0] == "*":
        if len(tokens) != 3:
            print "Please enter two numbers to multiply. For example:"
            print "* 4 2"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print multiply(tokens[1], tokens[2])
    elif tokens[0] == "/":
        if len(tokens) != 3:
            print "Please enter two numbers to divide. For example:"
            print "/ 4 2"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print divide(tokens[1], tokens[2])
    elif tokens[0] == "square":
        if len(tokens) != 2:
            print "Please enter one number to square. For example:"
            print "square 3"
        else:
            tokens[1] = int(tokens[1])
            print square(tokens[1])
    elif tokens[0] == "cube":
        if len(tokens) != 2:
            print "Please enter one number to cube. For example:"
            print "cube 2"
        else:
            tokens[1] = int(tokens[1])
            print cube(tokens[1])
    elif tokens[0] == "power":
        if len(tokens) != 3:
            print "Please enter exactly two numbers. For example:"
            print "power 2 5"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print power(tokens[1], tokens[2])
    elif tokens[0] == "mod":
        if len(tokens) != 3:
            print "Please enter exactly two numbers. For example:"
            print "mod 5 3"
        else:
            tokens[1] = int(tokens[1])
            tokens[2] = int(tokens[2])
            print mod(tokens[1], tokens[2])
    elif tokens[0] == "q":
        exit()
    else:
        print "Sorry, I'm not sure what that means. Please enter a valid argument."
