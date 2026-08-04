javab = input("Salam Mikhahid kharid konid? ")
javab = javab.lower()
javab = javab.strip()

if javab == "yes":
    products = input("Befarmaid, yaddasht mikonam: ").split(",")
    print("Mahsoolati ke goftid:", products)

elif javab == "no":
    print("Mamnoon")

else:
    print("Lotfan faghat ba yes or no javab bedid")