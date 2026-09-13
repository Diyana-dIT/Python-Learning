orders=[("Ali","Laptop"),("Sara","Phone"),("Ali","Phone"),("Reza","Laptop"),("Sara","Laptop"),("Ali","Tablet"),("Reza","Phone")]

result={}
for customer,product in orders:
    result[customer]=result.get(customer,[])
    result[customer].append(product)
print(result)
