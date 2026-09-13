sales=(("Ali","Laptop",1200),("Sara","Phone",800),("Ali","Phone",800),("Reza","Laptop",1200),("Sara","Laptop",1200),("Ali","Mouse",50))

customer_sales={}
product_count={}
total_sales=0

for customer,product,price in sales:
    customer_sales[customer]=customer_sales.get(customer,0)+price
    product_count[product]=product_count.get(product,0)+1
    total_sales+=price

for customer,amount in customer_sales.items():
    print(customer,"→",amount)

top_customer=max(customer_sales,key=customer_sales.get)
print("Top customer:",top_customer,"→",customer_sales[top_customer])

for product,count in product_count.items():
    print(product,"→",count)

print("Total sales:",total_sales)
