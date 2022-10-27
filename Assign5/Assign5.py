#1. The benefits of using my programs features include the fact that they are very familiar. The new feature, which is the ability to import files, is also intuitive and helpful for orgaanizing work. People like Abi and Pat will find this easy to use, and Tim
#   will see the use of the function and be interested in it.

#2. The cost of using my program is the learning curve, which is low. However, the new feature that I added (file import) may make someone like Abi hesitate to use it as there are some unknowns. There is a tutorial to help mitigate this.

#3. Each button will do exactly what it says, so there is a limited amount of information on the screen at the start. However, as the program is used (ex: using the import function or creating a note) new options are added for the user to interact with. Nothing
#   unnecessary is given to the user, so only the info they wanted is given.

#4. Each button is clearly labeled to make it as familiar as possible, so even people like Abi will feel comfortable in the program. Many of the features are also similar to other popular applications in functionality.

#5. The user is easily able to delete anything they have typed in the program, so people like Abi or Pat can avoid being overwhelmed.

#6. The application starts off with a tutorial that can be hidden. The buttons are also clearly labeled, so people like Abi will have a clear explanation of each of the features. People like Tim and Pat can instantly hide the tutorial and explore on their own.

#7. The application will have nothing except for a tutorial when it opens, so any approach can be taken when using the program. It is fully up to the user to proceed how they want.

#8. The application encourages tinkering mindfully by putting a limit to how many notes can be created. The program also allows you to bring the tutorial up whenever, so you can see what a button does rather than messing with it forever. This can help people like Tim
#   stay on task by giving them the information they want.

#Quality 1. The first quality attribute I focused on was reliability, which I did by making sure everything ran smoothly with no hiccups. Everything loads quickly and I have not been able to make the program slow down. I did this by keeping each individual process simple.

#Quality 2. The second quality attribute I focused on was flexibility, which I did by allowing the program to accept almost any file type.

#Quality 3. The last attribute I focused on was Integrity, which I did by making sure that it was very hard to crash the program. Each button does what it is supposed to, and I have not experienced any crashes in my testing.

import time
from tkinter import *
from tkinter.ttk import *
import sys

window = Tk()
counter = 0
yPlace = 100
warningCheck = False
currentFileInput = ''
fileContent = ''
tutorialHidden = True

#create entry window
inputFile = Entry(window, width = 50)

tutorial = Text(window, height = 5, width = 50, wrap = WORD)



def saveInput(userInput: Entry):
    with open('exampleSave.txt', 'w') as wf:
        wf.write(userInput.get(1.0, "end-1c"))

    wf.close()
    return



#make a new note if there is room
def makeNote():
    global warningCheck
    global counter
    xPlace = 200
    global yPlace
    global fileContent

    #creates input box inside window (this is the note)
    if counter == 0:
        input = Text(window, height = 10, width = 20, wrap = WORD)
        input.place(x = xPlace, y = yPlace)
        input.insert('end', fileContent)

        saveButton = Button(window, text = "Save", command = saveInput(input))
        saveButton.place(x = xPlace + 45, y = yPlace + 165)

        counter += 1

    elif counter < 3:
        input = Text(window, height = 10, width = 20, wrap = WORD)
        xPlace = xPlace + (250 * counter)
        input.place(x = xPlace, y = yPlace)
        input.insert('end', fileContent)

        saveButton = Button(window, text = "Save", command = saveInput(input))
        saveButton.place(x = xPlace + 45, y = yPlace + 165)

        counter += 1

    #update yPlace prior to 4 so that warningCheck works
    elif counter == 3:
        input = Text(window, height = 10, width = 20, wrap = WORD)
        xPlace = xPlace + (250 * counter)
        input.place(x = xPlace, y = yPlace)
        input.insert('end', fileContent)

        saveButton = Button(window, text = "Save", command = saveInput(input))
        saveButton.place(x = xPlace + 45, y = yPlace + 165)

        counter += 1
        yPlace = yPlace + 200

    #make sure it does not overprint the warning
    elif warningCheck == True:
        pass

    #make warning that the max number of notes has been reached
    elif yPlace > 500:
        warning = Label(window, width = 50, text = "You have created the max number of notes!")
        warning.pack()
        warningCheck = True

    #creates a new row of notes
    elif counter == 4:
        counter = 0
        input = Text(window, height = 10, width = 20, wrap = WORD)
        input.place(x = xPlace, y = yPlace)
        input.insert('end', fileContent)

        saveButton = Button(window, text = "Save", command = saveInput(input))
        saveButton.place(x = xPlace + 45, y = yPlace + 165)

        counter += 1

    #clear file content so that the next note created does not have unwanted text
    fileContent = ''



#take and store user input
def acceptInput():
    global currentFileInput
    global fileContent
    global inputFile

    currentFileInput = inputFile.get()
    
    with open(currentFileInput, 'r') as rf:
        fileContent = rf.readline()
    
    rf.close()
    makeNote()



#take input from the user for the file name
def importFile():
    global inputFile

    inputFile.place(x = 760, y = 25)
    
    takeInput = Button(window, text = "Import File", command = acceptInput)  
    takeInput.place(x = 875, y = 50)


#hide the tutorial box
def hideTutorial():
    global tutorial
    global tutorialHidden

    if tutorialHidden == False:
        tutorial.place(x = 675, y = 30)
        tutorialHidden = True

    elif tutorialHidden == True:
        tutorial.place_forget()
        tutorialHidden = False



#basic program loop
while True:
    window.geometry('1280x720')
    window.resizable(0, 0)

    #calls makeNote function to create a small note window when clicked
    noteButton = Button(window, text = 'New Note', command = makeNote)
    noteButton.place(x = 800, y = 0)

    importButton = Button(window, text = "Import", command = importFile)
    importButton.place(x = 875, y = 0)

    tutorial.place(x = 675, y = 30)
    tutorial.insert('end', "Use the 'New Note' button to create a note on the page. This will let you type anything! This will also create a save button to save your input in a file. Use the 'Import' button to take the name of a file to place the text of a file in a new note!")

    closeTutorial = Button(window, text = "Toggle Tutorial", command = hideTutorial)
    closeTutorial.place(x = 950, y = 0)

    window.mainloop()

    break

