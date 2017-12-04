# Phase: Prepare
f = open("rawText.txt", "r")
lines = f.read()
f.close()

usableText = []
lastspace = False #prevents double spaces
for i in range(0, len(lines)):
    if lines[i].isalpha() or (lines[i] == " " and not lastspace):
        usableText.append(lines[i])
        if lines[i] == " ": lastspace = True
        else: lastspace = False
while usableText[0] == " ":
    usableText.pop(0)
usableText = "".join(usableText)
usableText = usableText.split(" ")

realText = []
for term in usableText:
    if len(term) > 3 and term[-3:] == "que" and not term in ["atque", "quemque", "neque", "plerumque"]: realText += [term[:-3],"+que"]
    else: realText.append(term)

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
        elif stem[1] == term[:len(stem[1])] and (stem[0][-1] != "E" or term[:len(stem[1])+1] in ["i","e"]):
            pos[-1].append(["v","p",stem]) #program checks the present system
        if not stem[0][-1] in ["D","S"] and stem[2] != "-" and stem[2][:len(stem[2])-addit] == term[:len(stem[2])-addit]:
            pos[-1].append(["v","pf",stem]) #checks the perfect system if neither semidep nor dep
        if stem[3] == term[:len(stem[3])] or stem[4] == term[:len(stem[4])]:
            pos[-1].append(["v","ppl",stem]) #checks all resulting participles if either "capie" or "capt" begins the term

    #pronouns and special adjectives
    unus = [["unus","one"],["nullus","none"],["ullus","any"],["solus","alone"],["neuter","neither"],["alter","either"],["uter","whichever"],["totus","all"],["alius","other"]] #unus nauta
    for un in unus:
        if term[:len(un[0])-2] == un[0][:-2]: pos[-1].append(["unus",un])

    prns = [["hic","this",5],["ille","that",7],["iste","that",7], ["qui","rel./inq.",6],["is","weak dem.",3]] #word, def, max length
    first = [["h"],["ill"],["ist"],["qu","cui"],["i","e"]] #first letters (pre = prefix)
    for i in range(len(first)):
        for pre in first[i]: #checks if term begins w/ same letters as any pronoun
            if len(term) <= prns[i][2] and term[:len(pre)] == pre: pos[-1].append(["prn",prns[i][:2]])

    #nouns
    for stem in nstems: #appends noun if term begins with noun's root
        if stem[2] == term[:len(stem[2])] or term == stem[1]: pos[-1].append(["n",stem])

    #adjectives
    for stem in astems:
        if term in stem[2:4] or term[:len(stem[1])] == stem[1]: pos[-1].append(["adj",stem])

    #conjunctions
    conjs = ["atque", "+que", "ac", "et", "sed", "at", "autem", "tamen", "si", "tam", "ita", "sic", "ut", "neque", "enim", "nam"]
    if term in conjs: pos[-1].append(["conj"])


#Phase: Select
final_list = []
report = []
#print pos
for pts in pos: #pts = possible terms: ["ducet",[duco,ducere,...],[do,dare,...]]
    [final,rep] = expand(pts)
    final_list.append(final)
    if rep != []: report.append(rep)

import os
os.remove("describe.pyc")
os.remove("expand.pyc")

#Phase: Format
ppls = []
while True:
    parsing = raw_input("Parsing, y/n? ")
    if parsing == "": parsing = "y"
    if parsing in ["y","n"]: break
    print "Invalid Response"
while True:
    errors = raw_input("Report errors, y/n? ")
    if errors == "": errors = "y"
    if errors in ["y","n"]: break
    print "Invalid Response"

for col in range(len(final_list)):
    if parsing == "n": final_list[col][2] = ""
    elif "Ppl" in final_list[col][2]:
        ppls.append(final_list[col][0:4])
        final_list[col][2] = ""

for col in range(len(final_list)): #dct compression
    stem = final_list[col][1].split(",")
    if len(stem) > 1 and len(stem[1]) >= 3:
        if stem[1][-3:] == "are": final_list[col][1] = stem[0]+"(1)"
        elif stem[1][-3:] == "ari": final_list[col][1] = stem[0]+"(1D)"
        elif not "-" in stem and stem[1][-2:] == "re" and [stem[0][-2:],stem[1][-3]] != ["eo","i"]:
            root = stem[1][:-3]
            [two,three,four] = ["-"+stem[1][-3:],stem[2],stem[3]]
            if len(stem[2]) > root and root == stem[2][:len(root)]: three = "-" + stem[2][len(root):]
            if len(stem[3]) > root and root == stem[3][:len(root)]: four = "-" + stem[3][len(root):]
            final_list[col][1] = ",".join([stem[0],two,three,four])

def flipped(block):
    table = []
    for height in range(5):
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

doc_width = 70 # change this to widen or lengthen the final product
indent = 6
all_lines = []
line_group = []
page = []
for col_id in range(len(final_list)):
    if indent + col_widths[col_id] > doc_width:
        line_group.insert(0,["txt","dct","prs","trn","cmt"])
        page.append(line_group) # archives old line
        indent = 6
        line_group = [] # begins new line
        if len(page) == 8:
            all_lines.append(page)
            page = []
    line_group.append(final_list[col_id])
    indent += col_widths[col_id] + 3
line_group.insert(0,["txt","dct","prs","trn","cmt"])
page.append(line_group)
all_lines.append(page)

horizon = ""
for i in range(doc_width):
    horizon += "-"

name = raw_input("Output file name: ")
if name in ["","y"]: name = "output"
output = open(name+".txt","w+")
for pg in all_lines:
    for line_group in pg:
        for row in flipped(line_group):
            for col_id in range(len(row)):
                output.write(row[col_id])
                if col_id == len(row) - 1: output.write("\n")
                else: output.write(" | ")
        output.write(horizon+"\n")
    output.write("\n\n")

if errors == "y":
    for err in report:
        if err[0] == "unknown": output.write("UNKNOWN: "+err[1]+"\n")
        elif err[0] == "multi":
            output.write("Conflict: "+err[1]+" might be from:\n")
            for w in err[2:]: #w = each individual dictionary entry
                output.write("- "+w[0]+" "+w[1]+" "+w[2]+"\n")
if parsing == "y":
    for ppl in ppls:
        output.write("Participle: "+": ".join(ppl)+"\n")
output.close()
