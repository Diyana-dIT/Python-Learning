import random
a=random.randint(1, 3)
person=0
while person !=a: 
    person=int(input('عدد را حدس بزنید:'))

    if person>a: 
        print('عدد را کوچکتر کن!') 
    elif person<a: 
        print('عدد را بزرگتر کن!')
    
    elif person==a:
        print('افرین!درست حدس زدی :)')
    