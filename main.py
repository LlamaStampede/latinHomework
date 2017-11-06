#copyright © Michael Lembck and Aiden Bailey
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

def getVerbs():
    f = open("/Users/mlembck/Desktop/verbs.txt", "r")
    lines = f.read().split("\n")
    for i in range(0, len(lines)):
        lines[i] = lines[i].split("\t")
    #print(lines[i])
    f.close()
    return(lines)

def participal(word, verb):
    noun = "ns, ntis, nti, ntem, nte, ntes, ntum, ntibus, ntes, ntibus".split(", ")
    for i in noun:
        preAct = verb[1][:-2] + i
        if word == preAct:
            return(True)

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

verbList = getVerbs() #[["4 prinparts", "definition"], [...]]
#print(indicative(possibleThing[7], verb))
stay = True
while stay:
    x = input("Enter a verb: ")
    if x == "stop":
        stay = False
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
                stop = participal(x, verb[0].split(', '))
