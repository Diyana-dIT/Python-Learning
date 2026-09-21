transactions = [
    ("Ali", "deposit", 5000000),
    ("Ali", "withdraw", 1000000),
    ("Sara", "deposit", 8000000),
    ("Ali", "withdraw", 500000),
    ("Sara", "withdraw", 2000000),
    ("Reza", "deposit", 10000000)
]

def analyze_transactions(transactions):
    a = {}
    for x in transactions:
        b=x[0]
        c=x[1]
        d=x[2]

        if b not in a:
            a[b]={
                "deposits":0,
                "withdrawals":0,
                "balance_change":0,
                "transactions":0
            }

        a[b]["transactions"]+=1
        if c=="deposit":
            a[b]["deposits"]+=d
            a[b]["balance_change"]+=d

        elif c=="withdraw":
            a[b]["withdrawals"]+=d
            a[b]["balance_change"]-=d
    return a
result = analyze_transactions(transactions)
print(result)