from random import *
"""
The list d0 to d9 are the list content drawing
chmot : LIST who content the letters of the word i have randomly choosen
mot : STR the randomly choosen word
usr : LIST the list of the letters who was be proposed by the player it content the first and the last caracter
chmotcompare : LIST a copy of chmot but without the first and the last character
localchmot : LIST the cariable i used when there are two same letter in a word
lettre : STR the letter proposed by the player
lettrevrai : LIST of good letters of the player
faux : INT number of error who make the player
lettresfausses : LiST of the falses letters of the player
in this code i use many differant listes, not because i need it, only for make the code more easy to read, so have fun ;p
"""
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
mot=dico[randrange(0,len(dico))]
#ci dessu mon choix aleatoire de mot

chmot=[]
for i in mot: chmot.append(i)
#ci dessu je convertis le mot en liste de lettre, pour le manipule plus facilement

#print(mot,"\n",chmot,"\n")

print("Le mot que vous cherchez est composé de",len(mot),"lettres.")
print(chmot[0],"_ "*(len(mot)-2),chmot[len(mot)-1])

usr=[""]*(len(chmot))
#print("usr",usr)
usr[0]=chmot[0]
#print("usr",usr)
usr[-1]=chmot[-1]
#print("usr:",usr)

faux=0
lettresfauses=[]#j'ai ajouter ca a la fin pour le fun

chmotcompare=chmot[:]
del chmotcompare[0]
del chmotcompare[-1]
#print("\n chmotcompre:",chmotcompare,"\n")

while (usr != chmot and faux < 10):
    lettre = input(":\>")
    if(lettre in chmotcompare):
        place = int(chmot.index(lettre))
        if(not usr[place] == ''):
            localchmot=chmot[:]
            #print("localchmot",localchmot)
            localchmot[chmot.index(lettre)]=(0)
            place=int(localchmot.index(lettre))
        usr[place]=lettre
        chmotcompare.remove(lettre)
        #print("usr:",usr)
        #print("chmotcompare:",chmotcompare)
        lettrevrai=""#il faut vider la variable a chaque fois pour la reconstruire a chque nouvelle letre juste parce que sinon c pas pratique pour remplacer les emplacement vides par des _
        for i in usr:
            if(i==''):
                lettrevrai+="_ "
            else:
                lettrevrai+=i
        print("\n",lettrevrai)
    elif(not lettre in chmotcompare):
        faux+=1
        """
        Okay it's sooo so so so ugly, but in py3 there not have switch, and i don't maka a duble list ... sorrryyyy everyone it's too sad
        """
        if(faux==1):print(d0[0],"\n")
        elif(faux==2):
            for i in range(len(d1)):
                print(d1[i])
            print("\n")
        elif(faux==3):
            for i in range(len(d2)):print(d2[i])
            print("\n")
        elif(faux==4):
            for i in range(len(d3)):print(d3[i])
            print("\n")
        elif(faux==5):
            for i in range(len(d4)):print(d4[i])
            print("\n")
        elif(faux==6):
            for i in range(len(d5)):print(d5[i])
            print("\n")
        elif(faux==7):
            for i in range(len(d6)):print(d6[i])
            print("\n")
        elif(faux==8):
            for i in range(len(d7)):print(d7[i])
            print("\n")
        elif(faux==9):
            for i in range(len(d8)):print(d8[i])
            print("\n")
        elif(faux==10):
            for i in range(len(d9)):print(d9[i])
            print("GAME OVER\n")
        print("\nnon il vous reste",10-faux,"essais.")
        lettresfauses.append(lettre)
        print("mauvaises lettres :",lettresfauses)
        lettrevrai=""#il faut vider la variable a chaque fois pour la reconstruire a chque nouvelle letre juste parce que sinon c pas pratique pour remplacer les emplacement vides par des _
        for i in usr:
            if(i==''):
                lettrevrai+="_ "
            else:
                lettrevrai+=i
        print("\n",lettrevrai)
if(faux >=10):
    print("\nVouw avez PERDU, le mot que vous cherchiez etait",mot,".")
else:
    print("\nVous avez trouver le bon mot Félicitation !")
