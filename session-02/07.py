a = input('Enter number: ')

if len(a) != 16:
    print('Error!')
elif a[:4] == "6037":
    print("بانک ملی")
else:
    print("پیش‌ شماره ناشناخته است.")
