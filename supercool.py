f = open("aiden_verbs.txt", "r")
verbList = f.read().split("\n")
f.close
for i in range(len(verbList)): #I get why you did this
    verbList[i] = verbList[i].split("\t")
#print verbList

term = raw_input("Enter a verb: ")

for verb in verbList:
    print verb
    if len(verb) != 6 and not verb[-1][-1] in ["I","6","D","*","P","F","S"]:
        print "",

for verb in verbList:
    if verb[0][0] == term[0] or verb[2][0] == term[0]:
        primary = verb[0][:-1]
        secondary = verb[0][:-1]
        
