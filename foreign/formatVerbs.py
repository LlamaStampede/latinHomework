#The heart of this code is the insert(index, value) function used here
#lis = ["1", "2", "3", "5"]
#lis.insert(3, "4")
#lis now is ["1", "2", "3", "4", "5"]


#returns a list of all of the "paro 1" things with ["par", index]
def getVerbs():
    f = open("verbs.txt", "r")
    lines = f.read().split("\n")
    f.close()

    listOfVerbs = []
    for id in range(0, len(lines)):
        lines[id] = lines[id].split("\t")
        if lines[id][1] == "1":
            stem = lines[id][0][:-1]
            listOfVerbs.append([stem, id, lines[id][2]])
    return(listOfVerbs, lines)

#takes the spot of the paro 1 and deletes it, then adds "paro	parare	paravi	paratus	prepare" in its spot
def writeVerbs(listOfVerbs, lines): #here listOfVerbs is [['par', 161, 'prepare']] in this case
    for i in listOfVerbs:
        lines.pop(i[1])
        prinParts = [i[0] + "o", i[0] + "are", i[0] + "avi", i[0] + "atus", i[2]]
        lines.insert(i[1], prinParts)

    for i in range(0, len(lines)):
        lines[i] = "\t".join(lines[i])
    lines = "\n".join(lines)

    f = open("verbs.txt", "a")
    f.write(lines)
    f.close()



x, y = getVerbs()
writeVerbs(x, y)
print("Completed reformatting verbs such as [paro 1 prepare] to ['paro', 'parare', 'paravi', 'paratus', 'prepare']")
