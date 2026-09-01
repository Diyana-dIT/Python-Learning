a=input('Emter Taxt:')
letters=0
upper=0
lower=0
numbers=0
spaces=0 
special=0
for i in a:
    if i.isalpha():
        letters+=1
    if i.isupper():
          upper+=1
    if i.islower():
        lower+=1
    if i.isdigit():
        numbers+=1
    if i.isspace():
        spaces+=1 
if not i.isalpha() and not i.isdigit() and not i.isspace():
    special += 1
print('Letters:', letters)
print('Uppercase:', upper)
print('Lowercase:', lower)
print('Numbers:', numbers)
print('Spaces:', spaces)
print('Special:', special)
        
        
        
