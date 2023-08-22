import random

class fileHandler:
    lines = []
    wordSet = None

    def __init__(self, path):
        self.path = path
        f = open(path, "r")
        self.lines = f.readlines()
        f.close()

    def replaceLine(self, line, newLine):
        self.lines[line] = newLine
        f = open(self.path, "w")
        f.writelines(self.lines)
        f.close()

    def randomSet(self, num):
        #generate a list  of random numbers between 0 and the number of lines in the file
        self.wordSet = random.sample(range(0, len(self.lines)), num)
        return self.wordSet
    
    def getLine(self, line):
        return self.lines[line]
    
    def fullSetScore(self):
        score = 0
        for i in range(len(self.lines)):
            score += int(self.lines[i].split(",")[3])
        max = len(self.lines)*200
        score = score / max
        score = round(score, 4)
        return score * 100
    
