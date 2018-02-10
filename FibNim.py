import random

orig = random.randint(20,1000)
last = (orig - 1) / 2
beg = "false"
p1Name = ""
p2Name = ""

def tryagain(lastuse, current):
    global beg
    if beg == "true":
        ret = int(input("Number is more than twice last used number or the number of coins!! please enter a valid number: "))
    else:
        ret = int(input("You can't take all the coins directly. \n Please enter a valid number: "))
    while ret > 2*lastuse or ret > current:
        if beg == "true":
            ret = int(input("Number is more than twice last used number or the number of coins!! please enter a valid number: "))
        else:
            ret = int(input("You can't take all the coins directly. \n Please enter a valid number: "))
    else:
        return (ret)

def player1():
    global p1Name
    global last
    global orig
    global beg
    p1 = int(input(p1Name + "'s turn: "))
    if p1 > 2*last or p1 > orig:
        p1 = tryagain(last, orig)
    last = p1
    orig -= last
    beg = "true"
    print ("There are " + str(orig) + " coins on the table")

def player2():
    global p2Name
    global last
    global orig
    global beg
    p2 = int(input(p2Name + "'s turn: "))
    if p2 > 2*last or p2 > orig:
        p2 = tryagain(last, orig)
    last = p2
    orig -= last
    beg = "true"
    print ("There are " + str(orig) + " coins on the table")

def comp():
    global last
    global orig
    global beg
    if orig <= 2*last:
        cplay = orig
    else:
        cplay = orig // 4
        if cplay > 2*last:
            cplay = 2*last
        if cplay == 0:
            cplay = 1
    print("Computer chose the number " + str(cplay))
    last = cplay
    orig -= last
    print ("There are " + str(orig) + " coins on the table")

def playagain():
    global orig
    global last
    x = input("Play again? (y/n) ")
    if x == "y":
        orig = random.randint(20,1000)
        last = (orig - 1) / 2
        game()
    else:
        exit()

def multiplayer():
    global p1Name
    global p2Name
    print ("There are " + str(orig) + " coins on the table")
    while orig != 0:
        player1()
        if orig == 0:
            print(p1Name + " wins!!")
            playagain()
        player2()
    print(p2Name + " wins!!")
    playagain()

def oneplayer():
    global p1Name
    print ("There are " + str(orig) + " coins on the table")
    while orig != 0:
        player1()
        if orig == 0:
            print(p1Name + " wins!!")
            playagain()
        comp()
    print("Computer wins!!")
    playagain()

def game():
    global p1Name
    global p2Name
    playmode = input("Enter 1 for one player or 2 for two players: ")
    if playmode == "1":
        p1Name = input("Player 1 name: ")
        oneplayer()
    else:
        p1Name = input("Player 1 name: ")
        p2Name = input("Player 2 name: ")
        multiplayer()
    
game()
