def get_values():
    a=[]
    n=int(input('Enter number: '))

    for i in range(n):
        b=input('Enter value: ')

        if b=='':
            print('Empty value is not allowed')
        else:
            a.append(b)

    return a


def add_unique(a,b):
    for i in range(len(a)):
        if a[i].lower()==b.lower():
            return False,i

    a.append(b)
    return True,len(a)-1


def process_values(a):
    b=[]
    c=[]
    d=[]

    for i in a:
        x,y=add_unique(b,i)

        if x==True:
            c.append(i)
            print(i,'-> new value, added to list')
        else:
            d.append(i)
            print(i,'-> duplicate, first position:',y+1)

    return b,c,d


def show_report(a,b,c):
    print()
    print('Unique values:',a)
    print('Duplicate values:',len(c))
    print('Unique values count:',len(a))
    print('First position:')

    for i in range(len(a)):
        print(a[i],'->',a[i])


a=get_values()
b,c,d=process_values(a)
show_report(b,c,d)