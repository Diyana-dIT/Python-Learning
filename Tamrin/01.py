my_list = [15, 50, 70, 1, 90, 20, 4, 108, 6]
biggest = max(my_list)
print(biggest)






numbers = [15, 50, 70, 1, 90, 20, 4, 108, 6]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num

print(biggest) 
