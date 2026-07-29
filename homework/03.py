mobile = input("شماره موبایل را وارد کنید: ")

if len(mobile) == 11:
    print("کد اپراتور:", mobile[1:4])
else:
    print("خطا: شماره باید0 ۱۱ رقم باشد!")
