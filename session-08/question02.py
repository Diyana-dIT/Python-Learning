data=[
"Ali,LOGIN,200",
"Sara,LOGIN,403",
"Ali,DOWNLOAD,200",
"Reza,LOGIN,500",
"Sara,LOGIN,403",
"Sara,LOGIN,403"
]

def count_successful_logins():
    count=0
    for line in data:
        user,action,status=line.split(",")
        if action=="LOGIN" and status=="200":
            count=count+1
    return count

def count_failed_logins():
    count=0
    for line in data:
        user,action,status=line.split(",")
        if action=="LOGIN" and status!="200":
            count=count+1
    return count

def find_suspicious_users():
    users={}
    for line in data:
        user,action,status=line.split(",")
        if status=="403":
            if user in users:
                users[user]=users[user]+1
            else:
                users[user]=1

    suspicious=[]
    for user in users:
        if users[user]>=3:
            suspicious.append(user)
    return suspicious

def generate_report():
    print("Login موفق:",count_successful_logins())
    print("Login ناموفق:",count_failed_logins())
    print("کاربران مشکوک:",find_suspicious_users())

    print("عملیات هر کاربر:")
    for line in data:
        user,action,status=line.split(",")
        print(user,"->",action)

generate_report()
