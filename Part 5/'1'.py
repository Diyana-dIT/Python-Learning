password=input('Enter password: ')
upper=False
lower=False
digit=False
special=False
if len(password)<8:
    print('Need 8 characters')
for x in password:
    if x.isupper():
        upper = True
    if x.islower():
        lower = True
    if x.isdigit():
        digit = True
    if x in ' % $ # @':
        special=True
if upper==False:
    print('No uppercase')
if lower==False:
    print('No lowercase')
if digit==False:
    print('No number')
if special==False:
    print('No special')
if len(password) >= 8 and upper and lower and digit and special:
    print('Yes :)')
