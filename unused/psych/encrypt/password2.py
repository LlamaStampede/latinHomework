from math import sqrt

chars = "Q W E R T Y U I O P A S D F G H J K L Z X C V B N M 1 2 3 4 5 6 7 8 9 0 q w e r t y u i o p a s d f g h j k l z x c v b n m".split(" ")+[" "]
ids = {}
textfile = open("alpha676.txt","r")
text = textfile.read()[:-1].split("|")
for item in text:
    pair = item.split("-")
    ids[pair[0]] = pair[1]

ok = [True,False,False] # [ignor,cease,menu]
def encrypt(password): # The important bit
    userid = 1
    for char in password:
        userid *= int(ids[char])
    userid = int(sqrt(sqrt(userid)))
    while userid >= 10**9: userid /= 10
    while userid < 10**9: userid *= 2
    return str(userid)[:1] + "-" + str(userid)[1:5] + "-" + str(userid)[5:]

def greek(password):
    for char in password:
        giveup = True
        for numlet in chars:
            if char == numlet: giveup = False
        if giveup: return True
    return False

people = []
def taken(value,type):
    return type == "username" and value in people

def check(value,type,cease,menu,which):
    if value == "q": cease = True
    elif value == "r": menu = True
    elif len(value) > 16: print "That %s is too long." % which
    elif len(value) < 8: print "That %s is too short." % which
    elif greek(value): print "Only alphanumeric characters please."
    elif taken(value,type): print "That username is already taken."
    else: return [True,cease,menu]
    return [False,cease,menu]

while True:
    if ok[2]:
        for l in range(10):
            print "\n"
        ok[2] = False
    print "\nAdmin Portal Home\n"
    print "Available Actions:\nType l to login\nType a to make a new account\nType v to view existing accounts\nType h for help\nType r to return to home menu\nType q to quit"
    while True:
        input = open("users.txt","r")
        users = input.read().split("|")[:-1]
        people = []
        for u in range(len(users)):
            users[u] = users[u].split(":")
            people.append(users[u][0])
        
        action = raw_input("\nAction: ")
        if action == "l":
            ice = False
            while True:
                username = raw_input("Username: ")
                if username == "q": ok[1] = True
                elif username == "r": ok[2] = True
                elif username in people:
                    while True:
                        ice = False
                        userid = encrypt(username+raw_input("Password: "))
                        if userid == "q": ok[1] = True
                        elif userid == "r": ok[2] = True
                        else:
                            for user in users:
                                if [username,userid[1:]] == [user[0],user[1][1:]]:
                                    while True:
                                        print username+"$ Action:"
                                        if userid == "q": ok[1] = True
                                        elif userid == "r": ok[2] = True
                                        else:
                                            print "Success!"
                                        if ok[1] or ok[2] or cube: break
                                    ice = True
                                    break
                                if user == users[-1]:
                                    print "That password is incorrect."
                        if ok[1] or ok[2] or ice: break
                else:
                    print "That username does not exist."
                if ok[1] or ok[2] or ice: break
        elif action == "a":
            while True:
                username = raw_input("\nPlease enter a username (8-16 letters): ")
                ok = check(username,"username",ok[1],ok[2],"username")
                if ok[0]:
                    while True:
                        password = raw_input("\nPlease enter a password (8-16 letters): ")
                        ok = check(password,"password",ok[1],ok[2],"password")
                        if ok[0]:
                            if password == raw_input("Confirm Password: "):
                                #print "User ID:",encrypt(username+password) # $$$
                                output = open("users.txt","a")
                                output.write("%s:%s|"%(username,encrypt(username+password)))
                                output.close()
                                people.append(username)
                                break
                            else: print "Try again."
                        if ok[1] or ok[2]: break
                    break
                elif ok[1] or ok[2]: break
        elif action == "v":
            auth = raw_input("Authenticate: ")
            if auth == "muahaha":
                names = ["Usernames:"]
                userids = ["User IDs:"]
                for user in users:
                    names.append(user[0])
                    userids.append(user[1])
                for n in range(len(names)):
                    for b in range(16-len(names[n])):
                        names[n] += " "
                for n in range(len(names)):
                    print names[n],"|",userids[n]
                    if n == 0: print "-----------------|-------------"
            else: print "Incorrect password"
        elif action == "h": print "Type r to return home."
        elif action == "q": ok[1] = True
        elif action == "r": ok[2] = True
        else: print "Invalid Key"
        if ok[1] or ok[2]: break
    if ok[1]: break