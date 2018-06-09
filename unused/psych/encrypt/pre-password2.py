from random import randrange
output = open("alpha676.txt","w+")
chars = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M 1 2 3 4 5 6 7 8 9 0 q w e r t y u i o p a s d f g h j k l z x c v b n m".split(" ")+[" "]
primes = []
copy = chars[:]
i = 1
while len(copy) > 0:
    i += 2
    val = True
    for p in primes:
        if i % p == 0:
            val = False
            break
    if val:
        primes.append(i)
        if i > 100:
            ind = randrange(0,len(copy))
            output.write("%s-%i|"%(copy.pop(ind),i))
output.close()