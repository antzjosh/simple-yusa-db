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

def main():
    #Tuple containing the labels
    userLabels = ('First Name', 'Second Name', 'Email Address', 'Mobile #', 'Address')
    
    #Create List for holding actual data entered by user
    userData = []

    #Display user promts from userLabels Tuple and save user input into userData List
    for label in userLabels:
        userData.append(input(label + ': '))
    
    #Format output to be displayed
    displayUser = "Hi, my name is " + userData[0] + " " + userData[1]
    displayAddr = "\nI live at " + userData[4]
    displayContacts = ".\nMy contacts are:\n\t-Email: " + userData[2] + "\n\t-Mobile: " + userData[3]
    
    #Display the output
    print(displayUser + displayAddr + displayContacts)

main()
