{
'p': 1,
'r': 2,
'o': 1,
'g': 2,
'a': 1,
'm': 2,
'i': 1,
'n': 1
}
text=input("Enter:")
b={}
for i in text:
    if i.isalpha():
        if i in b:
            b[i]+=1
        else:
            b[i]=1
print(b)
