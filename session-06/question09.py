products={
    "P01":("Laptop",1200,5),
    "P02":("Phone",800,0),
    "P03":("Tablet",500,12),
    "P04":("Mouse",50,25),
    "P05":("Keyboard",100,0)
}



total=0
values={}
for code,(name,price,stock) in products.items():
    if stock>0:
        print('موجود:',name)
    else:
        print('ناموجود:',name)
    
    value=price*stock
    values[code]=value
    total+=value

most=max(values,key=values.get)

print('بیشترین ارزش موجودی:',products[most][0])
print('ارزش:',values[most])
print('ارزش کل انبار:',total)
