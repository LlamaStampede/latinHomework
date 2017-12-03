#PYTHONDONTWRITEBYTECODE=True
#export PYTHONDONTWRITEBYTECODE
import featureA
import os
try:
    os.remove('featureA.pyc')
except:
    print()

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


ex_terms = featureA.getUsableText("due11-14.txt")#raw_input("Enter a term: ").split(" ") # You might need to change this to input() for your python version


preps = []
for prep in prepList:
    print(prep)
    if len(prep) == 1:
        phase = prep[0]
    else:
        preps.append([prep[0].lower(),prep[1]])
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
        if dep and verb[1][-2] != "r":
            conj = "3"
            if verb[0][-2-addit] == "i": conj = "3i"
        if dep: conj += "D"
        elif semidep: conj += "S"
        elif "-" in verb: conj = "def"

        primary = verb[0][:-1]
        if dep: primary = verb[0][:-2]
        secondary = verb[2][:-1]
        if dep or semidep: secondary = "-"
        if verb[2] == "-": secondary = "-"

        impf = primary
        if conj[0] == "1": impf += "a"
        elif conj[0] in ["3","4"]: impf += "e"

        if dep: ppp = verb[2][:-6] #CONATus sum
        elif verb[3] == "-": ppp = "-"
        else: ppp = verb[3][:-2]

        return [conj,primary,secondary,impf,ppp,trn]
    elif verb[0] == "-":
        if verb[3] == "-":
            ppl = "-"
        else:
            ppl = verb[3][:-2]
        return ["3P","-",verb[2][:-1],"-",ppl,trn] #preterate
    elif verb[0][-1] == "m":
        root = verb[0][:-3]
        if len(root) != 0 and root[-1] == "s": root = root[:-1] + "t"
        return ["sum",root,verb[2][:-1],verb[1],"-",trn] #sum-thing
    elif verb[0][-1] == "t":
        if verb[1] == "-": conj = "imp" #impersonal
        else: conj = "third" #third-only
        return [conj,verb[0],verb[1],"-","-",trn]
#print conj("paro parare paravi paratus prepare".split(" "))
#print conj("sequor_sequi_secutus sum_-_follow".split("_"))
#print conj("moneo monere monui monitus warn".split(" "))
#print conj("salveo salvere - - be_healthy".split(" "))
#print conj("patior_pati_passus sum_-_endure".split("_"))
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
pos = [] #pos = list of all terms in passage and their possible stems
for term in ex_terms:
    pos.append([term])

    adv = inc(term,advs) #adv = {term is an adverb, yes/no}
    if adv[0]: pos[-1].append(["adv",adv[1]])
    prep = inc(term,preps) #prep = {prep is an adverb, yes/no}
    if prep[0]: pos[-1].append(["prep",prep[1]])

    for stem in vstems: #every append statement only happens if term begins with verb's root
        if stem[2][-1] == "v": addit = 1 #to account for syncopation eliminating the "v"
        else: addit = 0 #ie. monui has no "v"
        if stem[0] == "sum" and stem[1] == term[:len(stem[1])]: pos[-1].append(["v","sum",stem])
        elif stem[1] == term[:len(stem[1])]: pos[-1].append(["v","p",stem]) #program checks the present system
        if not stem[0][-1] in ["D","S"] and stem[2] != "-" and stem[2][:len(stem[2])-addit] == term[:len(stem[2])-addit]: pos[-1].append(["v","pf",stem]) #checks the perfect system if neither semidep nor dep
        if stem[3] == term[:len(stem[3])] or stem[4] == term[:len(stem[4])]: pos[-1].append(["v","ppl",stem]) #checks all resulting participles if either "capie" or "capt" begins the term

    prns = [["hic","this",5],["qui","-",6],["is","weak dem",3]] #word, def, max length
    pres = [["h"],["qu","cui"],["i","e"]] #prefixes (word-beginnings)
    for i in range(len(pres)):
        for pre in pres[i]: #checks if term begins with same initial letters as any pronouns
            if len(term) <= prns[i][2] and term[:len(pre)] == pre: pos[-1].append(["prn",prns[i][:2]])

    #nouns
    for stem in nstems: #appends noun if term begins with noun's root
        if stem[2] == term[:len(stem[2])] or term == stem[1]: pos[-1].append(["n",stem])

    #adjectives


#Phase: Select
final_list = []
report = []
personal = ["o","s","t","mus","tis","nt","or","ris","tur","mur","mini","ntur"] #personal endings
perfects = ["i","isti","it","imus","istis","erunt"] #perfect endings
persons = ["1S","2S","3S","1P","2P","3P"] #1st/2nd/3rd Sg/Pl
sums = ["sum","es","est","sumus","estis","sunt"] #sum in the present
sufs = ["placeholder", #so that a word's suffixes can be called via sufs[decl] instead of sufs[decl-1]
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
def infin(c,stem):
    if c == "1": end = "are"
    elif c == "3": end = "ere"
    else: end = "re"
    root = stem[1]
    if len(stem[0]) > 1 and stem[0][1] == "i": root = root[:-1] #CAPi
    if c == "s": [root,end] = [stem[3],""]
    pai = root+end #pai = Present Active Infinitive
    if c == "3": end = end[:-3]+"i"
    else: end = end[:-1]+"i"
    ppi = root+end #ppi = Present Passive Infinitive
    return [pai,ppi]
for pts in pos: #pts = possible terms: ["ducet",[duco,ducere,...],[do,dare,...]]
    term = pts.pop(0)
    fins = [term] #finalists, all aplicable forms will later be appended
    for p in pts: #p = possibile word ([do,dare,...])
        apls = [] #apls=aplicable forms
        forms = [] #every form of the word will be added
        #if p[0] == "prep": fins.append([term,term,"Prep w/"+p[1][2],p[1][1],""]) #prep & adv (& con) are guaranteed matches
        if p[0] == "adv": fins.append([term,term,"Adv",p[1][1],""])
        elif p[0] == "conj": fins.append([term,term,"Conj",p[1][1],""])
        elif p[0] == "v": #Intensive verb identifier, all tenses
            #print(p)
            stem = p[2]
            if p[1] == "p": #present system (P,Impf,F)
            #this section is only enabled if the term begins with some verb's present stem
                c = stem[0][0] #1st character of conjugation (1,2,3,4)
                for tense in ["P","Impf","F"]:
                    pers = personal[:]
                    if tense in ["P","F"]: root = stem[1]
                    if tense == "Impf" or c in ["1","2"]: root = stem[3] + "b" #This line undoes the last one for parabit, etc.
                    if tense == "Impf": root += "a"
                    for i in range(12): #range(12) means 1st/2nd/3rd Sg/Pl Active/Passive
                        if i<6: voice = "A"
                        else: voice = "P"
                        if stem[0][-1] == "D": voice = "D"

                        if tense == "P":
                            if c == "1" and i%6 != 0: pers[i] = "a" + pers[i]
                            elif c in ["3","4"] and i == 7: pers[i] = "e" + pers[i] #avoid "iri" in the 2ndSgP
                            elif c == "3" and not "i" in stem[0] and i%6 in range(1,5): pers[i] = "i" + pers[i] #regit
                            elif c in ["3","4"] and i%6 == 5: pers[i] = "u" + pers[i] #capiunt
                        elif tense == "Impf":
                            pers[::6] = ["m","r"] #parabam
                        elif tense == "F":
                            if c in ["1","2"]: #bo bis bit
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
                if stem[0][-1] != "D": forms.append([pai,"P-Inf-A"])
                if stem[0][-1] != "D": forms.append([ppi,"P-Inf-P"]) #parari
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
                            if c == "1" and i%6 != 0: pers[i] = "e" + pers[i] #lets
                            else: pers[i] = "a" + pers[i] #eat caviar
                        else: root = pai #imperfect subjuntives are the p.a.i. plus personal endings
                        if deply(stem[0],i):
                            forms.append([root+pers[i],"%s-%s-S-%s"%(persons[i%6],tense,voice)])
                            if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-S-%s" % (persons[i%6],tense,voice)]) #alternative 2ndPlP form (looks like p.a.i. in the present)


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

                        forms.append([root+pers[i],"%s-%s-I-A" % (persons[i%6],tense)])
                        if pers[i][-3:] == "ris": forms.append([(root+pers[i])[:-2]+"e","%s-%s-I-A"%(persons[i%6],tense)]) #alterntive 2ndPlP form
                        if stem[2][-1] == "v" and i != 0: forms.append([root[:-1]+pers[i][1:],"%s-%s-I-A" % (persons[i%6],tense)]) #syncopation
                        if pers[i][-3:] == "ris" and stem[2][-1] == "v": forms.append([root[:-1]+pers[i][1:-2]+"e","%s-%s-I-A" % (persons[i%6],tense)]) #syncopated alternative 2ndPlP form

                pfi = stem[2]+"isse" #pfi = PerFect active Infinitive
                forms.append([pfi,"Pf-Inf-A"])

                for tense in ["Pf","Ppf"]: #subjunctives
                    pers = personal[:6]
                    pers[0] = "m"
                    for i in range(6):
                        if tense == "Pf": root = stem[2] + "eri" #pf subjunctive perfect stem + "eri" + personal endings
                        else: root = pfi #ppf subjunctive is p.f.i. + personal endings
                        forms.append([root+pers[i],"%s-%s-S-A"%(persons[i%6],tense)])
                        if (root+pers[i])[-3:] == "ris": forms.append([root+pers[i][:-2]+"e","%s-%s-S-A"%(persons[i%6],tense)]) #alt 2PlP form
            elif p[1] == "ppl": #All participles, enabled if term contains impf stem (CAPIEbam) or p.p.p. stem (CAPTus)
                for n in range(4): #0:PPplA 1:FPplP 2:FPplA 3:PfPplP
                    nom = stem[[3,4][n/2]] + ["ns","nd","ur",""][n] #0:parans 1:parand(us-a-um) 2:paratur(us-a-um) 3:parat(us-a-um)
                    root = stem[[3,4][n/2]] + ["nt","nd","ur",""][n] #0:parant(is) 1:parand(i-ae) 2:paratur(i-ae) 3:parat(i-ae)
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
                if len(stem[2]) > 1 and (stem[1][-1] in ["s","x"] and not (stem[2][-1] in vowels or stem[2][-2] in vowels)):
                    istem = True #base in 2 consonants

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
            print "no glossary yet"
        if p[0] in ["v","n"]: #conflict resolution/error reporting
            for form in forms:
                #print form
                if form[0] == term: apls.append([stem,form[1]]) #checks if term and form spelled the same
        if len(apls) != 0:
            difs = [] #for conflicting parsings (dat/abl pl)
            ld = {"n":3,"v":6}[p[0]] #verbs can have at most 6 (participles). nouns only ever have 3 (gender,case,number)
            for i in range(ld):
                difs.append([])

            prsf = "" #prsf = Final Parsing (will include blankspaces)
            for apl in apls: #aplicable forms
                prs = apl[1].split("-")
                #print prs
                for l in range(len(prs)):
                    difs[l+ld-len(prs)].append(prs[l]) #separating parsings into different columns for comparison
            for l in difs: #l is a value location (Gender,Case,Tense,etc.)
                value = True
                cur = 0 #cur = current value (sg,masc,dat,fem,gen,etc.)
                for x in l:
                    if cur == 0: cur = x
                    elif cur != x: #Conflicting values in the same word
                        value = False #means that neither value is printed in the final cut
                        report.append(["minor",term,stem,difs]) #error reporting is notified
                if len(l) != 0:
                    if value: prsf += l[0] + "-" #if value is certain
                    else: prsf += "   -" #if value is indefinite
                    if l[0][-1] == "/": prsf = prsf[:-1] #eliminates dash after slash: ...-A/-M-...
            prsf = prsf[:-1] # eliminates extra dash: ...-G-P-
            stem = apls[0][0]
            if p[0] == "v": [pai,ppi] = infin(stem[0][0],stem)
            if p[0] == "n": dct = [stem[1],stem[2]+sufs[stem[0]][1]] #rex,regis
            elif stem[0][-1] == "D": dct = [stem[1]+"or",ppi,stem[4]+"us sum","-"] #sequor,sequi,secutus sum,-
            else: dct = [stem[1]+"o",pai,stem[2]+"i",stem[4]+"us"] #paro,parare,paravi,paratus
            if stem[0] == "sum": dct[0] = stem[1]+"sum"
            dct = ",".join(dct)
            fins.append([term,dct,prsf,stem[{"n":4,"v":5}[p[0]]],""]) #["regum","rex,regis","M-G-S","to rule",""]
    if len(fins) > 2: #Conflict: Multiple Possibilities (ie.rei from res,rei:thing or reus,rei:defendant)
        final_list.append([term,"","","",""]) #leaves blank spaces b/c origin unknown
        words = [fins[0]]
        for fin in fins[1:]:
            words.append(fin[1])
        report.append(["multi"]+words) #error reporting is notified
    elif len(fins) == 1: #Error: Term Unknown (new word not in glossaries)
        final_list.append([term,"","","",""]) #leaves blank spaces b/c origin unknown
        report.append(["unknown",term]) #error reporting is notified
    else: final_list.append(fins[1]) #when program is running smoothly


#Phase: Format
parsing = raw_input("Parsing, y/n? ")
errors = raw_input("Report errors, y/n? ")
leng = raw_input("Fitted lines, y/n?")
if parsing == "n":
    for col in range(len(final_list)):
        final_list[col][2] = ""
elif errors == "y":
    minor = raw_input("Report parsing inconsistencies, y/n? ")
    if minor == "y": minors = {}

def flipped(block):
    table = []
    for height in block[0]:
        table.append([]) # this just appends 5 []'s
    for col in block:
        for row_id in range(len(col)):
            table[row_id].append(col[row_id])
    return table
col_widths = []
for col_id in range(len(final_list)):
    lens = [] # used for appending spaces later on
    width = 0
    for row in final_list[col_id]:
        l = len(str(row))
        lens.append(l)
        if l > width: width = l
    col_widths.append(width) #col_width = [longest length of each row segment for each column, ...]
    for row_id in range(len(final_list[col_id])):
        final_list[col_id][row_id] = str(final_list[col_id][row_id])
        for b in range(width - lens[row_id]):
            final_list[col_id][row_id] += " "
# Modifies each term to be equal length. For example: [
# "bonarum"
# "us-a-um"
# "F-G-P  "
# "good   "
# "       "]


doc_width = 140 # change this to widen or lengthen the final product
indent = 4
all_lines = []
line_group = []
block_count = 0
for col_id in range(len(final_list)):
    if indent + col_widths[col_id] > doc_width:
        line_group.insert(0,["txt","dct","prs","trn","cmt"])
        all_lines.append(line_group) # archives old line
        indent = 4
        line_group = [] # begins new line
    if block_count == 8: print "\n\n"
    line_group.append(final_list[col_id])
    indent += col_widths[col_id] + 3
line_group.insert(0,["txt","dct","prs","trn","cmt"])
all_lines.append(line_group)

horizon = [] #each row has its own length which is at minimum 140 get each one is added len(row)
temp = 0
lis = []
liss = []
for line_group in all_lines:
    lis = []
    for row in flipped(line_group):
        temp = 0
        for col_id in range(0, len(row)):
            temp += len(row[col_id])
            temp += 3
        lis.append(temp-3)
    liss.append(lis)
print(liss)
for i in range(0, len(liss)):
    horizon.append("-"*liss[i][0])
#print(len("     | te | autem | Catilina"))
#
#I noticed that the amount of | columns times two is the amount that it is off for each line in most cases?! {~m}
#

for line_group in range(0, len(all_lines)):
    for row in flipped(all_lines[line_group]):
        for col_id in range(len(row)):
            if col_id == len(row) - 1:
                print row[col_id]
            else:
                print row[col_id], "|",# len(row),
    if leng == "y":
        print horizon[line_group]
    else:
        print "-" * doc_width
if errors == "y":
    for err in report:
        if err[0] == "unknown": print "Unknown:",err[1]
        elif err[0] == "multi":
            print "Conflict:",err[1],"might be from",
            for w in err[2:]: #w = each individual dictionary entry
                print w
        elif minor == "y": #ignore code from here down, i haven't figured out how to report minor errors in the way I want yet
            if err[1] in minors: minors[err[1]].append([err[2],err[3]])
            else: minors[err[1]] = [[err[2],err[3]]]
    if len(minors) != 0:
        discs = []
        #print minors
        log = {}
        for mini in minors: #Minor discrpancy (Dat vs Abl)
            if not mini in log: log[mini] = [minors[mini]]
            elif log[mini][-1][0] == minors[mini][0]: log[mini] += minors[mini][1]
            else: log[mini].append([minors[mini]]) #separates minor discs by word origin
        #for mini in log:
            #print mini, log[mini]

        #print mini, "might be",
