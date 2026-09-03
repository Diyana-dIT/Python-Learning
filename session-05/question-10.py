a=input('Enter short text:')
b=input('Enter long text:')
a=a.split()
b=b.split()
for i in a:
    if i in b:
        print(i)
        
