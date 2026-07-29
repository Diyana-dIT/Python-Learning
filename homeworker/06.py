price = float(input("مبلغ خرید را وارد کنید: "))

if price > 1000000:
    rebate = price * 0.15
elif 500000 <= price <= 1000000:
    rebate = price * 0.10
else:
    rebate = 0
final_price = price - rebate
print("مبلغ نهایی:", final_price)
