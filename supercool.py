def inc(term,list): # efficiently returns (term in list) boolean
    for item in list:
        if term == item[0]: #[0] important
            return [True,item]
    return [False]

def glossary(url):
    f = open(url,"r")
    gloss = f.read().split("\n")
    f.close()
    for i in range(len(gloss)):
        gloss[i] = gloss[i].split("\t")
    return gloss

verbList = glossary("aiden_verbs.txt")
prepList = glossary("preps.txt")
advList = glossary("adverbs.txt")
nounList = [] #glossary("nouns.txt")

ex_term = raw_input("Enter a term: ") # You might need to change this to input() for your python version

preps = []
for prep in prepList:
    if len(prep) == 1:
        phase = prep[0]
    else:
        preps.append([prep[0].lower(),prep[1],phase])
advs = []
for adv in advList:
    advs.append(adv[::-1])

#to do: non-passive, "virtual deponent"
# Phase: Conjugate
def conj(verb): #takes [paro,parare,paravi,paratus,prepare,1] returns [1,par,parav,para,parat,to prepare]
    trn = "to "+verb[4]
    if verb[0][-1] in ["o","r"]:
        dep = False
        semidep = False
        addit = 0
        if verb[0][-1] == "r": dep = True
        elif " " in verb[2]: semidep = True

        if dep: addit = 1
        if verb[1][-3] == "a": conj = "1"
        elif verb[1][-3] == "i": conj = "4"
        elif verb[0][-2-addit] == "e": conj = "2"
        elif verb[0][-2-addit] == "i": conj = "3i"
        else: conj = "3"
        if dep: conj += "D"
        elif semidep: conj += "S"
        elif "-" in verb: conj = "def"

        primary = verb[0][:-1]
        if dep: primary = verb[0][:-2]
        secondary = verb[2][:-1]
        if dep or semidep: secondary = verb[2][:-6] #CONATus sum
        if verb[2] == "-": secondary = "-"

        impf = primary
        if conj[0] == "1": impf += "a"
        elif conj in ["3","3i","4"]: impf += "e"

        if dep: ppp = secondary
        elif verb[3] == "-": ppp = "-"
        else: ppp = verb[3][:-2]

        return [conj,primary,secondary,impf,ppp,trn]
    elif verb[0] == "-": return ["3P","-",verb[2][:-1],"-",verb[3][:-2],trn] #preterate
    elif verb[0][-1] == "m": return ["sum",verb[0],verb[2][:-1],verb[1],"-",trn] #sum-thing
    elif verb[0][-1] == "t":
        if verb[1] == "-": conj = "imp" #impersonal
        else: conj = "third" #third-only
        return [conj,verb[0],verb[1],"-","-",trn]

#print conj("paro parare paravi paratus prepare".split(" "))
#print conj("sequor_sequi_secutus sum_-_follow".split("_"))
#print conj("moneo monere monui monitus warn".split(" "))
#print conj("salveo salvere - - be_healthy".split(" "))

vstems = []
for verb in verbList:
    vstems.append(conj(verb))
#if you run this, you might get an error here
#that's because of some irregular verbs in the  list

decls = {"ae":1,"i":2,"is":3,"us":4,"ei":5}
for i in range(10):
    print decls
def decl(noun):
    [nom,gen,gend] = noun
    for s in decls:
        if s == gen[-len(s):]: suf = s
    return [decls[suf],nom,gen[:-len(suf)],gend.upper()]

nstems = []
for noun in nounList:
    nstems.append(decl(noun))

#Phase: Assemble
pos = []
for term in [ex_term]:
    pos.append([term])

    adv = inc(term,advs) #in reality adv = (is term an adverb?)
    if adv[0]: pos[-1].append(["adv",adv[1]])
    prep = inc(term,preps)
    if prep[0]: pos[-1].append(["prep",prep[1]])

    for stem in vstems:
        #print "Fake:",stem
        if stem[1] == term[:len(stem[1])]: pos[-1].append(["v","p",stem])
        if stem[2] != "-" and stem[2][:-1] == term[:len(stem[2])-1]: pos[-1].append(["v","pf",stem])
        if stem[3] == term[:len(stem[3])]: pos[-1].append(["v","ppl",stem])
        if stem[3] == term[:len(stem[3])]: pos[-1].append(["v","ppp",stem])

    prns = [["hic","this",5],["qui","-",6],["is","weak dem",3]] #id, def, max length
    pres = [["h"],["qu","cui"],["i","e"]] #prefixes (word-beginnings)
    for i in range(len(pres)):
        for pre in pres[i]:
            if len(term) <= prns[i][2] and term[:len(pre)] == pre: pos[-1].append(["prn",prns[i][:2]])

    #nouns
    for noun in nstems:
        if inc(term[0],stem[1:3]): pos[-1].append(["n",noun])

    #adjectives

for pts in pos:
    for p in pts[1:]:
        print p

#Phase: Select
final_list = []
conflict = []
personal = ["o","s","t","mus","tis","nt","or","ris","tur","mur","mini","ntur"]
perfects = ["i","isti","it","imus","istis","erunt"]
persons = ["1S","2S","3S","1P","2P","3P"]
sufs = ["placeholder",
["a","ae","ae","am","a","ae","arum","is","as","is"],
["","i","o","um","o","i","orum","is","os","is"],
["","is","i","em","e","es","um","ibus","es","ibus"],
["","us","ui","um","u","us","uum","ibus","us","ibus"],
["","ei","ei","em","e","es","erum","ebus","es","ebus"]]
case = ["N","G","D","Ac","Ab"]
number = ["S","P"]
vowels = ["a","e","i","o","u"]
for pts in pos: #possible terms
    fins = [] #finalists
    term = pts.pop(0)
    for p in pts: #possibility
        if p[0] in ["adv","prep"]: fins.append(p)
        elif p[0] == "v":
            #Intensive verb identifier, all tenses
            forms = []
            stem = p[2]
            if p[1] == "p":
                for tense in ["P","Impf","F"]:
                    pers = personal[:]
                    if tense == "P": root = stem[1]
                    else: root = stem[3] + "b"
                    if tense == "Impf": root += "a"
                    for i in range(12):
                        if i<6: voice = "A"
                        else: voice = "P"

                        if tense == "P":
                            if stem[0] == "1" and i%6 != 0: pers[i] = "a" + pers[i]
                            elif stem[0] == "3" and i%6 in range(1,5): pers[i] = "i" + pers[i]
                            elif stem[0] in ["3","3i","4"] and i%6 == 5: pers[i] = "u" + pers[i]
                        elif tense == "Impf": pers[::6] = ["m","r"]
                        elif tense == "F":
                            if stem[0] in ["1","2"]:
                                if i%6 in range(1,5): pers[i] = "i" + pers[i]
                                elif i%6 == 5: pers[i] = "u" + pers[i]
                                pers[7] = "eris"
                            else:
                                pers[0] = "m"
                                if i%6 == 0: pers[i] = "a" + pers[i]
                                else: pers[i] = "e" + pers[i]

                        forms.append([root+pers[i],"%s-%s-I-%s"%(persons[i%6],tense,voice)])
                c = stem[0][0]
                if c == "1": end = "are"
                elif c == "3": end = "ere"
                else: end = "re"
                root = stem[1]
                if stem[0][2] == "i": root = root[:-1] #any error at this line probably occurs because nounList is empty
                forms.append([root+end,"P-Inf-A"])
                if c == "3": end = end[:-3]+"i"
                else: stem = end[:-1]+"i"
                forms.append([root+end,"P-Inf-P"])
            elif p[1] == "pf":
                for tense in ["Pf","Ppf","Fp"]:
                    root = stem[2]
                    pers = personal[:6]
                    if tense == "Ppf": pers[0] = "m"
                    for i in range(6):
                        if tense == "Pf": pers = perfects[:]
                        elif tense == "Ppf": pers[i] = "a" + pers[i]
                        elif i != 0: pers[i] = "i" + pers[i]
                        if tense != "Pf": pers[i] = "er" + pers[i]
                        forms.append([root+pers[i],"%s-%s-I-A" % (persons[i%6],tense)])
                        if stem[2][-1] == "v": forms.append([root[:-1]+pers[i][1:],"%s-%s-I-A" % (persons[i%6],tense),"sync"]) #syncopation
                forms.append([stem[2]+"isse","Pf-Inf-A"])
            elif p[1] == "ppl":
                print "parans parandus"
            elif p[1] == "ppp":
                print "paratus paraturus"
            for form in forms:
                if form[0] == term: fins.append([stem,form[1:]])
        elif p[0] == "prn":
            stem = p[1][0]
            if stem == "hic":
                print "hic haec hoc"
            elif stem == "qui":
                print "qui quae quod"
            elif stem == "is":
                print "is ea id"
        elif p[0] == "n":
            stem = p[1]
            ends = sufs[stem[0]][:]
            if stem[3] == "N": [ends[5],ends[8]] = ["a","a"]
            istem = False
            if stem[0] == 3:
                if (stem[1][-1] in ["s","x"] and not (stem[2][-1] in vowels or stem[2][-2] in vowels)): istem = True
                elif len(stem[1]) > len(stem[2]): istem = True
                elif stem[3] == "N" and (nom[-2:] in ["al","ar"] or nom[-1] == ["e"]): istem = True
            for i in range(10):
                end = ends[i]
                if istem and i in [4,5,6,8]:
                    if stem[3] == "N":
                        if i == 4: end = "i"
                        elif i!= 6: end = "i" + end
                    if i == 6: end = "i" + end
                word = stem[2] + end
                if i == 0 or [i,stem[3]] == [3,"N"]: word = stem[1]
                forms.append([word,"%s-%s-%s" % (stem[3],case[i%5],number[i/5])])
            for form in forms:
                if form[0] == term: fins.append([stem,form[1]])
        elif p[0] == "adj":
            print "same thing here"
    if len(fins) > 1: fins.insert(0,"conf") #conflict
    elif len(fins) == 0: fins = ["unknown"]
    final_list.append(fins)
#final_list goes to format.py