logs=[
("Ali","LOGIN",200),
("Ali","DOWNLOAD",200),
("Sara","LOGIN",403),
("Reza","LOGIN",200),
("Sara","LOGIN",403),
("Sara","LOGIN",403)
]
def report(logs):
    a=0
    b=0
    c={}
    d={}
    for x in logs:
        name=x[0]
        action=x[1]
        code=x[2]
        if action=="LOGIN" and code==200:
            a+=1
        if action=="LOGIN" and code==403:
            b+=1
        if name not in c:
            c[name]=0
        c[name]+=1
        if name not in d:
            d[name]=0
        if code==403:
            d[name]+=1
    e=[]
    for x in d:
        if d[x]>=3:
            e.append(x)
    return {
        "successful_login":a,
        "failed_login":b,
        "suspicious_users":e,
        "operations":c
    }

print(report(logs))