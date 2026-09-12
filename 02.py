inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}
print('Available:')
for i in inventory:
    if inventory[i]>0:
        print(i)
print('------   ')

print("Out of stock:")
for i in inventory:
    if inventory[i]==0:
        print(i)
print('------   ')

available=0
out_of_stock=0

for i in inventory:
    if inventory[i]>0:
        available+= 1
    else:
        out_of_stock+=1
        
print("Available count:", available)
print("Out of stock count:", out_of_stock)  
