import random

orig = random.randint(20,1000)
last = (orig - 1) / 2
beg = "false"

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
    global last
    global orig
    global beg
    p1 = int(input("Player one's turn: "))
    if p1 > 2*last or p1 > orig:
        p1 = tryagain(last, orig)
    last = p1
    orig -= last
    beg = "true"
    print ("There are " + str(orig) + " coins on the table")

def player2():
    global last
    global orig
    global beg
    p2 = int(input("Player two's turn: "))
    if p2 > 2*last or p2 > orig:
        p2 = tryagain(last, orig)
    last = p2
    orig -= last
    beg = "true"
    print ("There are " + str(orig) + " coins on the table")

def playagain():
    global orig
    global last
    global beg
    x = input("Play again? (y/n) ")
    if x == "y":
        orig = random.randint(20,1000)
        last = (orig - 1) / 2
        beg = "false"
        game()
    else:
        exit()

def multiplayer():
    print ("There are " + str(orig) + " coins on the table")
    while orig != 0:
        player1()
        if orig == 0:
            print("Player one wins!!")
            playagain()
        player2()
    print("Player two wins!!")
    playagain()

def game():
    print ("There are " + str(orig) + " coins on the table")
    while orig != 0:
        player1()
        if orig == 0:
            print("Player one wins!!")
            playagain()
        player2()
    print("Player two wins!!")
    playagain()
    
game()
