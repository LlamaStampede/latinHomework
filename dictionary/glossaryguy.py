print "Enter q to quit."
while True:
    part = raw_input("Parts of Speech:\nnoun\nverb\nadj\nadverb\n\nx__ ")
    if part == "q": break
    word = []
    if part == ["verb"]:
        print "Principal parts:"
        for i in range(1,5):
            word.append(raw_input("%i: "%i))
    elif part in ["adj","noun"]:
        while True:
            addon = raw_input("PP: ")
            if addon == "": break
            word.append(addon)
    else:
        word.append(raw_input(word))

    if part == "noun": word.append(raw_input("Gender: ").lower())
    word.append(raw_input("Definition: "))
    if part == "adverb": word.reverse()

    entry = "\t".join(word)
    f = open(part+"s.txt","r")
    exists = False
    for line in f.read().split("\n"):
        if line == entry: exists = True
    f.close()
    if exists: print "That entry already exists."
    else:
        f = open(part+"s.txt","a")
        f.write("\n"+word)
        f.close()