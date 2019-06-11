'''def IsPhoneNumber(text):
    if (len(text)!= 12):
        print("not 12 numbers long");
        return False
    if ( not text[0:3].isdecimal() or not text[4:7].isdecimal() or not text[8:12].isdecimal()):
        print("between the numbers there's a differtent type of character")
        return False
    if (text[3]!="-" or text[7]!="-"):
        print("lacks hyphens or aren't in their place")
        return False
    return True'''

import re

def IsPhoneNumber(text):
    phoneRegex= re.compile(r'(\d{3})-(\d{3}-\d{4})')
    mo=foundNumber=phoneRegex.search(text) #mo=Match object, es como se llama normalmente a las busquedas del regex
    return foundNumber.groups()
