# MOBILE-SHOP-CRUD-PROJECT
📱 MOBILE SHOP CRUD PROJECT

This is a simple Python-based Mobile Shop Management System that performs basic CRUD operations on mobile phone records.

The project uses a menu-driven dashboard where users can add, display, search, update, and delete mobile records.

📌 Project Overview

The application stores mobile phone details such as:

- Mobile ID
- Brand
- Model
- Price
- Quantity

The mobile records are stored in a Python list during program execution.

🛠️ Technologies Used

- Python 3.10 or later
- Python Functions
- Lists
- Loops
- Conditional Statements
- User Input
- F-Strings
- Match-Case Statement

📂 Project Structure

Mobile-Shop-CRUD/
│
├── mobile_shop.py
└── README.md

✨ Features

1. Add Mobile

Adds a new mobile record by taking:

- Mobile ID
- Brand
- Model
- Price
- Quantity

The program also checks whether the entered Mobile ID already exists.

2. Display All Mobiles

Displays all available mobile records in a formatted table containing:

- ID
- Brand
- Model
- Price
- Quantity

If there are no records, the program displays a message indicating that no mobile records are available.

3. Search Mobile

Searches for a mobile using its Mobile ID.

If the mobile is found, its complete details are displayed. Otherwise, the program shows Mobile not found.

4. Update Mobile

Updates the details of an existing mobile.

The user can update:

- Brand
- Model
- Price
- Quantity

The Mobile ID is used to find the record that needs to be updated.

5. Delete Mobile

Deletes an existing mobile record using its Mobile ID.

Before deleting, the program asks the user for confirmation using Y/N.

6. Dashboard

The dashboard provides the main menu for controlling the application.

=============================================
        MOBILE SHOP MANAGEMENT
=============================================
1. Add Mobile
2. Display All Mobiles
3. Search Mobile
4. Update Mobile
5. Delete Mobile
6. Exit
=============================================

The menu uses a "match-case" statement to execute the selected operation.

🚀 How to Run

Step 1: Clone the Repository

git clone https://github.com/your-username/Mobile-Shop-CRUD.git

Step 2: Open the Project Folder

cd Mobile-Shop-CRUD

Step 3: Run the Python Program

python mobile_shop.py

📋 CRUD Operations

Operation| Function| Purpose
Create| "add_mobile()"| Add a new mobile
Read| "display_mobiles()"| Display all mobiles
Read| "search_mobile()"| Search a mobile
Update| "update_mobile()"| Update mobile details
Delete| "delete_mobile()"| Delete a mobile

🎯 Learning Objectives

This project helps in understanding:

- Python functions
- Lists
- Loops
- Conditional statements
- User input
- Searching records
- Updating records
- Deleting records
- Menu-driven programs
- CRUD operations

⚠️ Requirements

- Python 3.10 or later
- The program uses the "match-case" statement.
- Mobile records are stored in the Python list while the program is running.

👨‍💻 Author

Arnab Pandit

B.Tech – Computer Science and Engineering

📌 Conclusion

The Mobile Shop CRUD Project is a beginner-friendly Python application that demonstrates how basic CRUD operations can be implemented using functions, lists, loops, conditions, and a menu-driven dashboard.

---

⭐ If you find this project useful, feel free to give it a star!
