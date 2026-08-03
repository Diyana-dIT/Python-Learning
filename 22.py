a=int(input('سن:'))
g=input('جنسیت:')

if g=='m' and a<=40 and a>=0:
    print('پسر ')
elif g=='m' and 40<=a<60:
    print('اقا')
elif g=='m' and a>=60:
    print('بابابزرگ')
elif g=='g' and a<=40 and a>=0:
    print('دختر')
elif g=='g' and 40<=a<60:
     print ('خانم ')
elif g=='g' and a>=60:
     print('مادربزرگ') 