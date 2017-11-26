import betaIdentify
import format
import os
try:
    os.remove('betaIdentify.pyc')
    os.remove('format.pyc')
except:
    print()

terms = betaIdentify.getTerms()
final = []
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
#print(findStem("divitiae", "divitiarum", 1, True))

#s = "123456"
#print(s[:2]) -> 12
#print(s[:-2]) -> 1234
#print(s[2:]) -> 3456
#print(s[-2:]) -> 56

def main(possibleTerms):
    currentTerm = possibleTerms[0]
    dct, prs, trn = "", "", ""
    #print(possibleTerms)
    word = possibleTerms[0]
    for termId in range(1, len(possibleTerms)):
        partOfSpeech = possibleTerms[termId][0]
        if partOfSpeech == "p":
            dct = possibleTerms[1][1][1]
            prs = "prep w/ %s"%(possibleTerms[1][1][0])
            trn = possibleTerms[1][1][2]
        if partOfSpeech == "adv":
            dct = possibleTerms[1][1][1]
            prs = possibleTerms[1][0]
            trn = possibleTerms[1][1][0]
        if partOfSpeech == "c":
            dct = possibleTerms[1][1][0]
            prs = "conj"
            trn = possibleTerms[1][1][1]
        if partOfSpeech == "adj":
            x = "x"
        if partOfSpeech == "v":
            x = "x"
        if partOfSpeech == "n": #possibleTerms[i] = ['n', ['tribunus', '-i', 'm', 'tribune']] If term is noun
            genitive = possibleTerms[termId][1][1]
            gender = possibleTerms[termId][1][2]
            definition = possibleTerms[termId][1][3]
            if gender == "pl": #in case it is ['n', ['divitiae', 'divitiarum', 'pl', 'f', 'wealth']] with pl
                gender = possibleTerms[termId][1][3]
                definition = possibleTerms[termId][1][4]
            declension = findDeclension(genitive, gender)
            nominative = possibleTerms[termId][1][0]
            onlyPlural = False
            if possibleTerms[termId][1][2] == "pl": #if noun only exists in the plural
                onlyPlural = True
            stem = findStem(nominative, genitive, declension, onlyPlural)
            endings = getList(gender)
            endings = endings[declension]
            for endingId in range(0, 10):
                currentWord = stem + endings[endingId]
                if word == currentWord:
                    dct = ", ".join([nominative, genitive])
                    case = getCase(endingId)
                    if endingId < 5:
                        number = "Sg"
                    else:
                        number = "Pl"
                    prs = "-".join([gender.upper(), case, number])
                    trn = definition

    #print("")
            #print(possibleTerms[i])
    lisOfFive = [currentTerm, dct, prs, trn, ""]
    return(lisOfFive)


for term in terms: # a term looks like ['ad', ['p', ['ac', 'ad', 'to, toward']]]
    possibleTerms = betaIdentify.getPossibleWords(term)
        #if term == problem term:
        #print(possibleTerms)
    final.append(main(possibleTerms))
format.main(final)
#possibleTerms[0] is always the word

#when the list looks like [["paro", "paro, 1", "1 S P-I-A", "prepare", ""]]
#then do format.main(list)
