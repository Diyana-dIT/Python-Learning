def analyze_text(text):
    words=text.split()
    
    a=0
    for x in text:
        if x.isalpha():
            a+=1
    b=0
    for x in text:
        if x.isdigit():
            b+=1
            
    c=0
    for x in text.lower():
        if x.isalpha:
            if x in c:
                c[x]+=1
            else:
                    c[x]=1
                    
    d=max(c,key=c.get)
    
    e={}
    for x in words:
        x=x.lower()
        if x in e:
            e[x]+=1
        else:
            e[x]=1

    f=max(e,key=e.get)

    g=max(words,key=len)
    
    h=min(words,key=len)

    i=0
    for x in words:
        x=x.lower()
        if x==x[::-1]:
            i+= 1

    j=0
    for x in text:
        if x.isupper():
            j+=1

    k=0
    for x in text:
        if x.islower():
            k+=1

    return {
        "words": len(words),
        "letters": a,
        "digits": b,
        "most_common_letter": d,
        "most_common_word": f,
        "longest_word": g,
        "shortest_word": h,
        "palindrome_words": i,
        "uppercase": j,
        "lowercase": k
    }


text=input("Enter text: ")
result=analyze_text(text)
print(result)
