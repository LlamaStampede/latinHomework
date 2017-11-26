#Need to add Vocative Case


nounSuffixesM = ["placeholder", #so that a word's suffixes can be called via sufs[decl] instead of sufs[decl-1]
                 ["a","ae","ae","am","a","ae","arum","is","as","is"],#because poeta
                 ["","i","o","um","o","i","orum","is","os","is"],
                 ["","is","i","em","e","es","um","ibus","es","ibus"],
                 ["","us","ui","um","u","us","uum","ibus","us","ibus"],
                 ["","ei","ei","em","e","es","erum","ebus","es","ebus"]]

nounSuffixesF = ["placeholder", #so that a word's suffixes can be called via sufs[decl] instead of sufs[decl-1]
                 ["a","ae","ae","am","a","ae","arum","is","as","is"],
                 ["placeholder"],
                 ["","is","i","em","e","es","um","ibus","es","ibus"],
                 ["","us","ui","um","u","us","uum","ibus","us","ibus"],
                 ["","ei","ei","em","e","es","erum","ebus","es","ebus"]]

nounSuffixesN = ["placeholder", #so that a word's suffixes can be called via sufs[decl] instead of sufs[decl-1]
                 ["placeholder"],
                 ["","i","o","","o","a","orum","is","a","is"],
                 ["","is","i","","e","a","um","ibus","a","ibus"],
                 ["","us","ui","um","u","us","uum","ibus","us","ibus"], #because cornu
                 ["placeholder"]]

cases = ["N", "G", "D", "Acc", "Abl"]

def getCase(endingId):
    new = endingId % 5
    return(cases[new])

def getList(gender):
    if gender == "m" or gender == "c":
        nounSuffixes = nounSuffixesM
    if gender == "f":
        nounSuffixes = nounSuffixesF
    if gender == "n":
        nounSuffixes = nounSuffixesN
    return(nounSuffixes)

def findDeclension(genitive, gender):
    nounSuffixes = getList(gender)
    for i in range(1, len(nounSuffixes)):
        if nounSuffixes[i] == ["placeholder"]:
            continue
        curEnding = nounSuffixes[i][1] #the genitive term for each suffix declension
        curPlEnding = nounSuffixes[i][6]#the plural genitive term for each declensoin
        curGenEnding = genitive[-1 * len(curEnding):]
        curGenPlEnding = genitive[-1 * len(curPlEnding):]
        if curGenEnding == curEnding or curGenPlEnding == curPlEnding:
            return(i)

def findStem(nominative, genitive, declension, onlyPlural):
    if genitive[0] == "-":#no 3rd dec all 4th some 1, some 2, some 5
        if declension == 1:
            return(nominative[:-1])
        elif declension == 2 or declension == 5:
            if onlyPlural:
                return(nominative[:-1])
            else:
                return(nominative[:-2])
        elif declension == 4:
            if nominative[-2:] == "us":
                return(nominative[:-2])
            else:
                return(nominative[:-1])
    else:
        if declension == 3:
            return(genitive[:-2])
        elif declension == 1:
            return(genitive[:-4])#only plural subtracts -arum
        elif declension == 2:
            if onlyPlural:
                return(genitive[:-4])
            else:
                return(genitive[:-1])
        elif declension == 5:
            return(genitive[:-1])
