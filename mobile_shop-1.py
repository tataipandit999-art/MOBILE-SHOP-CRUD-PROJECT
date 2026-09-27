# MOBILE SHOP CRUD PROJECT

# Global list to store all mobile records
mobiles = []


# ------------------------------------------------------------
# Function: add_mobile()
# Purpose: Add a new mobile record
# ------------------------------------------------------------
def add_mobile():
    print("\n========== ADD MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID: "))

    # Check whether the ID already exists
    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("Mobile ID already exists.")
            return

    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    mobile = [mobile_id, brand, model, price, quantity]
    mobiles.append(mobile)

    print("Mobile added successfully.")


# ------------------------------------------------------------
# Function: display_mobiles()
# Purpose: Display all mobile records
# ------------------------------------------------------------
def display_mobiles():
    print("\n========== MOBILE LIST ==========")

    if len(mobiles) == 0:
        print("No mobile records available.")
        return

    print("-" * 75)
    print(
        f"{'ID':<8}"
        f"{'Brand':<15}"
        f"{'Model':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )
    print("-" * 75)

    for mobile in mobiles:
        print(
            f"{mobile[0]:<8}"
            f"{mobile[1]:<15}"
            f"{mobile[2]:<20}"
            f"{mobile[3]:<15.2f}"
            f"{mobile[4]:<10}"
        )

    print("-" * 75)


# ------------------------------------------------------------
# Function: search_mobile()
# Purpose: Search for a mobile using Mobile ID
# ------------------------------------------------------------
def search_mobile():
    print("\n========== SEARCH MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to search: "))

    found = False

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found!")
            print("Mobile ID :", mobile[0])
            print("Brand     :", mobile[1])
            print("Model     :", mobile[2])
            print("Price     :", mobile[3])
            print("Quantity  :", mobile[4])

            found = True
            break

    if found == False:
        print("Mobile not found.")


# ------------------------------------------------------------
# Function: update_mobile()
# Purpose: Update details of an existing mobile
# ------------------------------------------------------------
def update_mobile():
    print("\n========== UPDATE MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to update: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found.")
            print("Current Brand    :", mobile[1])
            print("Current Model    :", mobile[2])
            print("Current Price    :", mobile[3])
            print("Current Quantity :", mobile[4])

            print("\nEnter New Details")

            new_brand = input("Enter New Brand: ")
            new_model = input("Enter New Model: ")
            new_price = float(input("Enter New Price: "))
            new_quantity = int(input("Enter New Quantity: "))

            mobile[1] = new_brand
            mobile[2] = new_model
            mobile[3] = new_price
            mobile[4] = new_quantity

            print("Mobile updated successfully.")
            return

    print("Mobile not found.")


# ------------------------------------------------------------
# Function: delete_mobile()
# Purpose: Delete a mobile record
# ------------------------------------------------------------
def delete_mobile():
    print("\n========== DELETE MOBILE ==========")
    mobile_id = int(input("Enter Mobile ID to delete: "))

    for mobile in mobiles:
        if mobile[0] == mobile_id:
            print("\nMobile Found.")
            print("Brand :", mobile[1])
            print("Model :", mobile[2])

            choice = input(
                "Do you want to delete this mobile? (Y/N): "
            )

            if choice.upper() == "Y":
                mobiles.remove(mobile)
                print("Mobile deleted successfully.")
            else:
                print("Delete operation cancelled.")

            return

    print("Mobile not found.")


# ------------------------------------------------------------
# Function: dashboard()
# Purpose: Display the main menu and control the application
# ------------------------------------------------------------
def dashboard():
    while True:
        print("\n")
        print("=" * 45)
        print(" MOBILE SHOP MANAGEMENT")
        print("=" * 45)
        print("1. Add Mobile")
        print("2. Display All Mobiles")
        print("3. Search Mobile")
        print("4. Update Mobile")
        print("5. Delete Mobile")
        print("6. Exit")
        print("=" * 45)

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
                print("\nThank you for using Mobile Shop Management.")
                break

            case _:
                print("Invalid choice. Please try again.")


# ------------------------------------------------------------
# Function: main()
# Purpose: Starting point of the application
# ------------------------------------------------------------
def main():
    dashboard()


# ------------------------------------------------------------
# Program execution starts here
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
