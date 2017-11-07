f = open("aiden_verbs.txt", "r")
verbList = f.read().split("\n")
f.close
for i in range(len(verbList)):
    verbList[i] = verbList[i].split("\t")
#print verbList

term = raw_input("Enter a verb: ") # You might need to change this to input() for your python version

for verb in verbList: #troubleshooting, ignore this block
    if len(verb) != 6 and not verb[-1][-1] in ["I","6","D","*","P","F","S"]:
        its_the_ = "EYE OF THE TIGER"
        its_the_ += "THRILL OF THE FIGHT"

def irreg(verb): #ignore this part too
    return "(i haven't written this function yet)"

# This is the main thing I wrote in this program:
def conj(verb): #takes [paro,parare,paravi,paratus,prepare,1] returns [1,par,parav,para,parat,to prepare]
    if verb[0][-1] in ["o","r"]:
        dep = False
        addit = 0
        if verb[0][-1] == "r": dep = True

        if dep: addit = 1
        if verb[1][-3] == "a": conj = "1"
        elif verb[1][-3] == "i": conj = "4"
        elif verb[0][-1-addit] == "e": conj = "2"
        elif verb[0][-1-addit] == "i": conj = "3i"
        else: conj = "3"
        if dep: conj += "D"

        primary = verb[0][:-1]
        if dep: primary = verb[0][:-2]
        secondary = verb[2][:-1]
        if dep: secondary = verb[2][:-6] #CONATus sum

        impf = primary
        if conj[:2] == "3i" or conj[0] == "4": impf += "i"
        if conj[0] == "1": impf += "a"
        else: impf += "e"

        if dep: ppp = secondary
        else: ppp = verb[3][:-2]

        dct = "to " + verb[-1] # [-2] for the current verbList

        return [conj,primary,secondary,impf,ppp,dct]
    else: return irreg(verb)

print conj("paro parare paravi paratus prepare".split(" "))
print conj("sequor sequi secutus_sum follow".split(" "))

stems = []
for verb in verbList:
    stems.append(conj(verb))
#if you run this, you might get an error here
#that's because of some irregular verbs in the  list

for verb in verbList: #I'll add to this later
    if verb[0][0] == term[0] or verb[2][0] == term[0]:
        print "Another one bites the dust"
