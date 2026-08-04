s=input('Enter name:')
if len(s) %2==0:
    print(s[:len(s)//2])
else:
    print(s[len(s)//2:])