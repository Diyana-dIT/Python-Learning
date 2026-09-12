color1 = input("رنگ اول را وارد کنید: ")
color2 = input("رنگ دوم را وارد کنید: ")
color3 = input("رنگ سوم را وارد کنید: ")

if color1 == color2 == color3:
    print("سه رنگ یکسان هستند")

elif color1 == color2 or color1 == color3 or color2 == color3:
    print("دو رنگ یکسان هستند")

else:
    print("رنگ‌ها یکسان نیستند")
