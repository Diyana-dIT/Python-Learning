Answer = input("Salam\nMikhahid kharid konid? ")
Answer = Answer.lower()
Answer = Answer.strip()

if Answer == "yes":
    print("Befarmaid")
    print("Yaddasht mikonam")
elif Answer == "no":
    print("Mamnoon")
else:
    print("Lotfan faghat ba yes or no javab bedid")
