import os
from operator import itemgetter
import math
from appJar import gui
import random

selectedPlayers=[]
selectedMonsters=[]
cwd = os.getcwd()
combatlist=[]
#Code for rolling dice, given the number of dice and the type of dice
def diceRoll(ndice, dtype):
    total=0;
    for i in range(0, ndice):
        total+=random.randrange(1,dtype+1)
    return(total)

#Code for pulling monster text files to the dropdown menu
def monsterMenu():
    menu=[]
    for files in os.listdir(cwd+"/Monster_Data"):
        if files.endswith(".txt"):
          menu.append(files)  
    return(sorted(menu))
    
#Code for pulling player text files to the dropdown menu
def playerMenu():
    menu=[]
    for files in os.listdir(cwd+"/Player_Data"):
        if files.endswith(".txt"):
          menu.append(files)  
    return(sorted(menu))

def monsterGen():
    for i in range(0,len(selectedMonsters)):
        for j in range(0, int(selectedMonsters[i][1])):
            combatlist.append(importMonster(selectedMonsters[i][0]))
    print(combatlist)
     




#Code for rolling dice, given the number of dice and the type of dice
def importMonster(monName):
    monFile=open(os.path.join(cwd+"/Monster_Data", monName), "r")
    monData=[]
    for line in monFile:
        if line != "Attack:\n":
            monData.append(line.strip("\n"))
    for i in range(2,8):
        monData[i]=int(monData[i])+random.randrange(-5,6)
        if monData[i]>10:
            monData[i]=int(math.floor((monData[i]-10)/2))
        elif monData[i]<10:
            monData[i]=int(math.ceil(10-(monData[i])/2))
        elif monData[i]==10:
            monData[i]=0;
    return(monData)

#Allows the DM to select which monsters they want to use for the encounters.
def selectmonsters():    
    app.showSubWindow("Select Your Monsters:")

def screen3(button):
    global selectedMonsters
    testlist={}
    outlist=[]
    if button == "Finish":
        app.hideSubWindow("Select Your Monsters:")
    elif button == "Add To Monster List":
        selectedMonsters.append([app.getOptionBox("Select Your Monsters:"),app.getEntry("Number of Monsters")]) 
        print(selectedMonsters)
    elif button == "Clear Monsters":
        selectedMonsters=[]
        combatlist=[]

#Allows the DM to select which Players are playing.
def selectplayers():    
    app.showSubWindow("Select Your Players:")

def screen4(button):
    global selectedPlayers
    testlist={}
    outlist=[]
    if button == "Finish":
        app.hideSubWindow("Select Your Players:")
    elif button == "Select":
        testlist= app.getOptionBox("Select Your Players:")
        for elements in list(testlist.items()):
            if elements[1]:
               outlist.append(elements[0]) 
        selectedPlayers=(sorted(outlist))
        app.hideSubWindow("Select Your Players:")


#Code for inputting player stats.
def playerInput():
    app2=gui("Please input the character's names and stats here:")
    app2.addLabelEntry("Name")
    app2.addLabelEntry("Strength")
    app2.addLabelEntry("Dexterity")
    app2.addLabelEntry("Constitution")
    app2.addLabelEntry("Intelligence")
    app2.addLabelEntry("Wisdom")
    app2.addLabelEntry("Charisma")
    app2.setFocus("Name") 
    def screen2(button):
        if button == "Cancel":
            app2.stop()
        elif button == "Next Player":
            name=app2.getEntry("Name")
            stre=app2.getEntry("Strength")
            dex=app2.getEntry("Dexterity")
            con=app2.getEntry("Constitution")
            intel=app2.getEntry("Intelligence")
            wis=app2.getEntry("Wisdom")
            chari=app2.getEntry("Charisma")
            playerfile=open(os.path.join(cwd+"/Player_Data", name + "." + "txt"), 'w')  
            playerfile.close()
            playerfile=open(os.path.join(cwd+"/Player_Data", name + "." + "txt"), 'r+')  
            playerfile.write(name+"\n")
            playerfile.write("Player\n")
            playerfile.write(stre+"\n")
            playerfile.write(dex+"\n")
            playerfile.write(con+"\n")
            playerfile.write(intel+"\n")
            playerfile.write(wis+"\n")
            playerfile.write(chari+"\n")
            app2.stop()    
    app2.addButtons(["Next Player", "Cancel"], screen2)
    app2.go()        
   
#Code for inputting monster stats.
def monsterInput():
    app2=gui("Please input the monster's names and stats here:")
    app2.addLabelEntry("Name")
    app2.addLabelEntry("Armor Class")
    app2.addLabelEntry("HP")
    app2.addLabelEntry("Strength")
    app2.addLabelEntry("Dexterity")
    app2.addLabelEntry("Constitution")
    app2.addLabelEntry("Intelligence")
    app2.addLabelEntry("Wisdom")
    app2.addLabelEntry("Charisma")
    app2.addLabelEntry("Attack1 Name")
    app2.addLabelEntry("Attack1 Dice Number", 9, 1)
    app2.addLabelEntry("Attack1 Dice Type", 9, 2)
    app2.addLabelEntry("Attack1 Bonus Stats", 9, 3)
    app2.addLabelEntry("Attack2 Name")
    app2.addLabelEntry("Attack2 Dice Number", 10, 1)
    app2.addLabelEntry("Attack2 Dice Type", 10, 2)
    app2.addLabelEntry("Attack2 Bonus Stats", 10, 3)
    app2.addLabelEntry("Attack3 Name")
    app2.addLabelEntry("Attack3 Dice Number", 11, 1)
    app2.addLabelEntry("Attack3 Dice Type", 11, 2)
    app2.addLabelEntry("Attack3 Bonus Stats", 11, 3)
    app2.addLabelEntry("Attack4 Name")
    app2.addLabelEntry("Attack4 Dice Number", 12, 1)
    app2.addLabelEntry("Attack4 Dice Type", 12, 2)
    app2.addLabelEntry("Attack4 Bonus Stats", 12, 3)
    app2.addLabelEntry("Attack5 Name")
    app2.addLabelEntry("Attack5 Dice Number", 13, 1)
    app2.addLabelEntry("Attack5 Dice Type", 13, 2)
    app2.addLabelEntry("Attack5 Bonus Stats", 13, 3)
    app2.addLabelEntry("Attack6 Name")
    app2.addLabelEntry("Attack6 Dice Number", 14, 1)
    app2.addLabelEntry("Attack6 Dice Type", 14, 2)
    app2.addLabelEntry("Attack6 Bonus Stats", 14, 3)
    app2.setFocus("Name") 
    def screen2(button):
        if button == "Cancel":
            app2.stop()
        elif button == "Next Monster":
            name=app2.getEntry("Name")
            ac=app2.getEntry("Armor Class")
            HP=app2.getEntry("HP")
            stre=app2.getEntry("Strength")
            dex=app2.getEntry("Dexterity")
            con=app2.getEntry("Constitution")
            intel=app2.getEntry("Intelligence")
            wis=app2.getEntry("Wisdom")
            chari=app2.getEntry("Charisma")
            attack1=app2.getEntry("Attack1")
            attack2=app2.getEntry("Attack2")
            attack3=app2.getEntry("Attack3")
            attack4=app2.getEntry("Attack4")
            attack5=app2.getEntry("Attack5")
            attack6=app2.getEntry("Attack6")
            playerfile=open(os.path.join(cwd+"/Monster_Data", name + "." + "txt"), 'w')  
            playerfile.close()
            playerfile=open(os.path.join(cwd+"/Monster_Data", name + "." + "txt"), 'r+')  
            playerfile.write(name+"\n")
            playerfile.write("Monster\n")
            playerfile.write(stre+"\n")
            playerfile.write(dex+"\n")
            playerfile.write(con+"\n")
            playerfile.write(intel+"\n")
            playerfile.write(wis+"\n")
            playerfile.write(chari+"\n")
            playerfile.write("Attack:"+attack1+"\n")
            playerfile.write("Attack:"+attack2+"\n")
            playerfile.write("Attack:"+attack3+"\n")
            playerfile.write("Attack:"+attack4+"\n")
            playerfile.write("Attack:"+attack5+"\n")
            playerfile.write("Attack:"+attack6+"\n")
            app2.stop()    
    app2.addButtons(["Next Monster", "Cancel"], screen2)
    app2.go()        

mlist=monsterMenu() 
plist=playerMenu() 
app = gui("Setting Up Your Campaign", "1920x1080")
app.addLabelEntry("Please enter the number of characters or monsters you want to add:")
def screen1(button):
    if button == "Cancel":
        app.stop()
    elif button == "Input Player Data": 
        playerNum = int(app.getEntry("Please enter the number of characters or monsters you want to add:"))
        for x in range(1, playerNum+1):
            playerInput()
        print(playerNum)
    elif button == "Input Monster Data": 
        playerNum = int(app.getEntry("Please enter the number of characters or monsters you want to add:"))
        for x in range(1, playerNum+1):
            monsterInput()
        print(playerNum)
    elif button == "Roll Dice": 
        hitRoll=diceRoll(2,20);
        print(hitRoll)
    elif button == "Select Monsters": 
        selectmonsters()
        print(selectedMonsters)
    elif button == "Select Players": 
        selectplayers()
    elif button == "Begin Combat":
        monsterGen()
    else:
        print(BUGFIXTIME)

app.startSubWindow("Select Your Monsters:")
app.addOptionBox("Select Your Monsters:", mlist)         
app.addLabelEntry("Number of Monsters")
app.addButtons(["Add To Monster List", "Clear Monsters", "Finish"], screen3)
app.stopSubWindow()

app.startSubWindow("Select Your Players:")
app.addTickOptionBox("Select Your Players:", plist)         
app.addButtons(["Select"], screen4)
app.stopSubWindow()

app.addButtons(["Input Player Data", "Input Monster Data","Select Players", "Select Monsters", "Begin Combat","Roll Dice", "Cancel"], screen1)
app.go()

