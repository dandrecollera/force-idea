import random


def readfile():
    a_file = open("ideas.txt", "r")
    lines = a_file.readlines()
    rand = random.randint(0, len(lines))
    a_file.close()

    print("Your Project is: \n"+lines[rand])
    del lines[rand]

    new_file = open("ideas.txt", "w+")
    for line in lines:
        new_file.write(line)
    new_file.close()


def appendfile(text):
    a_file = open("ideas.txt", "a")
    a_file.write(text + " \n")
    a_file.close()


while(True):
    choice = str(
        input("Type 'a' to add an idea or 'b' to force yourself to do your own idea: "))

    if choice == 'a':
        while(True):
            idea = str(input("Enter an Idea: "))
            appendfile(idea)
            choice2 = str(input("add more idea? y/n: "))
            if choice2 == 'y':
                pass
            elif choice2 == 'n':
                break
            else:
                pass
        break
    elif choice == 'b':
        readfile()
        break
