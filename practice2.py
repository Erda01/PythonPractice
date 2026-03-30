# ============ SECOND PRACTICE ==========
# Task D1, multiple orders

customer_name = input("Enter customer name: ")
items_count = 0

subtotal = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")

    if item.lower() == "done":
        break

    price = int(input("Enter price: "))
    subtotal = subtotal + price
    items_count += 1

print("\nCustomer : ", customer_name.upper())
print("Items : ", items_count)
print("Subtotal : ", subtotal, " KZT")

# Task D2, Time-Based Discount

current_hour = int(input("\nEnter current hour (0-23) : "))
discount = 0
time_period = ""

if 6 <= current_hour < 12:
    discount = 10
    time_period = "Morning discount"
elif 12 <= current_hour < 17:
    discount = 0
    time_period = "No discount"
elif 17 <= current_hour < 22:
    discount = 5
    time_period = "Evening discount"
else:
    print("Closed")
    exit()

discount_amount = subtotal * discount / 100
total = subtotal - discount_amount
tip = total * 0.10
total = total + tip

print("\n-------------------------------")
print("Time period : ", time_period)
print("Discount : ", discount_amount, " KZT")
print("Tip (10%) : ", tip, " KZT")
print("Total : ", total, " KZT")
print("-------------------------------")


#Task D3, Name Analysis

print("\nName uppercase : ", customer_name.upper())
print("Name lowercase : ", customer_name.lower())
print("Name length : ", len(customer_name))
if customer_name[0].upper() == 'A' or customer_name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")