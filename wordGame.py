import getch
import os
import fileHandler
from chatAPI import w25
import promptBank as pb
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#creates a menu from a list of words
def menu(question , options):
    clear()
    print(question)
    print()
    for i in range(len(options)):
        print(str(i + 1) + ": " + options[i])
    print()
    char = getch.getch()
    #return c as an int
    try:
        c = int(char)
        return options[c - 1]
    except:
        if char == "q":
            return -1
        else:
            print("Invalid input")
            time.sleep(500/1000)
            return menu(question, options)
        
def teach(word, info):
    print()
    message = pb.prompt("literary_example", word, info)
    #print(message)
    print(w25(message))
    print()
    message = pb.prompt("connotation", word, info)
    print()
    #print(message)
    print(w25(message))
    print()
    return True

def stagePlay(word):
    print("Please use the vocab word in a response to the prompt as if you are the second in a two man play: " + '\n')
    message = pb.prompt("prompt3", word)
    personna = random.choice(["Man 1", "Woman 1", "Dog 1"])
    prompt = (personna + ": " + w25(message))
    print(prompt)
    print()
    info = input("-> ")
    message = pb.prompt("dialogue", word, (prompt + '\n' + "Man 2: " + "\"" + info + "\""))
    print()
    print(w25(message))
    print()

def tutor(word, info):
    #randomly select one of two functions
    if random.choice([True, False]):
        stagePlay(word)
    else:
        teach(word, info)

def synonym(word):
    message = pb.prompt("synonym", word)
    print()
    #print(message)
    print(w25(message))
    print()
    return True
    

##########################################################
posVneg = ["positive", "negative", "neutral", "unknown"] #
actVstate = ["an act", "a state of being", "unknown"]    #
setsize = 10                                             #
##########################################################
clear()
setNum = input("What set would you like to practice? ")
path = "word_lists/sets/set" + str(setNum) + ".csv"
fh = fileHandler.fileHandler(path)
set = fh.randomSet(setsize)
oldScore = round(fh.fullSetScore(),2)
input("Set score is " + str(oldScore) + ". Press enter to continue")
clear()
flag = True
while flag:
    numCorrect = 0
    numNeutral = 0
    for i in range(setsize):
        progress = (str(i + 1) + "/" + str(setsize))
        line = set[i]
        info = fh.getLine(line).split(",")
        word = info[0]
        checkForNeutral = True
        if info[2].strip() == "neutral" and checkForNeutral == True:
            print("Neutral word: " + word)
            synonym(word)
            time.sleep(5)
            numCorrect += 1
            numNeutral += 1
        else:
            question = "Set " + str(setNum) + '\n' + '(' + progress + ') ' + "What connotation does '" + word + "' inspire?"
            answer = menu(question, posVneg)
            if answer == -1:
                flag = False
                break
            else:
                if info[2].strip() == answer.strip():
                    numCorrect += 1
                    print("Correct!")
                    print()
                    synonym(word)
                    print()
                    print("Tutor anyway? y/n")
                    char = getch.getch()
                    if char == "y":
                        print("Gotcha - here ya go!\n")
                        tutor(word, info)
                        input("Press enter to continue")
                    grant = 10
                    if int(info[3]) <= 200 - grant:
                        score = int(info[3]) + grant
                    else:
                        score = 200
                    fh.replaceLine(line, word + "," + info[1] + "," + info[2] + "," + str(score) + "\n")
                else:
                    print("Incorrect: " + word + " is " +info[2])
                    print()
                    synonym(word)
                    print()
                    tutor(word, info)
                    input("Press enter to continue")
                    deduct = 10
                    if int(info[3]) >= deduct:
                        score = int(info[3]) - deduct
                    fh.replaceLine(line, word + "," + info[1] + "," + info[2] + "," + str(score) + "\n")
        clear()
    if flag ==True:
        setScore = 0
        for i in range(setsize):
            line = set[i]
            setScore += int(fh.getLine(line).split(",")[3])
        setPercent = round((setScore + numNeutral * 200) / (setsize * 200), 2)
        setPercent *= 100
        #print("Set score: " + str(setPercent) + "%")
        print()
        print("Set Correct: " + str(numCorrect) + "/" + str(setsize))
        print()
        score = fh.fullSetScore()
        score = round(score, 2)
        print("Full Set: " + str(oldScore) + "% --> " + str(score) + "%")
        x = input("Run set again? y/n/(r)andomize: ")
        if x == "n":
            flag = False
        elif x == "r":
            set = fh.randomSet(setsize)

        