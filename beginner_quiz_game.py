''' THIS IS AN IMPROVISED CODE '''

print("Welcome to Quizone!")

# 1st WAY to perform this if statement...
yeslist = ["y","yes","yep","yeah"]
nolist = ["n", "no", "nope"]

#input function to input a value
interested = input("Are you interested to play?\n").lower() #.lower() will convert the whole input value in lower case. 
interested = interested.rstrip() #rstrip() helps to reduce space issue in output
if interested in nolist:
    quit()

print("Cool! Let's get started!")

# 2nd WAY  
'''interested = input("Do you wanna play?\n")
print (interested) #not mandatory here. It will be the same without this 'print' function

#using .lower() so all kinds of 'yes' will be converted into lower case
if interested.lower() != "yes":
    quit()

print("Cool! Let's get started!")''' 

point = 0
correct = 0

answer = input("What does https stand for?\n")
answer = answer.rstrip()
if answer.lower() == "hypertext transfer protocol secure": #.lower()/.upper() can be written with if statement 
    print("Correct!\n")
    point += 1
    correct += 1
else:
    print("Wrong Answer!\n")

answer = input("Who is called the father of Python?\n")
answer = answer.rstrip()
if answer.lower() == "guido van rossum" or answer.lower() == "guido":
    print("Correct!\n")
    point += 2
    correct += 1
else:
    print("Wrong Answer!\n")

answer = input("What is the permanent storage device of a computer?\n").lower() #.lower()/.upper() can be written after input function also
answer = answer.rstrip()
if answer == "rom" or answer == "read only memory":
    print("Correct!\n")
    point += 3
    correct += 1
else:
    print("Wrong Answer!\n")

answer = input("Byte is the series of ……………… bits.\n").lower()
answer = answer.rstrip()
if answer == "eight" or answer == "8":
    print("Correct!\n")
    point += 4
    correct += 1
else:
    print("Wrong Answer!\n")

if point != 0:
    print("Congratulations! You got " + str(point) + " points.") #it can either be concatenated the int value with '+' sign by making it a string with 'str' or ....
    print("Total", correct, "answers are correct!") #or single comma is also right. In this case the int should not be converted into string with 'str' type
    print("Your average is", str((correct/4)*100) + "%") 
else:
    print("0 points! :(")
    print("Better luck next time!")

