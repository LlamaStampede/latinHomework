# Prelude
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

verbList = glossary("verbs.txt")
prepList = glossary("preps.txt")
advList = glossary("adverbs.txt")
nounList = glossary("nouns.txt")

ex_terms = raw_input("Enter a term: ").split(" ") # You might need to change this to input() for your python version

preps = []
for prep in prepList:
    if len(prep) == 1:
        phase = prep[0]
    else:
        preps.append([prep[0].lower(),prep[1],phase])
advs = []
for adv in advList:
    advs.append(adv[::-1])


#to do: non-passive, "virtual deponent", preterates
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
        elif conj[0] in ["3","4"]: impf += "e"

        if dep: ppp = secondary
        elif verb[3] == "-": ppp = "-"
        else: ppp = verb[3][:-2]

        return [conj,primary,secondary,impf,ppp,trn]
    elif verb[0] == "-":
        if verb[3] == "-":
            ppl = "-"
        else:
            ppl = verb[3][:-2]
        return ["3P","-",verb[2][:-1],"-",ppl,trn] #preterate
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

def decl(noun):
    decls = {"ae":1,"i":2,"is":3,"us":4,"ei":5}
    pls = {"arum":1,"orum":2,"um":3,"uum":4,"erum":5}
    noms = [0,1,2,2,2,2]
    [nom,gen,gend,trn] = noun
    if gend == "n": noms[4] = 1
    if gen[-1] == "m": sufs = pls
    else: sufs = decls
    for s in sufs:
        if s == gen[-len(s):]: suf = s
    if gen == "-" + suf: root = nom[:-noms[sufs[suf]]]
    elif "-" in gen:
        mark = 0
        for l in range(len(nom)):
            if nom[l] == gen[1]: mark = l
        if mark == 0: mark = len(nom)-noms[sufs[suf]]
        root = nom[:mark] + gen[1:-len(suf)]
    else: root = gen[:-len(suf)]
    return [sufs[suf],nom,root,gend.upper(),trn]

nstems = []
for noun in nounList:
    nstems.append(decl(noun))


#Phase: Assemble
pos = []
for term in ex_terms:
    pos.append([term])

    adv = inc(term,advs) #in reality adv = (is term an adverb?)
    if adv[0]: pos[-1].append(["adv",adv[1]])
    prep = inc(term,preps)
    if prep[0]: pos[-1].append(["prep",prep[1]])

    for stem in vstems:
        if stem[2][-1] == "v": addit = 1
        else: addit = 0
        if stem[1] == term[:len(stem[1])]: pos[-1].append(["v","p",stem])
        if stem[0][-1] != "D" and stem[2] != "-" and stem[2][:-addit] == term[:len(stem[2])-1]: pos[-1].append(["v","pf",stem])
        if stem[3] == term[:len(stem[3])] or stem[4] == term[:len(stem[4])]: pos[-1].append(["v","ppl",stem])

    prns = [["hic","this",5],["qui","-",6],["is","weak dem",3]] #id, def, max length
    pres = [["h"],["qu","cui"],["i","e"]] #prefixes (word-beginnings)
    for i in range(len(pres)):
        for pre in pres[i]:
            if len(term) <= prns[i][2] and term[:len(pre)] == pre: pos[-1].append(["prn",prns[i][:2]])

    #nouns
    for stem in nstems:
        if stem[2] == term[:len(stem[2])] or term == stem[1]: pos[-1].append(["n",stem])

    #adjectives

for pts in pos:
    for p in pts[1:]:
        print p


#Phase: Select
final_list = []
report = []
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
def deply(conj,voice):
    return (conj[-1] == "D" and voice/6 == 1) or conj[-1] != "D"
print pos, "KL"
for pts in pos: #possible terms
    term = pts.pop(0)
    fins = [term] #finalists
    for p in pts: #possibility
        apls = []
        forms = []
        if p[0] == "prep": fins.append([term,term,"Prep w/"+p[1][2],p[1][1],""])
        elif p[0] == "adv": fins.append([term,term,"Adv",p[1][1],""])
        elif p[0] == "v":
            #Intensive verb identifier, all tenses
            stem = p[2]
            if p[1] == "p":
                c = stem[0][0]
                for tense in ["P","Impf","F"]:
                    pers = personal[:]
                    if tense in ["P","F"]: root = stem[1]
                    if tense == "Impf" or c in ["1","2"]: root = stem[3] + "b"
                    if tense == "Impf": root += "a"
                    for i in range(12):
                        if i<6: voice = "A"
                        else: voice = "P"
                        if stem[0][-1] == "D": voice = "D"

                        if tense == "P":
                            if c == "1" and i%6 != 0: pers[i] = "a" + pers[i]
                            elif c in ["3","4"] and i == 7: pers[i] = "e" + pers[i]
                            elif c == "3" and not "i" in stem[0] and i%6 in range(1,5): pers[i] = "i" + pers[i]
                            elif c in ["3","4"] and i%6 == 5: pers[i] = "u" + pers[i]

                        elif tense == "Impf":
                            pers[::6] = ["m","r"]
                        elif tense == "F":
                            if c in ["1","2"]:
                                if i%6 in range(1,5): pers[i] = "i" + pers[i]
                                elif i%6 == 5: pers[i] = "u" + pers[i]
                                pers[7] = "eris"
                            else:
                                pers[::6] = ["m","r"]
                                if i%6 == 0: pers[i] = "a" + pers[i]
                                else: pers[i] = "e" + pers[i]

                        if deply(stem[0],i):
                            forms.append([root+pers[i],"%s-%s-I-%s"%(persons[i%6],tense,voice)])
                            if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-I-%s"%(persons[i%6],tense,voice)])
                if c == "1": end = "are"
                elif c == "3": end = "ere"
                else: end = "re"
                root = stem[1]
                if len(stem[0]) > 1 and stem[0][1] == "i": root = root[:-1]
                pai = root+end
                if stem[0][-1] != "D": forms.append([root+end,"P-Inf-A"])
                if c == "3": end = end[:-3]+"i"
                else: end = end[:-1]+"i"
                if stem[0][-1] != "D": forms.append([root+end,"P-Inf-P"])
                else: forms.append([root+end,"P-Inf-D"])

                for tense in ["P","Impf"]:
                    root = stem[1]
                    pers = personal[:]
                    pers[::6] = ["m","r"]
                    for i in range(12):
                        if i<6: voice = "A"
                        else: voice = "P"
                        if stem[0][-1] == "D": voice = "D"

                        if tense == "P":
                            if c == "1" and i%6 != 0: pers[i] = "e" + pers[i]
                            else: pers[i] = "a" + pers[i]
                        else: root = pai
                        if deply(stem[0],i):
                            forms.append([root+pers[i],"%s-%s-S-%s"%(persons[i%6],tense,voice)])
                            if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-S-%s"%(persons[i%6],tense,voice)])


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
                        if pers[i][-3:] == "ris": forms.append([(root+pers[i])[:-2]+"e","%s-%s-I-A"%(persons[i%6],tense)])
                        if stem[2][-1] == "v" and i != 0: forms.append([root[:-1]+pers[i][1:],"%s-%s-I-A" % (persons[i%6],tense)]) #syncopation
                        if pers[i][-3:] == "ris" and stem[2][-1] == "v": forms.append([root[:-1]+pers[i][1:-2]+"e","%s-%s-I-A" % (persons[i%6],tense)])

                pfi = stem[2]+"isse"
                forms.append([pfi,"Pf-Inf-A"])

                for tense in ["Pf","Ppf"]:
                    pers = personal[:6]
                    pers[0] = "m"
                    for i in range(6):
                        if tense == "Pf": root = stem[2] + "eri"
                        else: root = pfi
                        forms.append([root+pers[i],"%s-%s-S-A"%(persons[i%6],tense)])
                        if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-S-A"%(persons[i%6],tense)])
            elif p[1] == "ppl":
                for n in range(4):
                    nom = stem[[3,4][n/2]] + ["ns","nd","ur",""][n]
                    root = stem[[3,4][n/2]] + ["nt","nd","ur",""][n]
                    voice = ["A","P"][n%2]
                    for g in ["M","F","N"]:
                        for i in range(10):
                            if i%5 == 3 and g == "N": i -= 3
                            end = sufs[2][i]
                            if stem[3] == "N" and i == 5: end = "a"
                            if n == 0:
                                end = sufs[3][i]
                                if i == 6 or (g == "N" and i == 5): end = "i" + end
                                if i == 4: end = "i"
                                word = stem[2] + end
                            elif g == "F": end = sufs[1][i]
                            if n != 0 and i == 0: end = {"M":"us","F":"a","N":"um"}[g]
                            if i == 0: word = nom + end
                            else: word = root + end
                            forms.append([word,"%s-Ppl-%s/-%s-%s-%s" % (["P","F","F","Pf"][n],voice,g,case[i%5],number[i/5])])
        elif p[0] == "prn":
            stem = p[1][0]
            if stem == "hic":
                print "hic haec hoc"
            elif stem == "qui":
                print "qui quae quod"
            elif stem == "is":
                print "is ea id"
        elif p[0] == "n":
            print forms
            stem = p[1]
            ends = sufs[stem[0]][:]
            if stem[3] == "N" and stem[0] == 4: ends[5] = "ua"
            elif stem[3] == "N": ends[5] = "a"
            istem = False
            if stem[0] == 3:
                if (stem[1][-1] in ["s","x"] and not (stem[2][-1] in vowels or stem[2][-2] in vowels)): istem = True
                elif len(stem[1]) > len(stem[2]): istem = True
                elif stem[3] == "N" and (nom[-2:] in ["al","ar"] or nom[-1] == ["e"]): istem = True
            for i in range(10):
                if i%5 == 3 and stem[3] == "N": i -= 3
                end = ends[i]
                if istem and i in [4,5,6]:
                    if stem[3] == "N":
                        if i == 4: end = "i"
                        elif i == 5: end = "i" + end
                    if i == 6: end = "i" + end
                word = stem[2] + end
                if i == 0 or [i,stem[3]] == [3,"N"]: word = stem[1]

                forms.append([word,"%s-%s-%s" % (stem[3],case[i%5],number[i/5])])
        elif p[0] == "adj":
            print "same thing here"
        if p[0] in ["v","n"]:
            for form in forms:
                print form
                if form[0] == term: apls.append([stem,form[1]])
            difs = [[],[],[],[],[],[]]
            for i in range({"n":3,"v":6}[p[0]]):
                difs.append([])
            prsf = ""
            for apl in apls:
                prs = apl[1].split("-")
                print prs
                for l in range(len(prs)):
                    difs[l+6-len(prs)].append(prs[l])
            if len(apls) != 0:
                for l in difs:
                    value = True
                    cur = 0
                    for x in l:
                        if cur == 0: cur = x
                        elif cur != x:
                            value = False
                            report.append([term,difs])
                    if value and len(l) != 0: prsf += l[0] + "-"
                    elif len(l) != 0: prsf += "   -"
                    if len(l) != 0 and l[0][-1] == "/": prsf = prsf[:-1]
                prsf = prsf[:-1] # eliminates extra dash
                stem = apls[0][0]
                if p[0] == "n": dct = stem[1]+","+stem[2]+sufs[stem[0]][1]
                else: dct = stem[1]+"o,"+pai+","+stem[2]+"i,"+stem[4]+"us"
                fins.append([term,dct,prsf,stem[{"n":4,"v":5}[p[0]]],""])
                print "F:", fins, "\F"
    if len(fins) > 2:
        final_list.append([term,"","","",""])
        report.append[fins]
    elif len(fins) == 1:
        final_list.append([term,"","","",""])
        report.append([term,"unknown"])
    final_list.append(fins)
print final_list
#final_list goes to format.py