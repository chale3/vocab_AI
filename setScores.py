
import fileHandler

for x in range(10):
    setNum = x + 1
    path = "word_lists/sets/set" + str(setNum) + ".csv"
    fh = fileHandler.fileHandler(path)
    oldScore = round(fh.fullSetScore(),2)
    print("Set " + str(setNum) +  " score is " + str(oldScore))


