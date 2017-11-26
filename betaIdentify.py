import featureA
import os
try:
    os.remove('featureA.pyc')
except:
    print()

def glossary(url):                                                                                                                    
    f = open(url,"r")                                                                                                                 
    gloss = f.read().split("\n")                                                                                                      
    f.close()                                                                                                                         
    for i in range(0, len(gloss)):                                                                                                    
        gloss[i] = gloss[i].split("\t")                                                                                               
    return gloss                                                                                                                      

def getTerms():
    terms = featureA.getUsableText("due11-14.txt")
    #print(terms)
    return(terms)
verbList = glossary("verbs.txt")#[['paro', 'parare', 'paravi', 'paratum', 'prepare'], ['moneo', 'monere', 'monui', 'monitum', 'warn']]
prepList = glossary("preps.txt")#[['ANTE', 'before'], ['PER', 'through, because of']]
advList = glossary("adverbs.txt")#[['yesterday', 'heri'], ['today', 'hodie']]
nounList = glossary("nouns.txt")#[['terra', '-ae', 'f', 'land'], ['vita', '-ae', 'f', 'life']]
conjList = glossary("conjunctions.txt")#et	and, que	and, si	if
adjList = glossary("2-1-2adjectives.txt")
#print(adjList)

def getPossibleWords(term):
    lis = [] #any possible terms will be appended to this lis which will ultimately be returned
    beginning = term[0:2]
    lis.append(term)
    for prep in prepList:
        prep[1] = prep[1].lower()
        if term == prep[1]:
            lis.append(["p", prep])
            return(lis) #the reason for the early return is if it equals the prep, conj, or adj then we dont need to check the verb to increase efficiency
    for adverb in advList:
        if term == adverb[1]:
            lis.append(["adv", adverb])
            return(lis)
    for conj in conjList:
        if term == conj[0]:
            lis.append(["c", conj])
            return(lis)
    for verb in verbList:
        if beginning == verb[0][0:2] or beginning == verb[2][0:2]:
            lis.append(["v", verb])
    for noun in nounList:
        if beginning == noun[0][0:2] or beginning == noun[1][0:2]:
            lis.append(["n", noun])
    for adj in adjList:
        if beginning == adj[0][0:2]:
            lis.append(["adj", adj])
    return(lis)
