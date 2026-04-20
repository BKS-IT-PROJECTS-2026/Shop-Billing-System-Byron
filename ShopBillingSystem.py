
print("=== Shop Billing System ===")
print("Enter item prices one by one.")
print("Type 'done' or enter 0 to finish.\n")

total = 0.0

while True:
    user_input = input("Enter item price (or 'done' to finish): ").strip().lower()

    if user_input == "done" or user_input == "0":
        break

    try:
        price = float(user_input)

        if price < 0:
            print("Price cannot be negative. Try again.")
            continue

        total += price

    except ValueError:
        print("Invalid input. Please enter a valid number.")

discount = 0.0

if total > 1000:
    discount = total * 0.20
elif total > 500:
    discount = total * 0.10

final_amount = total - discount

print("\n=== Billing Summary ===")
print(f"Total before discount: R{total:.2f}")
print(f"Discount applied:      R{discount:.2f}")
print(f"Final amount to pay:   R{final_amount:.2f}")
print("=======================")