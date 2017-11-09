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
        if usableText[0] == " ":
            usableText.pop(0)
    usableText = "".join(usableText)
    usableText = usableText.split(" ")
    return(usableText)
print(getUsableText("rawText.txt"))
