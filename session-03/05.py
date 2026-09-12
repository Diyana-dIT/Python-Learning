print('.به ماشین حساب جونیور، خوش آمدید')
num1 = float(input('عدد اول را وارد کنید:'))
num2 = float(input('عدد دوم را وارد کنید:'))
amal = input('عملیات را وارد کنید:')

if    amal == '+':
    print(num1 + num2)
elif  amal == '-':
    print(num1 - num2)
elif  amal == '/':
    print(num1 / num2)
elif amal == '//':
    print(num1//num2)
elif  amal == '*':
    print(num1*num2)
elif amal == '**':
    print(num1**num2)
print('''
  ___________
 | Diana 0.0 |
 |___________|
 | 7 | 8 | + |
 | 4 | 5 | - |
 | 1 | 2 | * |
 | . | 0 | / |
 |___________|''')
