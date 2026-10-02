def calculate_balance(a):
    d={}

    for i in a:
        b=i.strip().split(',')
        name=b[0]
        kind=b[1]
        money=int(b[2])

        if name not in d:
            d[name]=0

        if kind=='deposit':
            d[name]=d[name]+money

        elif kind=='withdraw' and money<=d[name]:
            d[name]=d[name]-money

    return d


def total_deposits(a):
    d={}

    for i in a:
        b=i.strip().split(',')

        if b[0] not in d:
            d[b[0]]=0

        if b[1]=='deposit':
            d[b[0]]=d[b[0]]+int(b[2])

    return d


def total_withdrawals(a):
    d={}

    for i in a:
        b=i.strip().split(',')

        if b[0] not in d:
            d[b[0]]=0

        if b[1]=='withdraw':
            d[b[0]]=d[b[0]]+int(b[2])

    return d


def find_invalid_transactions(a):
    d={}
    invalid={}

    for i in a:
        b=i.strip().split(',')
        name=b[0]
        money=int(b[2])

        if name not in d:
            d[name]=0
            invalid[name]=0

        if b[1]=='deposit':
            d[name]=d[name]+money

        elif b[1]=='withdraw':
            if money>d[name]:
                invalid[name]=invalid[name]+1
            else:
                d[name]=d[name]-money

    return invalid


def generate_report(a):
    b=calculate_balance(a)
    c=total_deposits(a)
    d=total_withdrawals(a)
    e=find_invalid_transactions(a)

    for i in b:
        print('Name:',i)
        print('Total deposits:',c[i])
        print('Total withdrawals:',d[i])
        print('Balance:',b[i])
        print('Invalid:',e[i])


f=open('transactions.txt','r')
a=f.readlines()
f.close()

generate_report(a)
