import re

while True:
    s = input()
    re_copmile = re.compile(r'^<*([a-zA-Z ]*)*>*\s*\S+@\w+\.\w+$')
    if re_copmile.match(s) != None:
        m = re_copmile.match(s)
        print(m.groups())
    else:
        print('not match')

