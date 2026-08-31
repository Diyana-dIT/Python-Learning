password=input('Password: ')

upper=False
lower=False
digit=False
special=False

for x in password:
    if x.isupper():
        upper=True
    if x.islower():
        lower=True
    if x.isdigit():
        digit=True
    if x in '%$#@':
        special=True
        
if len(password)< 8:
    print('Need 8 characters')
if upper==False:
    print('Need uppercase')
if lower==False:
    print('Need lowercase')
if digit==False:
    print('Need number')
if special==False:
    print('Need special')
if len(password)>=8 and upper and lower and digit and special:
    print('Valid')