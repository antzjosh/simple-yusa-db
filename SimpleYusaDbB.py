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
    userLabels = ('First Name', 'Second Name', 'Email Address', 'Mobile #', 'Address')
    
    fname = input(userLabels[0] + ': ')
    sname = input(userLabels[1] + ': ')
    email = input(userLabels[2] + ': ')
    mobile = input(userLabels[3] + ': ')
    addr = input(userLabels[4] + ': ')
    
    userData = [fname, sname, email, mobile, addr]
    
    displayUser = "Hi, my name is " + userData[0] + " " + userData[1]
    displayAddr = "\nI live at " + userData[4]
    displayContacts = ".\nMy contacts are:\n\t-Email: " + userData[2] + "\n\t-Mobile: " + userData[3]
    
    print(displayUser + displayAddr + displayContacts)

main()
