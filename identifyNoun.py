def openN(file):
    f = open("Nouns/" + file, "r")
    lines = f.read().split("\n")
    f.close()
    return(lines)


def compare(word, lisWords):
    print(word, lisWords)

def identify(word): #in this example lets do amicorum
    firstDecF = "a, ae, ae, am, a, ae, arum, is, as, is".split(", ")
    secondDecM = "us, i, o, um, o, i, orum, is, os, is".split(", ")
    secondDecN = "um, i, o, um, o, a, orum, is, a, is".split(", ")
    thirdM = "-, is, i, em, e, es, um, ibus, es, ibus".split(", ")
    thirdN = "-, is, i, -, e, a, um, ibus, a, ibus".split(", ")
    thirdIM = "is, is, i, em, e, es, ium, ibus, es, ibus".split(", ")
    thirdIN = "e, is, i, e, i, ia, ium, ibus, ia, ibus".split(", ")
    fourthM = "us, us, ui, um, u, us, uum, ibus, us, ibus".split(", ")
    fourthN = "u, us, u, u, u, ua, uum, ibus, ua, ibus".split(", ")
    fifthF = "es, ei, ei, em, e, es, erum, ebus, es, ebus".split(", ")
    fifthM = "es, ei, ei, em, e, es, erum, ebus, es, ebus".split(", ")
    all = [firstDecF, secondDecM, secondDecN, thirdM, thirdN, thirdIM, thirdIN, fourthM, fourthN, fifthF, fifthM]
    #print(all)
    possible = []
    for i in range(0, len(all)):
        for j in all[i]:
            if j == word[-len(j):]:
                possible.append([j, i])
    for i in possible:
        temp = word[:-len(i[0])]
        #print(temp, i)
        if i[1] == 0:
            lines = openN("firstDeclNoun.txt")
            possibleJ = []
            for j in lines:
                if j[0] == word[0]:
                    possibleJ.append(j.split("\t"))
            compare(temp, possibleJ)
        elif i[1] == 1:
            lines = openN("firstDeclNoun.txt")
            possibleJ = []
            for j in lines:
                if j[0] == word[0]:
                    possibleJ.append(j.split("\t"))
            compare(temp, possibleJ)


identify("amicorum")
#w = "civibus"
#print(w[2:])
#print(w[:2])
#print(w[-2:])
#print(w[:-2])
