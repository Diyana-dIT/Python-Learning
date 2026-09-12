import random
while True:
    person = input('سنگ، کاغذ، قیچی: ')
    
    if person == 'exit':
        break
    
    elif person not in ['سنگ', 'کاغذ', 'قیچی']:
        print('ورودی اشتباه است! دوباره وارد کنید.')
        continue

    computer = random.choice(['سنگ', 'کاغذ', 'قیچی'])
    if person == computer:
        print('مساوی!')

    elif (person == 'سنگ' and computer == 'قیچی') or \
         (person == 'کاغذ' and computer == 'سنگ') or \
         (person == 'قیچی' and computer == 'کاغذ'):
        print('کاربر برنده شد!')

    else:
        print('کامپیوتر برنده شد!')
