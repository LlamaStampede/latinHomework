# Phase: Prepare
f = open("rawText.txt", "r")
lines = f.read()
f.close()

usableText = []
lastspace = True #prevents double spaces
godown = True
for i in range(0, len(lines)):
    letter = lines[i]
    if letter.isalpha() or (letter == " " and not lastspace):
        if lastspace and letter.isalpha(): firstletter = True
        else: firstletter = False
        if firstletter and godown:
            letter = letter.lower()
            godown = False
        usableText.append(letter)
        if letter == " ": lastspace = True
        else: lastspace = False
    if letter in [".",":",";"] and not firstletter:
        godown = True
while usableText[0] == " ":
    usableText.pop(0)
usableText = "".join(usableText).split(" ")

realText = []
for term in usableText:
    if len(term) > 3 and term[-3:] == "que" and not term in ["atque", "quemque", "neque", "plerumque","denique"]: realText += [term[:-3],"+que"]
    elif term == "modo" and realText[-1] == "non": realText[-1] = "non_modo"
    else: realText.append(term)

method = 0

from describe import *
from expand import *

# Phase: Collect
def inc(term,list): # efficiently returns (term in list) boolean
    for item in list:
        if term == item[0]: #[0] important
            return [True,item]
    return [False]

def glossary(url):
    f = open("../dictionary/"+url+".txt","r")
    gloss = f.read().split("\n")
    f.close()
    for i in range(len(gloss)):
        gloss[i] = gloss[i].split("\t")
    return gloss

verbList = glossary("verbs")
prepList = glossary("preps")
advList = glossary("adverbs")
nounList = glossary("nouns")
adjList = glossary("adjs")

ex_terms = realText #raw_input("Enter a term: ").split(" ")
#ex_terms = ["imus"]

preps = []
for prep in prepList:
    if len(prep) == 1:
        phase = prep[0]
    else:
        preps.append([prep[0].lower(),prep[1],phase])
advs = []
for adv in advList:
    advs.append(adv[::-1])



# Phase: Conjugate

vstems = []
for verb in verbList:
    vstems.append(conj(verb))

nstems = []
for noun in nounList:
    nstems.append(decl(noun))

astems = []
for adj in adjList:
    astems.append(adecl(adj))

#Phase: Assemble
specials = [["bonus","melior","optimus"], ["malus","peior","pessimus"], ["magnus","maior","maximus"], ["parvus","minor","minimus"], ["multus","pluror","plurimus"]]
def compable(term,adjroot):
    for spec in specials:
        if adjroot == spec[0][:-2]:
            for i in range(1,3):
                if term[:len(spec[i])-2] == spec[i][:-2]: return True
    return False

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
        if stem[0] == "sum" and stem[1] == term[:len(stem[1])]:
            pos[-1].append(["v","sum",stem])
        elif stem[1][:-1] == term[:len(stem[1])-1] and (stem[0][-1] != "E" or term[:len(stem[1])+1] in ["i","e"]) and stem[0][-1] != "P":
            pos[-1].append(["v","p",stem]) #program checks the present system
        if not stem[0][-1] in ["D","S"] and stem[2] != "-" and stem[2][:len(stem[2])-addit] == term[:len(stem[2])-addit]:
            pos[-1].append(["v","pf",stem]) #checks the perfect system if neither semidep nor dep
        if stem[3] == term[:len(stem[3])] or stem[4] == term[:len(stem[4])]:
            pos[-1].append(["v","ppl",stem]) #checks all resulting participles if either "capie" or "capt" begins the term

    #pronouns and special adjectives
    unus = [["unus","one"],["nullus","none"],["ullus","any"],["solus","alone"],["neuter","neither"],["alter","either"],["uter","whichever"],["totus","all"],["alius","other"]] #unus nauta
    for un in unus:
        if term[:len(un[0])-2] == un[0][:-2]: pos[-1].append(["unus",un])

    prns = [["hic","this",5],["ille","that",7],["iste","that",7], ["qui","rel./inq.",6],["is","weak dem.",8],["ipse","refl. adj.",7]] #word, def, max length
    first = [["h"],["ill"],["ist"],["qu","cui"],["i","e"],["ips"]] #first letters (pre = prefix)
    for i in range(len(first)):
        for pre in first[i]: #checks if term begins w/ same letters as any pronoun
            if len(term) <= prns[i][2] and term[:len(pre)] == pre: pos[-1].append(["prn",prns[i][:2]])

    #nouns
    for stem in nstems: #appends noun if term begins with noun's root
        if stem[2] == term[:len(stem[2])] or term == stem[1]: pos[-1].append(["n",stem])

    #adjectives
    
    for stem in astems:
        if term in stem[2:4] or term[:len(stem[1])] == stem[1] or compable(term,stem[1]): pos[-1].append(["adj",stem])

    #conjunctions
    conjs = ["atque","+que","ac","et","sed","at","aut","autem","tamen","si","tam","ita","sic","ut","num","ne","neque","enim","nam","dum","cum","quod","quasi"]
    if term in conjs: pos[-1].append(["conj"])
    
    #personal pronouns
    for letter in ["m","t","s","n","v"]:
        if term[0] == letter: pos[-1].append(["pers"])
    if term == "ego": pos[-1].append(["pers"])


#Phase: Select
final_list = []
report = []
#print pos
ind = 0
for pts in pos: #pts = possible terms: ["ducet",[duco,ducere,...],[do,dare,...]]
    ind += 1
    if ind < len(pos): nextword = pos[ind][0]
    else: nextword = "finish"
    [final,rep] = expand(pts,method,nextword,ind)
    final_list.append(final)
    if rep != []: report.append(rep)

#Phase: Format
ppls = []
parsing = "y" #Change to "n" to eliminate parsing
errors = "y" #Change to "n" to eliminate error report

for col in range(len(final_list)):
    if parsing == "n": final_list[col][2] = ""
    elif "Ppl" in final_list[col][2]:
        ppls.append(final_list[col][0:4])
        final_list[col][2] = [final_list[col][2],"","<input type='text' value='%s'>"%(final_list[col][2])][method]

for col in range(len(final_list)): #dct compression
    stem = final_list[col][1].split(",")
    if len(stem) > 1 and len(stem[1]) >= 3:
        if stem[1][-3:] == "are": final_list[col][1] = stem[0]+"(1)"
        elif stem[1][-3:] == "ari": final_list[col][1] = stem[0]+"(1D)"
        elif not "-" in stem and stem[1][-2:] == "re" and [stem[0][-2:],stem[1][-3]] != ["eo","i"]:
            root = stem[1][:-3]
            [two,three,four] = ["-"+stem[1][-3:],stem[2],stem[3]]
            if len(stem[2]) > len(root) and root == stem[2][:len(root)]: three = "-" + stem[2][len(root):]
            if len(stem[3]) > len(root) and root == stem[3][:len(root)]: four = "-" + stem[3][len(root):]
            final_list[col][1] = ",".join([stem[0],two,three,four])
        elif final_list[col][1][-2:] == ",-": final_list[col][1] = final_list[col][1][:-2]
    if len(stem) == 3 and [stem[0][-2:],stem[1][-1],stem[2][-2:]] == ["us","a","um"]: final_list[col][1] = stem[0]+",-a,-um"
    if len(stem) == 2:
        if [stem[0][-1],stem[1][-2:]] == ["a","ae"]: final_list[col][1] = stem[0]+",-ae"
        elif [stem[0][-2:],stem[1][-1]] == ["us","i"]: final_list[col][1] = stem[0]+",-i"
        elif [stem[0][-2:],stem[1][-1]] == ["um","i"]: final_list[col][1] = stem[0]+",-i"
        elif [stem[0][-2:],stem[1][-2:]] == ["us","us"]: final_list[col][1] = stem[0]+",-us"
        elif [stem[0][-2:],stem[1][-2:]] == ["es","ei"]: final_list[col][1] = stem[0]+",-ei"
        else:
            for t in [["tas","tatis"],["tio","tionis"],["or","oris"],["is","e"],["ns","ntis"]]:
                if [stem[0][-len(t[0]):],stem[1][-len(t[1]):]] == t:
                    final_list[col][1] = stem[0]+",-"+t[1]
    term = final_list[col][0]
    names = {"M":"Marcus","L":"Lucius"}
    if term in names: final_list[col][1::2] = [names[term],names[term]]

from output0 import *
format(final_list,report,parsing,errors)
#print report

