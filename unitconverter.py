def km_to_m():
    km = float(input("Enter value in Kilometer: "))
    m = km * 1000
    print(f"{km} km = {m} meters")

def kg_to_g():
    kg = float(input("Enter value in Kilogram: "))
    g = kg * 1000
    print(f"{kg} kg = {g} grams")

def dollar_to_rupees():
    dollar = float(input("Enter value in Dollar: "))
    rate = 84.0   # Example rate, you can change
    rupees = dollar * rate
    print(f"${dollar} = ₹{rupees}")

# Main Program
while True:
    print("\n--- UNIT CONVERTER ---")
    print("1. KM to Meter")
    print("2. KG to Gram")
    print("3. Dollar to Rupees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        km_to_m()
    elif choice == "2":
        kg_to_g()
    elif choice == "3":
        dollar_to_rupees()
    elif choice == "4":
        print("Thanks for using the converter made by wasim")
        break
    else:
        print("Invalid choice! Please try again.")