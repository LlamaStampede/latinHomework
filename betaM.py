import betaIdentify
import format
import noun
import os
try:
    os.remove('betaIdentify.pyc')
    os.remove('format.pyc')
    os.remove('noun.pyc')
except:
    print()

terms = betaIdentify.getTerms()
final = []

#s = "123456"
#print(s[:2]) -> 12
#print(s[:-2]) -> 1234
#print(s[2:]) -> 3456
#print(s[-2:]) -> 56

cases = ["N", "G", "D", "Ac", "Ab"]
def parsing(endingsId, endingId):
    if endingsId == 0:
        gender = "F"
    elif endingsId == 1:
        gender = "M"
    else:
        gender = "N"
    case = cases[endingId % 5]
    if endingId < 5:
        number = "Sg"
    else:
        number = "Pl"
    prs = "-".join([gender, case, number])
    return(prs)

def main(possibleTerms):
    empty = " "
    currentTerm = possibleTerms[0]
    word = possibleTerms[0] #yes i realize this is a duplicate lol idk why
    dct, prs, trn = "", "", ""
    confirmedTerms = []
    for termId in range(1, len(possibleTerms)):
        partOfSpeech = possibleTerms[termId][0]
        if partOfSpeech == "p":
            dct = possibleTerms[1][1][1]
            prs = "prep w/ %s"%(possibleTerms[1][1][0])
            trn = possibleTerms[1][1][2]
            confirmedTerms.append([currentTerm, dct, prs, trn, ""])
        if partOfSpeech == "adv":
            dct = possibleTerms[1][1][1]
            prs = possibleTerms[1][0]
            trn = possibleTerms[1][1][0]
            confirmedTerms.append([currentTerm, dct, prs, trn, ""])
        if partOfSpeech == "c":
            dct = possibleTerms[1][1][0]
            prs = "conj"
            trn = possibleTerms[1][1][1]
            confirmedTerms.append([currentTerm, dct, prs, trn, ""])
        if partOfSpeech == "adj":

            allEndings = [["a","ae","ae","am","a","ae","arum","is","as","is"],
                          ["us","i","o","um","o","i","orum","is","os","is"],
                          ["um","i","o","um","o","a","orum","is","a","is"]]
            #possibleTerms[termId]  is ['adj', ['longus, a, um', 'long']] or ['adj', ['miser, misera, miserum', 'sad, wretched']] or ['adj', ['noster, nostra, nostrum', 'our, ours']]
            curTerm = possibleTerms[termId][1][0]
            #print(word, curTerm)
            if curTerm[-7:] == ", a, um": #if like longus a um
                stem = curTerm[:-9]
                for endingsId in range(0, len(allEndings)):
                    for endingId in range(0, len(allEndings[endingsId])):
                        curWord = stem + allEndings[endingsId][endingId]
                        #print(curWord)
                        if word == curWord:
                            confirmedTerms.append([currentTerm, curTerm, parsing(endingsId, endingId), possibleTerms[termId][1][1], ""])
            else:
                print(curTerm)
        if partOfSpeech == "v":
            x = "x"
        if partOfSpeech == "n": #possibleTerms[termId] = ['n', ['tribunus', '-i', 'm', 'tribune']] If term is noun
            genitive = possibleTerms[termId][1][1]
            gender = possibleTerms[termId][1][2]
            definition = possibleTerms[termId][1][3]
            if gender == "pl": #in case it is ['n', ['divitiae', 'divitiarum', 'pl', 'f', 'wealth']] with pl
                gender = possibleTerms[termId][1][3]
                definition = possibleTerms[termId][1][4]
            declension = noun.findDeclension(genitive, gender)
            nominative = possibleTerms[termId][1][0]
            onlyPlural = False
            if possibleTerms[termId][1][2] == "pl": #if noun only exists in the plural
                onlyPlural = True
            stem = noun.findStem(nominative, genitive, declension, onlyPlural)
            endings = noun.getList(gender)
            endings = endings[declension]
            for endingId in range(0, 10):
                if endings[endingId] == "":
                    currentWord = nominative
                else:
                    currentWord = stem + endings[endingId]
                if word == currentWord:
                    dct = ", ".join([nominative, genitive])
                    case = noun.getCase(endingId)
                    if endingId < 5:
                        number = "Sg"
                    else:
                        number = "Pl"
                    prs = "-".join([gender.upper(), case, number])
                    trn = definition
                    confirmedTerms.append([currentTerm, dct, prs, trn, ""])

    #print("")
            #print(possibleTerms[i])
    lisOfFive = []
    errors = []
    if len(confirmedTerms) == 0:
        confirmedTerms.append([currentTerm, dct, prs, trn, ""])
    if len(confirmedTerms) == 1:
        lisOfFive = confirmedTerms[0]
    else:
        for termId in range(0, len(confirmedTerms)): # a term is ['metus', 'metus, -us', 'M-G-Sg', 'fear', '']
            term = confirmedTerms[termId]
            prs = term[2].split("-")
            if termId == 0:
                w = term[0]
                d = term[1]
                p = prs
                t = term[3]
            else: #if any extra term, probably there is an easier way to write this
                if w != term[0]:
                    w = empty
                if d != term[1]:
                    d = empty
                if p[0] != prs[0]:
                    p[0] = empty
                if p[1] != prs[1]:
                    p[1] = empty
                if p[2] != prs[2]:
                    p[2] = empty
                if t != term[3]:
                    t = empty
        lisOfFive = [w, d, "-".join(p), t, ""]
        errors.append([word, confirmedTerms])
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
