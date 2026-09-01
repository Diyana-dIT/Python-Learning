a=input('Enter text:')
words=['hack','fraud','scam','password','atack']
for i in words:
    if i in a:
        print(i,'->',a.count(i)) 
