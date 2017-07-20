import os
from appJar import gui

#Function responsible for writing player data to files.
def screen1(button):
    if button == "Cancel":
        app.stop()
    elif button == "Submit": 
        playerNum = app.getEntry("Please insert the number of player characters:")
        for x in playerNum:
            playerInput()
        print(playerNum)
        app.stop()



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
            playerfile=open(os.path.join(cwd, name + "." + "txt"), 'r+')  
            playerfile.write(name+"\n")
            playerfile.write(stre+"\n")
            playerfile.write(dex+"\n")
            playerfile.write(con+"\n")
            playerfile.write(intel+"\n")
            playerfile.write(wis+"\n")
            playerfile.write(chari+"\n")
            app2.stop()    
    app2.addButtons(["Next Player", "Cancel"], screen2)
    app2.go()        
    
cwd = os.getcwd()
print(cwd)
app = gui("Setting Up Your Campaign", "400x200")
app.addLabelEntry("Please insert the number of player characters:")
app.setFocus("Please insert the number of player characters:")
app.addButtons(["Submit", "Cancel"], screen1)
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

