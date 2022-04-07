
participantList = []
exitVar = 0

def signUp():
    print("Participant Sign Up\n====================")
    validInput = 0

    name = input("Participant name: ")

    while validInput == 0:
        slot = input(f"desired starting slot [1-{numParticipants}]")

        if not slot.isnumeric():                            #if slot is not all numbers
            print("Invalid input, please enter a number")
        elif int(slot) > numParticipants:
            print("There's not that many slots, try again")
        elif participantList[int(slot)-1] != 'None':             #if slot is occupied
            print(f"Slot #{slot} is taken, try another")
        else:
            validInput = 1
            participantList[int(slot)-1] = name
'''
function cancelSignUp()
    print signUpHeader
    validInput = 0

    while validInput == 0
        slot = input slot of player to remove
        name = input name of player to remove

        if participantList[slot-1] != name
            print "Error, {name} is not in that slot."
        else
            validInput = 1
            participantList[slot-1] = 'None'
            print "Success, {name} has been removed from slot #{slot}"

function viewParticipants()
    print participantHeader
    validInput = 0

    while validInput = 0
        slot = input slot to view
        if slot is not numeric
            print "Error, please enter a number for slot"
        else
            validInput = 1
    
    print "Starting Slot: Participant"

    if slot < 6
        for i in range(0, slot)
            print "{i+1}: {participantList[i]}"
    else if slot > numParticipants - 5
        for i in range(slot-6, numParticipants)
            print "{i+1}: {participantList[i]}"
    else
        for i in range(slot-6, slot+4)
            print "{i+1}: {participantList[i]}"


function saveChanges()
    print saveChangeHeader
    answer = ''
    validInput = 0

    while validInput = 0
        answer = input "Save your changes to csv? [y/n]"

        if answer = 'y' or 'n'
            validInput = 1
        else
            print "Invalid answer, please try again."
    
    if answer = 'y'
        save participantList to csv
        print "Your changes were saved."
    else
        print "Your changes were not saved."

function exit()
    print exitHeader
    answer = ''
    validInput = 0
    global exitVar

    while validInput = 0
        answer = input "Are you sure you want to exit? [y/n]"

        if answer = 'y' or 'n'
            validInput = 1
        else
            print "Invalid answer, please try again."

    if answer = 'y'
        exitVar = 1

'''

#start up
print("Welcome to Tournaments R Us\n============================")
numParticipants = int(input("Enter the number of participants: "))

for i in range(0, numParticipants):             #populate participant list
    participantList.append('None')

print(f"There are {numParticipants} slots available")

signUp()
signUp()
signUp()

print(f"Here's the list: {participantList}")

'''


while exitVar == 0   
    menuInput = 0

    #main menu
    print mainMenu
    menuInput = get input for menu

    if menuInput == 1
        signUp()
    else if menuInput == 2
        cancelSignUp()
    else if menuInput == 3
        viewParticipants()
    else if menuInput == 4
        saveChanges()
    else if menuInput == 5
        exit()

print "Goodbye!"
    
'''