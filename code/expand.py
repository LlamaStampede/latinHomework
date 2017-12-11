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
hics = [["ic","aec","oc"],
["uius","uius","uius"],
["uic","uic","uic"],
["unc","anc","oc"],
["oc","ac","oc"],
["i","ae","aec"],
]
cases = ["N","G","D","Ac","Ab"]
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
    if stem[0] == "3F": end = "re"
    pai = root+end #pai = Present Active Infinitive
    if stem[0] == "sum":
        if len(stem[1]) > 0 and stem[1][-1] == "t": pai = stem[1][:-1] + "sse"
        else: pai = stem[1] + "esse"
    if c == "3": end = "i"
    else: end = end[:-1]+"i"
    if stem[0] == "3F": end = "ri"
    ppi = root+end #ppi = Present Passive Infinitive
    if stem[1] == "faci": ppi = "fieri"
    return [pai,ppi]

def present(stem):
    forms = []
    [conj,primary,secondary,impf,ppp,dfn] = stem
    c = conj[0]
    for tense in ["P","Impf","F"]:
        for i in range(12): #range(12) means 1st/2nd/3rd Sg/Pl Active/Passive
            if i<6: voice = "A"
            else: voice = "P"
            if stem[0][-1] == "D": voice = "D"
            
            bam = tense == "Impf" or (tense == "F" and (c in ["1","2"] or conj == "4E"))
            root = primary
            if bam: root = impf + "b"#This line undoes the last one for parabit, monebit, etc.
            fio = primary == "faci" and i >= 6
            if fio:
                root = "fi"
                if bam: root = "fieb"
                i -= 6
            if tense == "Impf": root += "a"

            end = personal[i]
            if tense == "P":
                if c in ["3","4"]:
                    if i%6 == 5: end = "u" + end #capiunt
                    if not (conj == "3F" and i in [1,2,4,7,8]):
                        if i == 7: end = "eris" #avoid "iri" in the 2ndSgP
                        elif c == "3" and not "i" in conj and i%6 in range(1,5): end = "i" + end #regit, not regunt
                if c == "1" and i%6 != 0: end = "a" + end
                if stem[0] == "4E":
                    if i in range(1,5): end = "i" + end
                    else: end = "e" + end

            elif tense == "Impf":
                if i%6 == 0: end = ["m","r"][i/6] #parabam
            elif tense == "F":
                if c in ["1","2"] or conj == "4E": #bo bis bit
                    if i%6 in range(1,5): end = "i" + end
                    elif i%6 == 5: end = "u" + end
                    if i == 7: end = "eris"
                else: #ham and 5 eggs
                    if i%6 == 0: end = ["m","r"][i/6]
                    if i%6 == 0: end = "a" + end #ham
                    else: end = "e" + end #5 eggs

            if deply(conj,i): #deply ensures that if the verb is deponent, forms gets no active endings
                forms.append([root+end,"%s-%s-I-%s"%(persons[i%6],tense,voice)])
                if (root+end)[-3:] == "ris": forms.append([(root+end)[:-2]+"e","%s-%s-I-%s"%(persons[i%6],tense,voice)])
    [pai,ppi] = infin(c,stem)
    if stem[0][-1] != "D":
        forms.append([pai,"P-Inf-A"])
        forms.append([ppi,"P-Inf-P"]) #parari
    else: forms.append([ppi,"P-Inf-D"]) #hortari

    for tense in ["P","Impf"]: #subjunctives
        for i in range(12):
            if i<6: voice = "A"
            else: voice = "P"
            if stem[0][-1] == "D": voice = "D"
            
            root = primary
            end = personal[i]
            if i%6 == 0: end = ["m","r"][i/6]
            
            fio = primary == "faci" and i >= 6
            if fio:
                root = "fi"
                i -= 6
                if i == 0: end = "m"

            if tense == "P": #lets eat caviar
                if stem[0] == "4E": root = root + "e"
                if c == "1" and i%6 != 0: end = "e" + end #lets
                else: end = "a" + end #eat caviar
            else: root = pai #imperfect subjuntives are the p.a.i. plus personal endings
            if fio and tense == "Impf": root = "fiere"
            if deply(stem[0],i):
                forms.append([root+end,"%s-%s-S-%s"%(persons[i%6],tense,voice)])
                if (root+end)[-3:] == "ris": forms.append([(root+end)[:-2]+"e","%s-%s-S-%s" % (persons[i%6],tense,voice)]) #alternative 2ndPlP form (looks like p.a.i. in the present)

    if deply(stem[0],0):
        forms.append([pai[:-2],"2S-P-Imp-A"])
        if c == "3" and conj != "3F": forms.append([pai[:-3]+"ite","2P-P-Imp-A"])
        else: forms.append([pai[:-2]+"te","2P-P-Imp-A"])
    return forms
def perfect(stem):
    forms = []
    for tense in ["Pf","Ppf","Fp"]:
        root = stem[2] #perfect stem (parav,monu,dux)
        for i in range(6): #range(6) is 1st/2nd/3rd Sg/Pl Active
            end = personal[i]
            if i == 0: end = "m"
            if tense == "Pf": end = perfects[i] #i isti it
            elif tense == "Ppf": end = "a" + end #rexeramus
            elif i != 0: end = "i" + end #rexerimus
            if tense != "Pf": end = "er" + end #rexeramus and rexerimus

            [la,lb] = [1,1] #syncopation, alternative forms
            if end[-3:] == "ris": la += 1
            if stem[2][-1] == "v" and end != "i": lb += 1
            if stem[0][0] == "4": lb += 1
            for a in range(la):
                for b in range(lb):
                    fin = end
                    if a == 1: fin = fin[:-2] + "e"
                    if b == 0: beg = root
                    else: beg = root[:-1]
                    if b == 1 and end != "i": fin = fin[1:]
                    forms.append([beg+fin,"%s-%s-I-A" % (persons[i%6],tense)])

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
        for i in range(6):
            end = personal[i]
            if i == 0: end = "m"
            if tense == "Pf":
                roots = []
                lb = 1
                if stem[2][-1] == "v": lb += 1
                if stem[0][0] == "4": lb += 1
                for b in range(lb):
                    mid = "eri"
                    if b == 0: beg = stem[2]
                    else: beg = stem[2][:-1]
                    if b == 1: mid = mid[1:]
                    roots.append(beg + mid) #pf subjunctive perfect stem + "eri" + personal endings
            else: roots = pfi #ppf subjunctives = p.f.i. + personal endings
            for root in roots:
                forms.append([root+end,"%s-%s-S-A"%(persons[i%6],tense)])
                if (root+end)[-3:] == "ris": forms.append([(root+end)[:-2]+"e","%s-%s-S-A"%(persons[i%6],tense)]) #alt 2-Pl...P form
    return forms
def case(stem): #nouns, pronouns, adjectives, participles
    forms = []
    [decl,nom,root,gender,pos] = stem
    ends = sufs[decl][:] #Specific to the word's declension
    if [decl,gender] == [4,"N"]: ends[5] = "ua" #4th Declension neuter plural
    elif stem[3] == "N": ends[5] = "a" #N.G.R.2
    istem = False
    if decl == 3:
        if len(root) > 1 and (nom[-1] in ["s","x"] and not (root[-1] in vowels or root[-2] in vowels)): istem = True #base in 2 consonants
        elif len(nom) > len(root): istem = True #monosyllabic (not actually functional, idk how to)
        elif gender == "N" and (nom[-2:] in ["al","ar"] or nom[-1] == ["e"]): istem = True #neuter ending in -al,-ar,-e
    if nom in ["mater","pater","frater"]: istem = False
    for i in range(10): #todo (istem ab sg rules)
        if i%5 == 3 and gender == "N": i -= 3 #N.G.R.1
        end = ends[i]
        if root == "qu":
            if i in [1,2]: root = "cu"
            if [i,gender] in [[5,"N"],[0,"F"]]: end = "ae"
            if i in [7,9]: end = "ibus"
        if pos in ["prn","unus"] and i in [1,2]: end = [0,"ius","i"][i]
        if [root,i,gender] == ["qu",3,"M"]: end = "em"
        if root == "h" and i < 6: end = hics[i][{"M":0,"F":1,"N":2}[gender]]
        
        if istem: #AblSg, Nom/AccPl, GenPl
            if gender == "N" and i == 5:end = "i" + end #maria, sapientia
            if (gender == "N" or pos == "adj") and i == 4: end = "i" #mari, sapienti
            if i == 6: end = "i" + end #marium, sapientium
        
        word = root + end
        if i == 0: word = nom #(nom/n-acc) sg
        if word == "aliius": word = "alius"
        if [root,i,gender] == ["e",0,"N"]: word = "id"
        
        case = cases[i%5]
        if [case,gender] == ["N","N"]: case = "   "
        if pos != "adj" or i < 5:forms.append([word,"%s-%s-%s" % (gender,case,number[i/5])]) #gender-case-number #or len(trn) < 4 or trn[-4:] != "(pl)"
        if root == "e" and (i in [7,9] or [gender,i] == ["M",5]): forms.append(["i"+end,"%s-%s-%s"%(gender,cases[i%5],number[i/5])])
        if root == "qu" and i == 0:
            if gender == "N": word = "quid"
            else: word = "quis"
            forms.append([word,"%s-%s-%s"%(gender,cases[i%5],number[i/5])])
    return forms

def expand(pts):
    rep = []
    term = pts.pop(0)
    fins = [term] #finalists, all aplicable forms will later be appended
    for p in pts: #p = possibile word ([do,dare,...])
        apls = [term] #apls=aplicable forms
        forms = [] #every form of the word will be added
        if p[0] == "prep":
            if term == "a": dct = "ab"
            elif term == "e": dct = "ex"
            else: dct = term
            fins.append([term,dct,"Prep w/"+p[1][2],p[1][1],""]) #prep & adv (& con) are guaranteed matches
        elif p[0] == "adv": fins.append([term,term,"Adv",p[1][1],""])
        elif p[0] == "conj": #trn is the conj equivalent of dfn
            if term in ["sed","at"]: trn = "but"
            elif term == "autem": trn = "moreover"
            elif term == "tamen": trn = "however"
            elif term == "aut": trn = "or"
            elif term == "neque": trn = "neither, nor"
            elif term == "si": trn = "if"
            elif term in ["tam","ita","sic"]: trn = "so, thus"
            elif term in ["enim","nam"]: trn = "for"
            elif term in ["ut"]: trn = "."
            elif term == "dum": trn = "while/until"
            elif term == "cum": trn = "when"
            elif term == "quod": trn = "because"
            else: trn = "and"

            if term == "ac": dct = "atque"
            else: dct = term
            fins.append([term,dct,"Conj",trn,""])
        elif p[0] == "pers":
            letter = term[0]
            person = {"e":1,"m":1,"t":2,"s":3,"n":4,"v":5}[letter]
            num = number[(person-1)/3]
            if person == 3: num = "   "
            for i in range(5):
                if person == 1: end = ["go","ei","ihi","e","e"][i]
                elif person in [2,3]: end = ["u","ui","ibi","e","e"][i]
                else: end = ["os","ostrum","obis","os","obis"][i]
                word = letter+end
                if [i,person] != [0,3]: forms.append([word,"   -%s-%s"%(cases[i],num)])
                if [i,person] == [1,4]: forms.append(["nostri","   -G-P"])
                if [i,person] == [1,5]: forms.append(["vestrum","   -G-P"])
            person = [3,1,2][person%3]
            dct = [0,"ego,mihi","tu,tui","-,sui"][person].split(",")
            dfn = "%i%s person prn"%(person,["st","nd","rd"][person-1])
            stem = [dct,dfn]
        elif p[0] == "v": #Intensive verb identifier, all tenses
            stem = p[2]
            if p[1] == "p": #present system (P,Impf,F)
                forms += present(stem)
            elif p[1] == "pf": #perfect system (Pf,PPf,Fp)
                forms += perfect(stem)
            elif p[1] == "ppl": #All participles, activated if term contains impf stem (CAPIEbam) or p.p.p. stem (CAPTus)
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
                            if not "-" in word: forms.append([word, "%s-Ppl-%s/-%s-%s-%s" % (["P","F","F","Pf"][n], voice,g,cases[i%5],number[i/5])])
            elif p[1] == "sum": #For verbs that come from sum (possum,posse) in the present
                pai = stem[3]
                if len(stem[1]) != 0: pot = stem[1]
                else: pot = "-"
                for tense in ["P","Impf","F"]:
                    for i in range(6):
                        root = pot
                        if tense == "P": end = sums[i]
                        else:
                            end = "er"
                            if tense == "Impf": end += "a"
                            elif i != 0: end += "i"
                            if [i,tense] == [0,"Impf"]: end += "m"
                            else: end += personal[i]
                        if end[0] == "s" and pot[-1] == "t": root = pot[:-1] + "s" #possum,potest
                        elif pot == "-": root = ""
                        forms.append([root+end,"%s-%s-I-A" % (persons[i], tense)])

                        if tense == "P": #Actually these are subjunctives
                            end = personal[i]
                            if i == 0: end = "m"
                            if pot[-1] == "t": root = pot[:-1] + "s"
                            elif pot == "-": root = ""
                            forms.append([root+"si"+end,persons[i]+"-P-S-A"])
                            forms.append([pai+end,persons[i]+"-Impf-S-A"])
                forms.append([pai,"P-Inf-A"])
        elif p[0] in ["prn","unus"]: #This section not written yet
            stem = p[1]
            [masc,dfn] = stem
            masc = p[1][0]
            for gender in ["M","F","N"]:
                if masc[-2:] == "us": root = masc[:-2]
                elif masc[-2:] == "er": root = masc[:-2] + "r"
                elif masc[-1] == "e": root = masc[:-1]
                if masc == "is": root = "e"
                if masc == "hic": root = "h"
                if masc == "qui": root = "qu"
                
                if gender == "F": decl = 1
                else: decl = 2
                
                if gender == "M": nom = masc
                if gender == "N":
                    if root in ["ali","ill","ist"]: nom = root + "ud"
                    elif root == "qu": nom = "quod"
                    else: nom = root + "um"
                    neut = nom
                if gender == "F": nom = root + "a"
                
                forms += case([decl,nom,root,gender,p[0]])
        elif p[0] == "n":
            stem = p[1]
            forms += case(stem[:4]+["n"])
        elif p[0] == "adj":
            stem = p[1]
            [decl,root,masc,neut,trn] = stem[:]
            for gen in ["M","F","N"]:
                if gen == "N": nom = neut
                elif gen == "F" and decl in ["212","33"]: nom = root + [0,0,"a","is"][int(decl[0])]
                else: nom = masc
                
                if decl[0] == "3": curdecl = 3
                elif gen == "F": curdecl = 1
                else: curdecl = 2
                
                forms += case([curdecl,nom,root,gen,"adj"])
        #print term, "()"
        for form in forms:
            if term == "caperet": print form, stem
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
            for l in difs: #l is a value location (Gender,case,Tense,etc.)
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
            elif p[0] in ["adj","unus","prn"]:
                if p[0] != "adj" or decl == "212": dct = [masc,root+"a",neut]
                else:
                    dct = [root+"is"]
                    if decl in ["32","33"]: dct.append(neut)
                    if decl in ["31","33"]: dct.insert(0,masc)
                if masc == "qui": dct = "qui quae quod".split(" ")
                if masc == "hic": dct = "hic haec hoc".split(" ")
                if masc in "ille iste".split(" "): dct = [masc,masc[:-1]+"a",masc[:-1]+"ud"]
                if masc == "alius": dct[2] = "aliud"
            elif p[0] == "pers": fake1=0
            elif p[0] == "v":
                if stem[0][-1] == "D": dct = [stem[1]+"or",ppi,stem[4]+"us sum","-"] #sequor,sequi,secutus sum,-
                else: dct = [stem[1]+"o",pai,stem[2]+"i",stem[4]+"us"] #paro,parare,paravi,paratus
                if stem[0] == "sum":
                    dct[0] = stem[1]+"sum"
                    dct[3] = "-"
                elif stem[0] == "4E":
                    dct[0] = dct[0][:-1] + "eo"
            dct = ",".join(dct)
            fins.append([term,dct,prsf,stem[-1],""]) #["regum","rex,regis","M-G-S","to rule",""]
    if len(fins) > 2: #Conflict: Multiple Possibilities (ie.rei from res,rei:thing or reus,rei:defendant)
        cur = fins[1][1:5:2]
        for fin in fins[1:]:
            if fin[1:5:2] != cur: cur = ""
        if cur == "": dfn = ""
        else:
            cur = fins[1][1]
            dfn = fins[1][3]
        final = [term,cur,"",dfn,""] #leaves blank spaces b/c origin unknown
        words = [fins[0]]
        for fin in fins[1:]:
            words.append(fin[1:4])
        rep = ["multi"]+words #error reporting is notified
    elif len(fins) == 1: #Error: Term Unknown (new word not in glossaries)
        final = [term,"","","",""] #leaves blank spaces b/c origin unknown
        rep = ["unknown",term] #error reporting is notified
    else: final = fins[1] #when program is running smoothly
    return [final,rep]
#print expand(["fert",["v","p",["3F","fer","tul","fere","lat","to bear"]]])
#print expand(["fiebat",["v","p",["3i","faci","tul","facie","fact","do"]]])
#print expand(["adfert",["v","p",["3F","adfer","adtul","adfere","lat","idk"]]])
#print expand(["nobis",["pers"]])
#print expand(["te",["pers"]])
#print expand(["huius",["prn",["hic","this"]]])
#print expand(["posses",["v","sum",["sum","pot","potu","posse","-"]]])
#print expand(["quod",["conj"],["prn",["qui","rel./inq. prn"]]])