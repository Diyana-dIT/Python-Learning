students = {
    'Ali': [18, 17, 20],
    'Sara': [15, 19, 18],
    'Reza': [12, 14, 10],
    'Mina': [20, 20, 19]
}

for name, scores in students.items():
    average=sum(scores)/len(scores)
    
    if average>=10:
        status="قبول"
    else:
        status="مردود"

    highest = max(scores)
    print("نام:",name)
    print("میانگین:",average)
    print("وضعیت:",status)
    print("بالاترین نمره:",highest)
    print("----------------")
