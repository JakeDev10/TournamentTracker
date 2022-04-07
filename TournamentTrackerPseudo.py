'''
declare participantList

function signUp()
    print menu
    validInput = 0

    name = input participant name

    while validInput == 0
        slot = input desired starting slot [1-numParticipants]

        if not slot.isnumeric()
            print "Invalid input, please enter a number"
        else if participantList[slot-1] != 'None'
            print "Slot # {slot} is taken, try another"
        else
            validInput = 1
            participantList[slot-1] = name
            



function cancelSignUp()
    print signUpMenu


function viewParticipants()

function saveChanges()

function exit()

#start up
print startupMenu
numParticipants = input number of participants
for i in 0-participants             #populate participant list
    participantList.add('None')



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
    
'''