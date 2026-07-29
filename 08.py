a = int(input('ساعت را وارد کنید: '))
if a < 0 or a > 23:
    print('خطا! ساعت باید بین ۰ تا ۲۳ باشد.')
elif 5 <= a <= 11:
    print('صبح')
elif 12 <= a <= 16:
    print('ظهر')
elif 17 <= a <= 19:
    print('عصر')
else:
    print('شب')