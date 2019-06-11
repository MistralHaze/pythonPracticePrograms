#! python3
#very simple program to test and remember python
import sys
import pyperclip

storedPasswords = { 'awfulWebsite' : "whyDoIEvenCare",
                    'portfolio' : "trustInYourselfYouDumbyDoo",
                    'instagram': 'uSexyBro',
                    'university' : 'passwordChangeNo6'
}

if len(sys.argv) <=1:
    print ("you need to tell me which password you need dumbass")
    sys.exit()

#sys argv stores in the first place the name of the program
#In the second slot it stores the info passed from the command line
account = sys.argv[1]
found = False

'''for strPassword in storedPasswords:
    if (strPassword == account):
        print(storedPasswords[account])
        found=True'''

#simpler version
if account in storedPasswords:
    print(storedPasswords[account])
    found=True
    pyperclip.copy(storedPasswords[account])

if (not found):
    print ("Are you sure you wrote that right or that the password is stored?")

