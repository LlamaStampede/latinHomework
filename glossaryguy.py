print "Input format: hortor_hortari_hortatus sum_-_urge"
while True:
    part = raw_input("Parts of Speech:\nnoun\nverb\nadj\nadverb \nprep\nprn\n\nx__ ")
    if part == "q": break
    word = "\t".join(raw_input("Word: ").split("_"))
    f = open(part+"s.txt","r")
    exists = False
    for line in f.read().split("\n"):
        if line == word: exists = True
    f.close()
    if exists: print "That entry already exists."
    else:
        f = open(part+"s.txt","a")
        f.write("\n"+word)
        f.close()