from random import *

d0=["=========="]
d1=["_         ","|         ","|         ","|         ","|         ","=========="]
d2=["_______   ","|         ","|         ","|         ","|         ","=========="]
d3=["_______   ","|     |   ","|         ","|         ","|         ","=========="]
d4=["_______   ","|     |   ","|     0   ","|         ","|         ","=========="]
d5=["_______   ","|     |   ","|     0   ","|     I   ","|         ","=========="]
d6=["_______   ","|     |   ","|     0   ","|    -I   ","|         ","=========="]
d7=["_______   ","|     |   ","|     0   ","|    -I-  ","|         ","=========="]
d8=["_______   ","|     |   ","|     0   ","|    -I-  ","|    /    ","=========="]
d9=["_______   ","|     |   ","|     0   ","|    -I-  ","|    / \  ","=========="]

dico=["easy","code","learning","potatoes","consumation","explain"]
world=dico[randrange(0,len(dico))]

def afficherDessin(nbCharWrong):
    if(nbCharWrong==1):
        print(d0[0])
    elif(nbCharWrong==2):
        for i in range(len(d1)):print(d1[i])
    elif(nbCharWrong==3):
        for i in range(len(d2)):print(d2[i])
    elif(nbCharWrong==4):
        for i in range(len(d3)):print(d3[i])
    elif(nbCharWrong==5):
        for i in range(len(d4)):print(d4[i])
    elif(nbCharWrong==6):
        for i in range(len(d5)):print(d5[i])
    elif(nbCharWrong==7):
        for i in range(len(d6)):print(d6[i])
    elif(nbCharWrong==8):
        for i in range(len(d7)):print(d7[i])
    elif(nbCharWrong==9):
        for i in range(len(d8)):print(d8[i])
    elif(nbCharWrong==10):
        for i in range(len(d9)):print(d9[i])

def update(lettresVrai):
    guessWorld=[]
    for i in lettresVrai:
        if(i==''):
            guessWorld+="_ "
        else:
            guessWorld+=i
    for i in guessWorld:
        print(i,sep='',end='')
    print()
    return guessWorld

def prompt(lettresFausses, lettresVrai):
    afficherDessin(len(lettresFausses))
    print(lettresFausses)
    print("Il vous reste %d coups"%(10-len(lettresFausses)))
    lettresVrai = update(lettresVrai)
    lettre = input("\n:\>")
    return lettre

def addCharAtGoodPos(charToAdd, worldWithBlank):
    if(worldWithBlank[world.index(charToAdd)] == charToAdd):#if the letter is alerdy in the world
        worldWithBlank[world.index(charToAdd, world.index(charToAdd))]=charToAdd
        print("Le car est deja dedan")
    else:
        worldWithBlank[world.index(charToAdd)]=charToAdd
        print("Il va etre ajouter")
    


wrongChars = []
trueChars = ['']*len(world)
trueChars[0] = world[0]
trueChars[-1] = world[-1]

compareWorld=world[:]
compareWorld=list(compareWorld)
del compareWorld[0]
del compareWorld[-1]

while( trueChars != list(world) and len(wrongChars) <= 10):
    lettre = prompt(wrongChars, trueChars)
    
    if(lettre in compareWorld):
        print("\n--OK--\n")
        addCharAtGoodPos(lettre, trueChars)
        compareWorld.remove(lettre)
    elif(not lettre in compareWorld):
        if(not lettre in wrongChars):
            wrongChars.append(lettre)
        
print("END")
