import pyperclip
import re

phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  #AreaCode none() or ()
        (\s|-|\.)?          # ' ' '-' '.'
        (\d{3})             # three digits
        (\s|-|\.)?          # ' ' '-' '.'
        (\d{4})             # four digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))? #' 'ext. (ddddd)
        )''',re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+ #At least one of these characters
        @                 #'At' Symbol
        [a-zA-Z0-9.-]+     #Domain Name
        (\.[a-zA-Z]{2,4}) #dot someting
        )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
# Find matches in clipboard text
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(group[0])

# Copy results to the clipboard.
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
