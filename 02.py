bozorg = 0

for i in range(10):
    h = float(input("ارتفاع را وارد کنید: "))

    if h > bozorg:
        bozorg = h
        print(h, "بیشترین پرش تا این لحظه ثبت شد")
    else:
        print("این مقدار قبلاً ثبت شده است")