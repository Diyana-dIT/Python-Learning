a=input('Enter taxt:')
words=a.split()
longest=words[0]
for i in words:
    if len(i)>len(longest):
        longest=i
print(longest)
print('Length:', len(longest))
