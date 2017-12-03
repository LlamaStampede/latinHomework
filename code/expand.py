personal = ["o","s","t","mus","tis","nt", "or","ris","tur","mur","mini","ntur"] #personal endings
perfects = ["i","isti","it","imus","istis","erunt"] #perfect endings
persons = ["1S","2S","3S","1P","2P","3P"] #1st/2nd/3rd Sg/Pl
sums = ["sum","es","est","sumus","estis","sunt"] #sum in the present
sufs = ["placeholder", #so that a word's suffixes can be called via sufs[1/2/3/4/5]
["a","ae","ae","am","a","ae","arum","is","as","is"],
["","i","o","um","o","i","orum","is","os","is"],
["","is","i","em","e","es","um","ibus","es","ibus"],
["","us","ui","um","u","us","uum","ibus","us","ibus"],
["","ei","ei","em","e","es","erum","ebus","es","ebus"]]
case = ["N","G","D","Ac","Ab"]
number = ["S","P"]
vowels = ["a","e","i","o","u"]
def deply(conj,voice):
    return (voice/6 == 1 or conj[-1] != "D") and (voice/6 == 0 or not conj[-1] in ["A","E"])
def infin(c,stem):
    if c == "1": end = "are"
    elif c == "3": end = "ere"
    elif stem[0] == "4E": end = "ire"
    else: end = "re"
    root = stem[1]
    if len(stem[0]) > 1 and stem[0][1] == "i": root = root[:-1] #CAPi
    if c == "s": [root,end] = [stem[3],""]
    pai = root+end #pai = Present Active Infinitive
    if c == "3": end = end[:-3]+"i"
    else: end = end[:-1]+"i"
    ppi = root+end #ppi = Present Passive Infinitive
    return [pai,ppi]

def expand(pts):
    rep = []
    term = pts.pop(0)
    fins = [term] #finalists, all aplicable forms will later be appended
    for p in pts: #p = possibile word ([do,dare,...])
        apls = [term] #apls=aplicable forms
        forms = [] #every form of the word will be added
        if p[0] == "prep": fins.append([term,term,"Prep w/"+p[1][2],p[1][1],""]) #prep & adv (& con) are guaranteed matches
        elif p[0] == "adv": fins.append([term,term,"Adv",p[1][1],""])
        elif p[0] == "conj":
            if term in ["sed","at"]: trn = "but"
            elif term == "autem": trn = "moreover"
            elif term == "tamen": trn = "however"
            elif term == "si": trn = "if"
            elif term in ["tam","ita","sic"]: trn = "so, thus"
            else: trn = "and"

            if term == "ac": dct = "atque"
            else: dct = term
            fins.append([term,dct,"Conj",trn,""])
        elif p[0] == "v": #Intensive verb identifier, all tenses
            stem = p[2]
            if p[1] == "p": #present system (P,Impf,F)
            #this section is only enabled if the term begins with some verb's present stem
                c = stem[0][0] #1st character of conjugation (1,2,3,4)
                for tense in ["P","Impf","F"]:
                    pers = personal[:]
                    if tense in ["P","F"]: root = stem[1]
                    if tense == "Impf" or (tense == "F" and (c in ["1","2"] or stem[0] == "4E")): root = stem[3] + "b" #This line undoes the last one for parabit, monebit, etc.
                    if tense == "Impf": root += "a"
                    for i in range(12): #range(12) means 1st/2nd/3rd Sg/Pl Active/Passive
                        if i<6: voice = "A"
                        else: voice = "P"
                        if stem[0][-1] == "D": voice = "D"

                        if tense == "P":
                            if c in ["3","4"] and i%6 == 5: pers[i] = "u" + pers[i] #capiunt
                            if c in ["3","4"] and i == 7: pers[i] = "e" + pers[i] #avoid "iri" in the 2ndSgP
                            elif c == "3" and not "i" in stem[0] and i%6 in range(1,5): pers[i] = "i" + pers[i] #regit, regunt
                            if c == "1" and i%6 != 0: pers[i] = "a" + pers[i]
                            if stem[0] == "4E":
                                if i in range(1,5): pers[i] = "i" + pers[i]
                                else: pers[i] = "e" + pers[i]

                        elif tense == "Impf":
                            pers[::6] = ["m","r"] #parabam
                        elif tense == "F":
                            if c in ["1","2"] or stem[0] == "4E": #bo bis bit
                                if i%6 in range(1,5): pers[i] = "i" + pers[i]
                                elif i%6 == 5: pers[i] = "u" + pers[i]
                                pers[7] = "eris"
                            else: #ham and 5 eggs
                                pers[::6] = ["m","r"]
                                if i%6 == 0: pers[i] = "a" + pers[i] #ham
                                else: pers[i] = "e" + pers[i] #5 eggs

                        if deply(stem[0],i): #deply ensures that if the verb is deponent, forms gets no active endings
                            forms.append([root+pers[i],"%s-%s-I-%s"%(persons[i%6],tense,voice)])
                            if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-I-%s"%(persons[i%6],tense,voice)])
                [pai,ppi] = infin(c,stem)
                if stem[0][-1] != "D":
                    forms.append([pai,"P-Inf-A"])
                    forms.append([ppi,"P-Inf-P"]) #parari
                else: forms.append([ppi,"P-Inf-D"]) #hortari

                for tense in ["P","Impf"]: #subjunctives
                    root = stem[1]
                    pers = personal[:]
                    pers[::6] = ["m","r"]
                    for i in range(12):
                        if i<6: voice = "A"
                        else: voice = "P"
                        if stem[0][-1] == "D": voice = "D"

                        if tense == "P": #lets eat caviar
                            if stem[0] == "4E": beg = root + "e"
                            else: beg = root
                            if c == "1" and i%6 != 0: pers[i] = "e" + pers[i] #lets
                            else: pers[i] = "a" + pers[i] #eat caviar
                        else: beg = pai #imperfect subjuntives are the p.a.i. plus personal endings
                        if deply(stem[0],i):
                            forms.append([beg+pers[i],"%s-%s-S-%s"%(persons[i%6],tense,voice)])
                            if (root+pers[i])[-3:] == "ris": forms.append([beg+pers[i][:-2]+"e","%s-%s-S-%s" % (persons[i%6],tense,voice)]) #alternative 2ndPlP form (looks like p.a.i. in the present)


            elif p[1] == "pf": #perfect system (Pf,PPf,Fp). Also, note that no deponents have perfect active forms
                for tense in ["Pf","Ppf","Fp"]:
                    root = stem[2] #perfect stem (parav,monu,dux)
                    pers = personal[:6]
                    if tense == "Ppf": pers[0] = "m" #paraveram
                    for i in range(6): #range(6) is 1st/2nd/3rd Sg/Pl Active
                        if tense == "Pf": pers = perfects[:] #i isti it
                        elif tense == "Ppf": pers[i] = "a" + pers[i] #rexeramus
                        elif i != 0: pers[i] = "i" + pers[i] #rexerimus
                        if tense != "Pf": pers[i] = "er" + pers[i] #rexeramus and rexerimus

                        [la,lb] = [1,1]
                        if pers[i][-3:] == "ris": la += 1
                        if stem[2][-1] == "v" and pers[i] != "i": lb += 1
                        if stem[0][0] == "4": lb += 1
                        for a in range(la):
                            for b in range(lb):
                                end = pers[i]
                                if a == 1: end = pers[i][:-2] + "e"
                                if b == 0: beg = root
                                else: beg = root[:-1]
                                if b == 1 and pers[i] != "i": end = end[1:]
                                forms.append([beg+end,"%s-%s-I-A" % (persons[i%6],tense)])

                pfi = stem[2]+"isse"
                lb = 1
                pfi = [] #pfi = PerFect active Infinitive
                lb = 1
                if stem[2][-1] == "v": lb += 1
                if stem[0][0] == "4": lb += 1
                for b in range(lb):
                    end = "isse"
                    if b == 0: beg = stem[2]
                    else: beg = stem[2][:-1]
                    if b == 1: end = "sse"
                    pfi.append(beg+end)
                for i in pfi:
                    forms.append([i,"Pf-I-A"])

                for tense in ["Pf","Ppf"]: #subjunctives
                    pers = personal[:6]
                    pers[0] = "m"
                    for i in range(6):
                        if tense == "Pf":
                            roots = []
                            lb = 1
                            if stem[2][-1] == "v": lb += 1
                            if stem[0][0] == "4": lb += 1
                            for b in range(lb):
                                end = "eri"
                                if b == 0: beg = stem[2]
                                else: beg = stem[2][:-1]
                                if b == 1: end = end[1:]
                                roots.append(beg + end) #pf subjunctive perfect stem + "eri" + personal endings
                        else: roots = pfi #ppf subjunctives = p.f.i. + personal endings
                        for root in roots:
                            forms.append([root+pers[i],"%s-%s-S-A"%(persons[i%6],tense)])
                            if pers[i][-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-S-A"%(persons[i%6],tense)]) #alt 2-Pl...P form
            elif p[1] == "ppl": #All participles, enabled if term contains impf stem (CAPIEbam) or p.p.p. stem (CAPTus)
                for n in range(4): #0:PPplA 1:FPplP 2:FPplA 3:PfPplP
                    nom = stem[[3,4][n/2]] + ["ns","nd","ur",""][n] #0:parans 1:parand(us-a-um) 2:paratur(us-a-um) 3:parat(us-a-um)
                    root = stem[[3,4][n/2]] + ["nt","nd","ur",""][n] #0:parant(is) 1:parand(i-ae) 2:paratur(i-ae) 3:parat(i-ae)
                    if stem[0] == "4E" and n in range(2): root = root[:-2]+"e"+root[-2:]
                    voice = ["A","P"][n%2] #0,2:A 1,3:P
                    for g in ["M","F","N"]:
                        for i in range(10): #range(10) = Nom/Gen/Dat/Acc/Abl Sg/Pl
                            if i%5 == 3 and g == "N": i -= 3 #Neuter Golden Rule 1: Nom=Acc
                            end = sufs[2][i] #2nd Declension
                            if g == "N" and i == 5: end = "a" #Neuter Golden Rule 2: Nom/Acc "a" in the plural
                            if n == 0:
                                end = sufs[3][i] #3rd Declension
                                if i == 6 or (g == "N" and i == 5): end = "i" + end #parantium
                                if i == 4: end = "i" #All participles are strong i-stems - paranti (AblSg)
                                word = stem[2] + end
                            elif g == "F": end = sufs[1][i] #2-1-2 is 1st Decl in the feminine
                            if n != 0 and i == 0: end = {"M":"us","F":"a","N":"um"}[g] #us-a-um in nom
                            if i == 0: word = nom + end #All (nominative/neuter-accusative) singulars
                            else: word = root + end #Everything else
                            if not "-" in word: forms.append([word, "%s-Ppl-%s/-%s-%s-%s" % (["P","F","F","Pf"][n], voice,g,case[i%5],number[i/5])])
            elif p[1] == "sum": #For verbs that come from sum (possum,posse) in the present
                pai = stem[3]
                if len(stem[1]) != 0: pot = stem[1]
                else: pot = "-"
                for tense in ["P","Impf","F"]:
                    pers = personal[:6]
                    if tense == "Impf": pers[0] = "m"
                    for i in range(6):
                        root = pot
                        if tense == "P": end = sums[i]
                        else:
                            end = "er"
                            if tense == "Impf": end += "a"
                            elif i != 0: end += "i"
                            end += pers[i]
                        if end[0] == "s" and pot[-1] == "t": root = pot[:-1] + "s" #possum,potest
                        elif pot == "-": root = ""
                        forms.append([root+end,"%s-%s-I-A" % (persons[i], tense)])

                        if tense == "P": #Actually these are subjunctives
                            pers[0] = "m"
                            if pot[-1] == "t": root = pot[:-1] + "s"
                            elif pot == "-": root = ""
                            forms.append([root+"si"+pers[i],persons[i]+"-P-S-A"])
                            forms.append([pai+pers[i],persons[i]+"-Impf-S-A"])
                forms.append([pai,"P-Inf-A"])
        elif p[0] == "prn": #This section not written yet
            stem = p[1][0]
            if stem == "hic":
                print "hic haec hoc"
            elif stem == "qui":
                print "qui quae quod"
            elif stem == "is":
                print "is ea id"
        elif p[0] == "n":
            stem = p[1]
            nom = stem[1]
            ends = sufs[stem[0]][:] #Specific to the word's declension
            if stem[3] == "N" and stem[0] == 4: ends[5] = "ua" #4th Declension neuter plural
            elif stem[3] == "N": ends[5] = "a" #N.G.R.2
            istem = False
            if stem[0] == 3:
                if len(stem[2]) > 1 and (stem[1][-1] in ["s","x"] and not (stem[2][-1] in vowels or stem[2][-2] in vowels)): istem = True #base in 2 consonants
                elif len(stem[1]) > len(stem[2]): istem = True #monosyllabic (not actually functional, idk how to)
                elif stem[3] == "N" and (nom[-2:] in ["al","ar"] or nom[-1] == ["e"]): istem = True #neuter ending in -al,-ar,-e
            for i in range(10):
                if i%5 == 3 and stem[3] == "N": i -= 3 #N.G.R.1
                end = ends[i]
                if istem and i in [4,5,6]: #AblSg, Nom/AccPl, GenPl
                    if stem[3] == "N":
                        if i == 4: end = "i" #mari
                        elif i == 5: end = "i" + end #maria
                    if i == 6: end = "i" + end #marium
                word = stem[2] + end
                if i == 0: word = stem[1] #(nom/n-acc) sg

                forms.append([word,"%s-%s-%s" % (stem[3],case[i%5],number[i/5])]) #gender,case,number
        elif p[0] == "adj":
            stem = p[1]
            [decl,root,masc,neut,trn] = stem[:]
            #print "rrroot:",root
            #print stem, "()"
            for gen in ["M","F","N"]:
                if decl[0] == "3": ends = sufs[3][:]
                elif gen == "F": ends = sufs[1][:]
                else: ends = sufs[2][:]
                if gen == "N": ends[5] = "a" #N.G.R.2

                if gen == "N": nom = neut
                elif gen == "F" and decl in ["212","33"]: nom = root + [0,0,"a","is"][int(decl[0])]
                else: nom = masc

                istem = False
                if decl[0] == "3": #!
                    if len(nom) > 1 and (nom[-1] in ["s","x"] and not (root[-1] in vowels or root[-2] in vowels)): istem = True #base in 2 consonants
                    elif len(nom) > len(root): istem = True #monosyllabic (not actually functional, idk how to)

                for i in range(10):
                    if i%5 == 3 and gen == "N": i -= 3 #N.G.R.1
                    end = ends[i]
                    if i == 5 and gen == "N": end = "a"
                    if istem and i in [4,5,6]: #AblSg, Nom/AccPl, GenPl
                        if gen == "N" and i == 5: end = "i" + end #sapientia
                        if i == 4: end = "i" #sapienti
                        if i == 6: end = "i" + end #sapientium
                    word = root + end
                    if i == 0: word = nom

                    if i < 5 or len(trn) < 4 or trn[-4:] != "(pl)": forms.append([word,"%s-%s-%s" % (gen,case[i%5],number[i/5])]) #gender-case-number
        for form in forms:
            #print form
            if form[0] == term: apls.append([stem,form[1]]) #checks if term and form spelled the same
        if len(apls) != 1:
            difs = [] #for conflicting parsings (dat/abl pl)
            ld = 3
            if p[0] == "v": ld = 6 #verbs can have at most 6 (participles). nouns only ever have 3 (gender,case,number)
            for i in range(ld):
                difs.append([])

            prsf = "" #prsf = Final Parsing (will include "   "-blankspaces for unknown values)
            for apl in apls[1:]: #aplicable forms
                prs = apl[1].split("-")
                #print prs
                for l in range(len(prs)):
                    difs[l+ld-len(prs)].append(prs[l]) #separating parsings into different columns for comparison
            for l in difs: #l is a value location (Gender,Case,Tense,etc.)
                value = True
                cur = 0 #cur = current value (sg,masc,dat,fem,gen,etc.)
                value = True
                for x in l:
                    if x != l[0]: value = False
                if len(l) != 0:
                    if value: prsf += l[0] + "-" #if value is certain
                    else: prsf += "   -" #if value is indefinite
                    if l[0][-1] == "/": prsf = prsf[:-1] #eliminates dash after slash: ...-A/-M-...
            prsf = prsf[:-1] # eliminates extra dash: ...-G-P-
            stem = apls[1][0]
            if p[0] == "v": [pai,ppi] = infin(stem[0][0],stem)
            if p[0] == "n": dct = [stem[1],stem[2]+sufs[stem[0]][1]] #rex,regis
            elif p[0] == "adj":
                if decl == "212": dct = [masc,root+"a",neut]
                else: dct = [root+"is"]
                if decl in ["32","33"]: dct.append(neut)
                if decl in ["31","33"]: dct.insert(0,masc)
            elif stem[0][-1] == "D": dct = [stem[1]+"or",ppi,stem[4]+"us sum","-"] #sequor,sequi,secutus sum,-
            else: dct = [stem[1]+"o",pai,stem[2]+"i",stem[4]+"us"] #paro,parare,paravi,paratus
            if stem[0] == "sum":
                dct[0] = stem[1]+"sum"
                dct[3] = "-"
            elif stem[0] == "4E":
                dct[0] = dct[0][:-1] + "eo"
            dct = ",".join(dct)
            fins.append([term,dct,prsf,stem[-1],""]) #["regum","rex,regis","M-G-S","to rule",""]
    if len(fins) > 2: #Conflict: Multiple Possibilities (ie.rei from res,rei:thing or reus,rei:defendant)
        cur = fins[1][1]
        for fin in fins[1:]:
            if fin[1] != cur: cur = ""
        if cur == "": dfn = ""
        else: dfn = fins[1][3]
        final = [term,cur,"",dfn,""] #leaves blank spaces b/c origin unknown
        words = [fins[0]]
        for fin in fins[1:]:
            words.append([fin[1],fin[2]])
        rep = ["multi"]+words #error reporting is notified
    elif len(fins) == 1: #Error: Term Unknown (new word not in glossaries)
        final = [term,"","","",""] #leaves blank spaces b/c origin unknown
        rep = ["unknown",term] #error reporting is notified
    else: final = fins[1] #when program is running smoothly
    return [final,rep]