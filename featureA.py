#this file is made to convert the text copied from the Perseus Project into code that we can work with in our program

#the test text is:
#[20] quae cum ita sint, Catilina, dubitas, si emori aequo animo non potes, abire in aliquas terras et vitam istam multis suppliciis iustis debitisque ereptam fugae solitudinique mandare?
def getLines(file):
    f = open(file, "r")
    lines = f.read()
    f.close()
    return(lines)

def getUsableText(file):
    lines = getLines(file)
    usableText = []
    for i in range(0, len(lines)):
        if lines[i].isalpha() or lines[i] == " ":
            usableText.append(lines[i])
    while usableText[0] == " ":
        usableText.pop(0)
    newLis = [usableText[0]]#this whole newLis section is for removing double spaces
    for i in range(1, len(usableText)):
        if usableText[i] != " " or usableText[i-1] != " ":
            newLis.append(usableText[i])
    usableText = newLis
    usableText = "".join(usableText)
    usableText = usableText.split(" ")
    return(usableText)
#print(getUsableText("rawText.txt"))
#getUsableText returns in this example:
#['quae', 'cum', 'ita', 'sint', 'Catilina', 'dubitas', 'si', 'emori', 'aequo', 'animo', 'non', 'potes', 'abire', 'in', 'aliquas', 'terras', 'et', 'vitam', 'istam', 'multis', 'suppliciis', 'iustis', 'debitisque', 'ereptam', 'fugae', 'solitudinique', 'mandare']
