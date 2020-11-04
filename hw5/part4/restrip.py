import re

#Author <Javian Williams>


def restrip(string, chars = None):
    if chars == None:
        stripedRegex = re.compile(r'(\s+)(.*)(\s+)')
        mo = stripedRegex.search(string)
        print(mo.group(2))
    else:
        a = chars
        stripedRegex = re.compile(rf"([^{a}$]+)(.*)")
        mo1 = stripedRegex.search(string)
        print(mo1.group(1))

restrip('xxxxxpiexxxx', 'x')
