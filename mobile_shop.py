# MOBILE SHOP CRUD PROJECT
# Author: Arnab Pandit

mobiles = []

def add_mobile():
    print("\n--- Add Mobile ---")
    mobile_id = input("Enter Mobile ID: ")

    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            print("Mobile ID already exists!")
            return

    brand = input("Enter Brand: ")
    model = input("Enter Model: ")

    try:
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
    except ValueError:
        print("Invalid price or quantity!")
        return

    mobiles.append({
        "id": mobile_id,
        "brand": brand,
        "model": model,
        "price": price,
        "quantity": quantity
    })
    print("Mobile added successfully!")

def display_mobiles():
    print("\n--- All Mobiles ---")
    if not mobiles:
        print("No mobile records found.")
        return

    print("-" * 75)
    print(f"{'ID':<12}{'Brand':<15}{'Model':<15}{'Price':<15}{'Quantity':<10}")
    print("-" * 75)

    for mobile in mobiles:
        print(f"{mobile['id']:<12}{mobile['brand']:<15}{mobile['model']:<15}"
              f"{mobile['price']:<15.2f}{mobile['quantity']:<10}")
    print("-" * 75)

def search_mobile():
    print("\n--- Search Mobile ---")
    mobile_id = input("Enter Mobile ID: ")

    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            print("\nMobile Found!")
            print("ID       :", mobile["id"])
            print("Brand    :", mobile["brand"])
            print("Model    :", mobile["model"])
            print("Price    :", mobile["price"])
            print("Quantity :", mobile["quantity"])
            return

    print("Mobile not found!")

def update_mobile():
    print("\n--- Update Mobile ---")
    mobile_id = input("Enter Mobile ID: ")

    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            brand = input(f"Enter Brand [{mobile['brand']}]: ")
            model = input(f"Enter Model [{mobile['model']}]: ")
            price = input(f"Enter Price [{mobile['price']}]: ")
            quantity = input(f"Enter Quantity [{mobile['quantity']}]: ")

            if brand:
                mobile["brand"] = brand
            if model:
                mobile["model"] = model

            if price:
                try:
                    mobile["price"] = float(price)
                except ValueError:
                    print("Invalid price. Existing price kept.")

            if quantity:
                try:
                    mobile["quantity"] = int(quantity)
                except ValueError:
                    print("Invalid quantity. Existing quantity kept.")

            print("Mobile updated successfully!")
            return

    print("Mobile not found!")

def delete_mobile():
    print("\n--- Delete Mobile ---")
    mobile_id = input("Enter Mobile ID: ")

    for mobile in mobiles:
        if mobile["id"] == mobile_id:
            confirm = input(
                f"Delete {mobile['brand']} {mobile['model']}? (y/n): "
            )

            if confirm.lower() == "y":
                mobiles.remove(mobile)
                print("Mobile deleted successfully!")
            else:
                print("Delete cancelled.")
            return

    print("Mobile not found!")

def main():
    while True:
        print("\n=============================================")
        print("       MOBILE SHOP MANAGEMENT")
        print("=============================================")
        print("1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")
        print("=============================================")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                add_mobile()
            case "2":
                display_mobiles()
            case "3":
                search_mobile()
            case "4":
                update_mobile()
            case "5":
                delete_mobile()
            case "6":
                print("Thank you for using Mobile Shop Management!")
                break
            case _:
                print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()
