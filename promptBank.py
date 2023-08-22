import random

def prompt(prompt, word, info=""):
    #match case using prompt type
    match prompt:
        case "connotation":
            message = "Please succinctly explain why the word '" + word + "' has a " + info[2] + " connotation."
            return message
        case "definition":
            pass
        case "academic_example":
            message = "Please return a few sentences from an academic paper that uses the word '" + word + "'. The text from the academic paper must include the word '" + word + ".'" + " If possible, please return the name of the paper and it's premise at the end of the response."
            return message
        case "literary_example":
            message = "Please return a few sentences from a literary example that uses the word '" + word + "'. The text from the literary example must include the word '" + word + ".'" + " If possible, please return the name of the work and it's premise at the end of the response."
            return message
        case "synonym":
            message = "Please return two synonyms for the word '" + word + "' in the format 'synonym1, synonym2'."
            return message
        case "prompt":
            message = "Please produce a sentence using a synonym of the word '" + word + "' in the charactor of a kooky memorable person who is going throught some sort of outrageous experience or event. The sentence needs to be in the first person, as if it was dialogue from a comedic play."
            return message
        case "prompt2":
            bank = open("wordBankGen.txt")
            content = bank.readlines()
            x = random.randrange(10, 25549, 2)
            y = content[x]
            message = "Please produce a sentence in the charactor of a kooky memorable person who is going throught some sort of outrageous experience or event involving " + y + ". The sentence needs to be in the first person, as if it was dialogue from a comedic play."
            #print(message)
            return message
        case "prompt3":
            bank = open("wordBankGen.txt")
            content = bank.readlines()
            x = random.randrange(10, 25549, 2)
            y = content[x]
            message = "Please produce a sentence in the character of a normal person who is going throught some sort of silly or uncomfortable experience or event involving " + y + " and " + word +". The sentence needs to be in the first person, as if it was dialogue from a stage play. Do not use the word '" + word + "' in your response. Try not to be too silly. Try come up with a few responses before returning one."
            #print(message)
            return message
        case "dialogue":
            words = info.split(" ")
            message = info + '\n' + "Please output one or two sentences of dialouge as if you are ' " + words[0] + " 1' and responding to 'Man 2'. Feel free to be mildy silly."
            #print(message)
            return message
        case _:
            return False