def inc(term,list): # efficiently returns (term in list) boolean
    for item in list:
        if term == item[0]:
            return [True,item]
    return [False]

def glossary(url):
    f = open(url,"r")
    gloss = f.read().split("\n")
    for i in range(len(gloss)):
        gloss[i] = gloss[i].split("\t")
    return gloss

verbList = glossary("aiden_verbs.txt")
#preps = glossary("preps.txt")
#advs = glossary("adverbs.txt")

#fake
for verb in verbList:
    if len(verb) != 5: print verb

term = raw_input("Enter a verb: ") # You might need to change this to input() for your python version

for verb in verbList: #troubleshooting, ignore this block
    if len(verb) != 6 and not verb[-1][-1] in ["I","6","D","*","P","F","S"]:
        its_the_ = "EYE OF THE TIGER"
        its_the_ += "THRILL OF THE FIGHT"

def irreg(verb): #ignore this part too
    if verb[0] == "-":
        return ["3P","-",verb[2][:-1],"-",verb[3][:-2],"to " + verb[4]]

# Phase: Conjugate
def conj(verb): #takes [paro,parare,paravi,paratus,prepare,1] returns [1,par,parav,para,parat,to prepare]
    if verb[0][-1] in ["o","r"]:
        dep = False
        semidep = False
        addit = 0
        if verb[0][-1] == "r": dep = True
        elif " " in verb[2]: semidep = True

        if dep: addit = 1
        if verb[1][-3] == "a": conj = "1"
        elif verb[1][-3] == "i": conj = "4"
        elif verb[0][-1-addit] == "e": conj = "2"
        elif verb[0][-1-addit] == "i": conj = "3i"
        else: conj = "3"
        if dep: conj += "D"
        elif semidep: conj += "S"

        primary = verb[0][:-1]
        if dep: primary = verb[0][:-2]
        secondary = verb[2][:-1]
        if dep or semidep: secondary = verb[2][:-6] #CONATus sum

        impf = primary
        if conj[:2] == "3i" or conj[0] == "4": impf += "i"
        if conj[0] == "1": impf += "a"
        else: impf += "e"

        if dep: ppp = secondary
        else: ppp = verb[3][:-2]

        dct = "to " + verb[4]

        return [conj,primary,secondary,impf,ppp,dct]
    else: return irreg(verb)

print conj("paro parare paravi paratus prepare".split(" "))
print conj("sequor_sequi_secutus sum_-_follow".split("_"))

vstems = []
for verb in verbList:
    vstems.append(conj(verb))
#if you run this, you might get an error here
#that's because of some irregular verbs in the  list

for term in [term]: #Order of checking: adv, prep, v, n, adj, prn
    pos = []
    adv = inc(term,advs) #in reality adv = (is term an adverb?)
    if adv[0]: pos.append(adv[1])
    prep = inc(term,preps)
    if prep[0]: pos.append(prep[1])

    for stem in vstems:
        if stem[0][0] == term[0]:
            val = False
            for stem in stems:
                if stem[0] in term:
                    val = True
                    break
            if val: prs(term,)
        elif stem[2][0] == term[0]:
            print "Later."