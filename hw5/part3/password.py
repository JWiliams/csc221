import re

# Author <Javian Williams>

# Strong Password Detection


def strong_password(string):
    passRegex = re.compile(r'[a-zA-Z0-9]{8,}')
    mo = passRegex.search(string)
    if mo == None:
        print('Bad Password')

    else:
        print('Good Password')

strong_password('ThisIsAGoodPassword1')
    
