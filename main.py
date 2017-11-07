#copyright Michael Lembck and Aiden Bailey
#Steel is baad

possibleThing = "paratus, parans, parabaris, parent, paravisse, parat, parabuntur, paraverint".split(", ")
verb = "paro, parare, paravi, paratus".split(", ")

def indicative(word, verb): # checks all indicatives except perfect system of passives because they are 2 words
    # verb is [paro, parare, paravi, paratus] {thx -a}
    curword = ""
    endings = ["o, s, t, mus, tis, nt".split(", "), "r, ris, tur, mur, mini, ntur".split(", ")] # {modified passive endings: or --> r. is this right? -a}
    futEnding = ", i, i, i, i, u".split(", ")
    stem = verb[1][:-2]#stem = parare - re = para
    perfStem = verb[2][:-1] #stem = parvi - i = parav
    perfEndings = "i, isti, it, imus, istis, erunt".split(", ")
    weird = ["m", "r"]
    for i in range(0, 6):
        for j in range(0, len(endings)):
            if i == 0:
                curword = stem[:-1] + endings[j][i]
            else:
                curword = stem + endings[j][i]
            if word == curword:
                return(True)
            if i == 0:
                currword = stem + "ba" + weird[j]
            else:
                currword = stem + "ba" + endings[j][i]
            if word == currword:
                return(True)
            if i == 0:
                curreword = stem + "b" + endings[j][i]
            else:
                curreword = stem + "b" + futEnding[i] + endings[j][i]
            if word == curreword:
                return(True)
        #print(curword, currword, curreword)
        perf = perfStem + perfEndings[i]
        if i == 0:
            pperf = perfStem + "era" + weird[0]
            fperf = perfStem + "er" + endings[0][i]
        else:
            pperf = perfStem + "era" + endings[0][i]
            fperf = perfStem + "eri" + endings[0][i]

        if pperf == word or perf == word or fperf == word:
            return(True)
        #print(perf, pperf, fperf, jdf)
        return(False)



def participal(word, verb):
    noun = "ns, ntis, nti, ntem, nte, ntes, ntium, ntibus, ntes, ntia".split(", ") #{I deleted a repeat of ntibus, edited the genitive plural (i-stem), and added the neuter plural -a}
    for i in noun:
        preAct = verb[1][:-2] + i #good thinking
        if word == preAct:
            return(True) #We might want to return more than just True

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

def infinitives(word, verb): #there is a mess up here with 2nd conjugation verbs having moni instead of moneri
    if word == verb[1]:
        return(True)
    elif word == verb[2] + "sse":
        return(True)

def checkVerb(word, verb):
    if indicative(word, verb) or infinitives(word, verb) or participal(word, verb):
        return(True)
    return(False)

f = open("/Users/mlembck/Desktop/verbs.txt", "r")
verbList = f.read().split("\n")
for i in range(0, len(verbList)):
    verbList[i] = verbList[i].split("\t")
    #print(verbList[i])
f.close()
#verbList = [["4 prinparts", "definition"], [...]]
#print(indicative(possibleThing[7], verb))

while True:
    x = input("Enter a verb: ")
    if x == "stop":
        break
    for verb in verbList:
        #stop = False
        #print(verb[0][0])
        if verb[0][0] == x[0]:
            stop = checkVerb(x, verb[0].split(", "))
            #print(verb)
        if stop == True:
            print("Dictionary Entry: ", verb[0], "\nTranslation: ", verb[1])
        else:
            stop = participal(x, verb[0].split(', ')) #This line can't affect anything: the verb is about to change and "stop" is about to be reset (on line 100)
            #Also, I feel like lines 99, 100, and 102 could be combined:
            # if (verb[0][0] == x[0] or verb[2][0] == x[0]) and checkVerb(x, verb[0].split(", ")):
            # Note: I added {checkVerb(x, verb[0].split(", "))} because some verbs changetheir first letter int the perfect, ie. ago agere egi actus
