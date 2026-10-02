def add_user():
    a=input('Enter username:')
    b=input('Enter password:')
    c=input('Enter status:')

    f=open('users.txt','r')
    d=f.readlines()
    f.close()

    for i in d:
        e=i.strip().split(',')
        if e[0]==a:
            print('already exists')
            return

    f=open('users.txt','a')
    f.write(a+','+b+','+c+'\n')
    f.close()
    print('User added')
add_user()