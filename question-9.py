username='Diyana'
password='1234'

attempts=3

while attempts>0:
    u=input('Enter username: ')
    p=input('Enter password: ')

    if u==username and p==password:
        print('Login successful')
        break
    else:
        attempts-=1
        print('Wrong username or password')