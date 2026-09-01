a=input('Enter password:')

upper=False
lower=False
digit=False
special=False

if len(a)<8:
    print('need 8 characters')
    
for i in a:
    if i.isupper():
        upper=True
    if i.islower():
            lower=True
    if i.isdigit():
                digit=True
    if i in '@#$%^&*!':
                    special=True
if upper==False:
    print('Need upper')
if lower==False:
    print('Need lower')
if digit==False:
    print('Need digit')
if special==False:
    print('Need special') 
