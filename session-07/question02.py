def process_order(customer, *products, **options):
    print("Customer:", customer)
    print("Products:", products)
    print("Options:", options)


process_order(
    "Ali",
    "Laptop",
    "Mouse",
    "Keyboard",
    discount=10,
    tax=9,
    shipping=200000
)
