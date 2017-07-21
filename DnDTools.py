import os
from appJar import gui
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


cwd = os.getcwd()
print(cwd)
app = gui("Setting Up Your Campaign", "400x200")
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
    else:
        app.stop()
app.addButtons(["Input Player Data", "Input Monster Data", "Select Monsters", "Begin Combat", "Cancel"], screen1)
app.go()



def combatOrder():
    app=gui()

    app.setBg("DarkKhaki")
    app.setGeometry(280,400)

    app.startPagedWindow("Main Title")
    app.startPage()
    app.addLabel("l13", "Label 1")
    app.stopPage()

    app.startPage()
    app.addLabel("l21", "Label 2")
    app.stopPage()

    app.startPage()
    app.addLabel("l3", "Label 3")
    app.stopPage()

    app.startPage()
    app.addLabel("l4", "Label 4")
    app.stopPage()
    app.stopPagedWindow()

    app.go()

