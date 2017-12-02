#to do: non-passive, "virtual deponent", preterates
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
        elif verb[3] == "-" and not "-" in verb[:3]: conj += "A"
        elif "-" in verb: conj = "def"
        if [verb[0][-2:],conj] == ["eo","4"]: conj += "E"

        primary = verb[0][:-1]
        if dep or conj == "4E": primary = verb[0][:-2]
        secondary = verb[2][:-1]
        if dep or semidep: secondary = "-"
        if verb[2] == "-": secondary = "-"

        impf = primary
        if conj[0] == "1": impf += "a"
        elif conj == "4E": impf += "i"
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
#print conj("eo ire ivi itus go".split(" "))

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
    elif "-" in gen: root = nom[:-2] + gen[1:-len(suf)]
    else: root = gen[:-len(suf)]
    return [sufs[suf],nom,root,gend.upper(),trn]

def adecl(adj):
    if [adj[1][-1],adj[2][-2:]] == ["a","um"]: decl = 212
    elif len(adj) == 4: decl = 33
    elif adj[1][-2:] == "is": decl = 31
    else: decl = 32

    if decl == 32 or (decl == 212 and adj[1][0] == "-"): root = adj[0][:-2]
    elif decl == 212: root = adj[1][:-1]
    elif decl in [31,33]: root = adj[1][:-2]

    if decl in [33,32]: neut = adj[-2]
    elif decl == 31: neut = adj[0]
    else: neut = root + "um"

    masc = adj[0]
    trn = adj[-1]

    return [str(decl),root,masc,neut,trn]