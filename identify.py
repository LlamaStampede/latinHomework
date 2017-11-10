#copyright Michael Lembck and Aiden Bailey
#Steel is baad

possibleWords = "paratus, parans, parabaris, parent, paravisse, parat, parabuntur, paraverint".split(", ")
exampleVerb = "paro, parare, paravi, paratus".split(", ")

def indicative(word, verb): # checks all indicatives except perfect system of passives because they are 2 words
    #print(word, verb)
    # verb is [paro, parare, paravi, paratus] {thx -a}
    presWord = ""
    endings = ["o, s, t, mus, tis, nt".split(", "), "or, ris, tur, mur, mini, ntur".split(", ")] # {modified passive endings: or --> r. is this right? -a} {you're right ~m}
    futEnding = ", i, i, i, i, u".split(", ")
    stem = verb[1][:-2]#stem = parare - re = para
    perfStem = verb[2][:-1] #stem = parvi - i = parav
    perfEndings = "i, isti, it, imus, istis, erunt".split(", ")
    OneSgEndings = ["m", "r"]
    for i in range(0, 6): # 6 is for the amount of endings
        for j in range(0, len(endings)):
            if i == 0:
                presWord = stem[:-1] + endings[j][i]
            else:
                presWord = stem + endings[j][i]
            if word == presWord: #{should I combine lines 22, 28, and 34? ~m}
                return(True)
            if i == 0:
                perfWord = stem + "ba" + OneSgEndings[j]
            else:
                perfWord = stem + "ba" + endings[j][i]
            if word == perfWord:
                return(True)
            if i == 0:
                futWord = stem + "b" + endings[j][i]
            else:
                futWord = stem + "b" + futEnding[i] + endings[j][i]
            if word == futWord:
                return(True)
        perf = perfStem + perfEndings[i]
        if i == 0:
            pperf = perfStem + "era" + OneSgEndings[0]
            fperf = perfStem + "er" + endings[0][i]
        else:
            pperf = perfStem + "era" + endings[0][i]
            fperf = perfStem + "eri" + endings[0][i]

        if pperf == word or perf == word or fperf == word:
            return(True)
    return(False)



def participal(word, verb):
    noun = "ns, ntis, nti, ntem, nte, ntes, ntium, ntibus, ntes, ntia".split(", ") #{I deleted a repeat of ntibus, edited the genitive plural (i-stem), and added the neuter plural -a}{ok ~m}
    for i in noun:
        preAct = verb[1][:-2] + i #good thinking{thanks ~m}
        if word == preAct:
            return(True) #We might want to return more than just True {yes if we want to do the parsing, when i made this i thought we weren't gonna have the program do that ~m}

    endings = "us, i, o, um, orum, is, os, a, ae, am, arum, as".split(', ')
    for i in endings:
        perPas = verb[3][:-2] + i
        if word == perPas:
            return(True)
        futPas = verb[1][:-2] + "nd" + i
        if futPas == word:
            return(True)
        futAct = verb[3][:-2] + "ur" + i
        if futAct == word:
            return(True)
    return(False)

def infinitives(word, verb): #there is a mess up here with 2nd conjugation verbs having moni instead of moneri {This problem will be removed with your conjugation identifier ~m}
    if word == verb[1]:
        return(True)
    elif word == verb[2] + "sse":
        return(True)

def checkVerb(word, verb):
    #print(word, verb)
    if indicative(word, verb) or infinitives(word, verb) or participal(word, verb):
        return(True)
    return(False)
def main(word):
    f = open("verbs.txt", "r")
    verbList = f.read().split("\n")
    for i in range(len(verbList)): #I get why you did this {ok ~m}
        #print(verbList[i])
        temp = verbList[i].split("\t")
        verbList[i] = [[temp[0], temp[1], temp[2], temp[3]], temp[4], temp[5]]

    f.close()
    #verbList = [["4 prinparts", "definition"], [...]]
    #print(indicative(possibleWords[7], verb))

    x = word#raw_input("Enter a verb: ") #Ignore this edit, I'm looking into how to upgrade my python {yeah pls do ~m}
        #if x == "stop":
        #break
    for verb in verbList:
        #print(verb[0][0])
        stop = False # The merge I mention below would eliminate the need for this line
        if verb[0][0][0] == x[0]:
            #print(verb[0][0])
            stop = checkVerb(x, verb[0])
            #print(verb)
        if stop == True:
            return (verb[0], verb[1])
        else:
            stop = participal(x, verb[0]) # This line can't affect anything: the verb is about to change and "stop" is about to be reset (on line 100). Also it caused an error.
            #Also, I feel like lines 99, 100, and 102 could be combined:
                # if (verb[0][0] == x[0] or verb[2][0] == x[0]) and checkVerb(x, verb[0].split(", ")): {Sounds good, go for it ~m}
                # Note: I added {verb[2][0]} because some verbs change their first letter in the perfect (ago agere EGI actus)
    return(None, None)
