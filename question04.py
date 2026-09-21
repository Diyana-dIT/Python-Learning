transactions=[
("Ali","deposit",50000000,10),
("Ali","withdraw",2000000,11),
("Ali","withdraw",3000000,12),
("Ali","withdraw",4000000,13),
("Ali","withdraw",5000000,14),
("Ali","withdraw",6000000,15),
("Sara","deposit",50000000,20),
("Sara","withdraw",60000000,21),
("Reza","deposit",150000000,30)
]

def check_large_transaction(a):
    if a[2]>100000000:
        return True
    return False

def check_repeated_withdrawals(a,b):
    if a[1]=="withdraw":
        b+=1
    else:
        b=0
    if b>3:
        return True,b
    return False,b

def check_balance(a,b):
    if a[1]=="withdraw" and a[2]>b:
        return True
    return False

def generate_fraud_report(a):
    b=[]
    c=0
    d=0

    for x in a:
        if check_large_transaction(x):
            b.append(x)

        if check_balance(x,c):
            b.append(x)

        if x[1]=="deposit":
            c+=x[2]

        if x[1]=="withdraw":
            c-=x[2]

        d,x=check_repeated_withdrawals(x,d)

        if d:
            b.append(x)

    return b

def detect_fraud(a):
    return generate_fraud_report(a)

print(detect_fraud(transactions))