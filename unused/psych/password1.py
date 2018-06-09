from random import randrange
ids = []
chars = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M 1 2 3 4 5 6 7 8 9 0 q w e r t y u i o p a s d f g h j k l z x c v b n m".split(" ")
print chars

def boxit(box):
    for vector in box:
        counter = 1
        for a in vector:
            print a,
            if counter == 4:
                print ""
                counter = 0
            counter += 1
        print ""

def lineit(line):
    for dig in line:
        print dig,
    print ""

vectors = []
for a in range(len(chars)):
    blankslate = []
    for a2 in range(len(chars)):
        blankslate.append(0)
    vectors.append(blankslate)
    vectors[-1][a] = 1

for vector in vectors:
    for dig in vector:
        if dig == 0: print "_",
        else: print dig,
    print ""
print ""
for s in range(1000):
    x = randrange(0,len(chars))
    while True:
        y = randrange(0,len(chars))
        if y != x: break
    if randrange(0,2) == 0:
        placeholder = vectors[y]
        vectors[y] = vectors[x]
        vectors[x] = placeholder
    else:
        for a in range(len(chars)):
            vectors[x][a] = (vectors[x][a]+vectors[y][a])%2
for vector in vectors:
    for dig in vector:
        if dig == 0: print "_",
        else: print dig,
    print ""
print ""
