# HOTEL MANAGEMENT SYSTEM
# Menu and Billing using Python

menu = {
    1: ["Tea", 15],
    2: ["Coffee", 25],
    3: ["Poha", 30],
    4: ["Vada Pav", 20],
    5: ["Misal Pav", 60],
    6: ["Veg Thali", 120],
    7: ["Paneer Masala", 150],
    8: ["Chapati", 10],
    9: ["Cold Drink", 40],
    10: ["Ice Cream", 50]
}

order = []

print("=" * 45)
print("       WELCOME TO PYTHON HOTEL")
print("=" * 45)

customer = input("Enter Customer Name: ")

while True:

    print("\n--------------- HOTEL MENU ---------------")
    print("No.       Item              Price")
    print("------------------------------------------")

    for number, details in menu.items():
        print(f"{number:<10}{details[0]:<18}Rs.{details[1]}")

    print("------------------------------------------")
    print("0. Generate Bill")

    choice = int(input("\nEnter item number: "))

    if choice == 0:
        break

    if choice not in menu:
        print("Invalid item number!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Please enter a valid quantity!")
        continue

    item_name = menu[choice][0]
    price = menu[choice][1]

    amount = price * quantity

    order.append([item_name, price, quantity, amount])

    print(item_name, "added successfully!")

# BILL GENERATION

print("\n")
print("=" * 45)
print("             PYTHON HOTEL")
print("=" * 45)

print("Customer Name:", customer)
print("-" * 45)

print(f"{'Item':<16}{'Qty':<6}{'Price':<8}{'Amount'}")
print("-" * 45)

subtotal = 0

for item in order:

    print(f"{item[0]:<16}{item[2]:<6}"
          f"{item[1]:<8}{item[3]}")

    subtotal += item[3]

gst = subtotal * 0.05
grand_total = subtotal + gst

print("-" * 45)
print(f"Subtotal:        Rs.{subtotal:.2f}")
print(f"GST (5%):        Rs.{gst:.2f}")
print("-" * 45)
print(f"GRAND TOTAL:     Rs.{grand_total:.2f}")

print("=" * 45)
print("       THANK YOU! VISIT AGAIN")
print("=" * 45)