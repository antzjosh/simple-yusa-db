############################################################################################################
#   Read Data from user input then store the input data in a list.                                         #
#   A tuple will contain the labels.                                                                       #
#   This version will be uploaded to github and there will be collaborations to improve it.                #
#   The goal is to be able to turn this into a fully functional Database through github collaboration      #
#   There will be a command line version as well as a GUI version                                          #
#                                                                                                          #
#   Author: Creekly.smol                                                                                   #
#   Version: 1.0                                                                                           #
#   Date: 07/05/17                                                                                         #
############################################################################################################
def initLabels():
    #Tuple containing the labels
    uLabels = ('First Name', 'Second Name', 'Email Address', 'Mobile #', 'Address')
    return uLabels;
    

def displayOutput(uData):
    displayUser = "Hi, my name is " + uData[0] + " " + uData[1]
    displayAddr = "\nI live at " + uData[4]
    displayContacts = ".\nMy contacts are:\n\t-Email: " + uData[2] + "\n\t-Mobile: " + uData[3]
    
def main():
    #Initialize labels 
    userLabels = initLabels()
    
    #Create List for holding actual data entered by user
    userData = []

    #Display user promts from userLabels Tuple and save user input into userData List
    for label in userLabels:
        userData.append(input(label + ': '))
    
    #Format output to be displayed
    displayOutput(userData)
    #Display the output
    print(displayUser + displayAddr + displayContacts)

main()
