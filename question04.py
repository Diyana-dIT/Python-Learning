employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },
    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },
    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}
print(max(employee["salary"] for employee in employees.values()))

#میانگین:
a= sum(employee["salary"] for employee in employees.values())
a=a/len(employees)
print("میانگین حقوق:", a)

#حقوق بیشتر از 3000
print(" با حقوق بیشتر از 3000:")
for employee in employees.values():
    if employee["salary"]>3000:
        print(employee["name"])

# کمترین حقوق
a=min(employees.values(), key=lambda employee: employee["salary"])
print("کمترین حقوق مربوط به:", a["name"])

