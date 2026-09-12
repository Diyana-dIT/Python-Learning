products = {
    "laptop": 1200,
    "phone": 800,
    "tablet": 500,
    "headphone": 150,
    "mouse": 50
}
print('expensive:',max(products.values()))
print('cheap:',min(products.values()))
print('average:',sum(products.values())/len(products))
print('sum:',sum(products.values()))
print('More than 500:',end=' ')
for i in products:
    if products[i] > 500:
        print(products[i], end=' ')
