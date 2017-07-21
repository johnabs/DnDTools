import os
from appJar import gui
import random

cwd = os.getcwd()
#Code for rolling dice, given the number of dice and the type of dice
def diceRoll(ndice, dtype):
   total=ndice*random.randrange(1,dtype+1);
   return(total)

#Code for pulling monster text files to the dropdown menu
def monsterMenu():
    menu=[]
    for files in os.listdir(cwd+"/Monster_Data"):
        if files.endswith(".txt"):
          menu.append(files)  
    return(sorted(menu))
    
#Code for pulling monster text files to the dropdown menu
def playerMenu():
    menu=[]
    for files in os.listdir(cwd+"/Player_Data"):
        if files.endswith(".txt"):
          menu.append(files)  
    return(sorted(menu))

#Code for rolling dice, given the number of dice and the type of dice
def importMonster(monName):
    monFile=open(os.path.join(cwd+"/Monster_Data", monName+"."+"txt"), "r")
    monData=[]
    for line in monFile:
        if line != "Attack:\n":
            monData.append(line)
    return(monData)



#Allows the DM to select which monsters they want to use for the encounters.
def selectmonsters():    
    testlist={}
    outlist=[]
    mlist=monsterMenu() 
    def screen3(button):
        if button == "Cancel":
            app3.stop()
        elif button == "Apply":
            testlist= app3.getOptionBox("Select your monsters:")
            for elements in list(testlist.items()):
                if elements[1]:
                   outlist.append(elements[0]) 
            print(sorted(outlist))
            app3.stop()
       #     main()
    app3=gui()
    app3.addTickOptionBox("Select your monsters:", mlist)         
    app3.addButtons(["Apply", "Cancel"], screen3)
    app3.go()


#Allows the DM to select which Players are playing.
def selectplayers():    
    testlist={}
    outlist=[]
    def screen3(button):
        if button == "Cancel":
            app3.stop()
        elif button == "Apply":
            testlist= app3.getOptionBox("Select your players:")
            for elements in list(testlist.items()):
                if elements[1]:
                   outlist.append(elements[0]) 
            print(sorted(outlist))
            app3.stop()
            main()
    plist=playerMenu()
    app3=gui()
    app3.addTickOptionBox("Select your players:", plist)         
    app3.addButtons(["Apply", "Cancel"], screen3)
    app3.go()


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
    app2.addLabelEntry("Attack1")
    app2.addLabelEntry("Attack2")
    app2.addLabelEntry("Attack3")
    app2.addLabelEntry("Attack4")
    app2.addLabelEntry("Attack5")
    app2.addLabelEntry("Attack6")
    app2.setFocus("Name") 
    def screen2(button):
        if button == "Cancel":
            app2.stop()
        elif button == "Next Monster":
            name=app2.getEntry("Name")
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

def main():
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
            hitRoll=diceRoll(1,20);
            print(hitRoll)
        elif button == "Select Monsters": 
            app.stop()
            selectmonsters()
        elif button == "Select Players": 
            app.stop()
            selectplayers()
        else:
            print(BUGFIXTIME)
    app.addButtons(["Input Player Data", "Input Monster Data","Select Players", "Select Monsters", "Begin Combat","Roll Dice", "Cancel"], screen1)
    app.go()

main()
