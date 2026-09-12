mojoodi = int(input("موجودی: "))

for i in range(3):
    bardasht = int(input("مبلغ برداشت: "))
   
    if bardasht <= 0:
        print("خطا")

    elif bardasht <= mojoodi:
        mojoodi = mojoodi - bardasht
        print("برداشت انجام شد")

    else:
        print("موجودی ناکافی")
