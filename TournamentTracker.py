import csv

participantList = []
exitVar = 0
validInput = 0

def signUp():
    print("Participant Sign Up\n====================")
    validInput = 0

    name = input("Participant name: ")

    while validInput == 0:
        slot = input(f"Starting slot #[1-{numParticipants}]: ")

        if not slot.isnumeric():                            #if slot is not all numbers
            print("Invalid input, please enter a number")
        elif int(slot) > numParticipants or int(slot) < 1:
            print("Error, that slot does not exist")
        elif participantList[int(slot)-1] != 'None':             #if slot is occupied
            print(f"Slot #{slot} is taken, try another")
        else:
            validInput = 1
            participantList[int(slot)-1] = name

def cancelSignUp():
    print("Participant Cancellation\n========================")
    validInput = 0

    while validInput == 0:
        slot = input(f"Starting slot #[1-{numParticipants}]: ")
        name = input("Participant name: ")

        if (not slot.isnumeric()):
            print("Invalid input, slot must be a number")
        elif int(slot) > numParticipants or int(slot) < 1:
            print(f"Invalid input, slot must be a number in range [1-{numParticipants}]")
        elif participantList[int(slot)-1] != name:
            print(f"Error, {name} is not in that slot.")
        else:
            validInput = 1
            participantList[int(slot)-1] = 'None'
            print(f"Success, {name} has been removed from slot #{slot}")

def viewParticipants():
    print("View Participants\n=================")
    validInput = 0

    while validInput == 0:
        slot = input(f"Starting slot #[1-{numParticipants}]: ")

        if not slot.isnumeric():
            print("Error, please enter a number for slot")
        elif int(slot) > numParticipants or int(slot) < 1:
            print(f"Invalid input, slot must be a number in range [1-{numParticipants}]")
        else:
            validInput = 1
    
    print("Starting Slot: Participant")
    slot = int(slot)

    if slot < 6 and slot > numParticipants - 6:
        for i in range(0, numParticipants):
            print(f"{i+1}: {participantList[i]}")
    elif slot < 6:
        for i in range(0, slot+5):
            print(f"{i+1}: {participantList[i]}")
    elif slot > numParticipants - 5:
        for i in range(slot-6, numParticipants):
            print(f"{i+1}: {participantList[i]}")
    else:
        for i in range(slot-6, slot+5):
            print(f"{i+1}: {participantList[i]}")


def saveChanges():
    print("Save Changes\n============")
    validInput = 0

    while validInput == 0:                   #input validation
        answer = input("Save your changes to CSV? [y/n] ")

        if answer == 'y':
            validInput = 1
            #save here
            file = open('TournamentSlots.csv', 'w')
            write = csv.writer(file)
            write.writerow(participantList)
            print("Your changes were saved.")
        elif answer == 'n':
            validInput = 1
            print("Your changes were not saved.")
        else:
            print("Invalid answer, please try again.")

def exit():
    print("Exit\n=====\nAny unsaved changes will be lost.")
    validInput = 0
    global exitVar

    while validInput == 0:                  #input validation
        answer = input("Are you sure you want to exit? [y/n]")

        if answer == 'y':
            validInput = 1
            exitVar = 1
        elif answer == 'n':
            validInput = 1
        else:
            print("Invalid answer, please try again.")



#start up
print("Welcome to Tournaments R Us\n============================")
while validInput == 0:                      #input validation
    numParticipants = input("Enter the number of participants: ")
    if not numParticipants.isnumeric():
            print("Error, please enter a number")
    else:
        validInput = 1
        numParticipants = int(numParticipants)

for i in range(0, numParticipants):         #populate participant list
    participantList.append('None')

print(f"There are {numParticipants} slots available")

#Main program loop
while exitVar == 0:   
    menuInput = 0

    print("""Participant Menu
    ================
    1. Sign Up
    2. Cancel Sign Up
    3. View Participants
    4. Save Changes
    5. Exit
    """)
    menuInput = input("What do you want to do? Enter [1-5] ")
    
    if menuInput.isnumeric():               #input validation
        menuInput = int(menuInput)
    else:
        print("Invalid input.")

    if menuInput == 1:
        signUp()
    elif menuInput == 2:
        cancelSignUp()
    elif menuInput == 3:
        viewParticipants()
    elif menuInput == 4:
        saveChanges()
    elif menuInput == 5:
        exit()

print("Goodbye!")
    