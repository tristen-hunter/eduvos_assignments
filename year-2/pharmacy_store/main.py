import sqlite3
from database import initialize_database
import employee


def main():
    # Create DB if not created yet (skips if it has)
    initialize_database()

    # DB Setup
    conn = sqlite3.connect("pharmacy_database.db")

    print("Welcome To The Pharmacy Store!\nWhat do you want to do today?\n\n")

    while True:
        print("1. Employees\n2. Customers\n3. Products\n4. Sales\n0. Quit\n\n")

        choice = input("Choice: ")

        if choice == "1":
            print(
                "\n1. Add Employe\n2. Remove Employee (by email)\n3. Display all\n0. Return"
            )
            action = input("Action: ")

            if action == "1":
                newEmployee = employee.create_employee()
                newEmployee.insert_person(conn)

                print(f"{newEmployee.name} Added Successfully!")
                return

            elif action == "2":
                pass
            elif action == "3":
                pass
            elif action == "0":
                pass
            else:
                print("Invalid input :(")
                continue

        elif choice == "2":
            print(
                "\n1. Add Customer\n2. Remove Customer (by email)\n3. Display all\n0. Return"
            )
            action = input("Action: ")

            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
            elif action == "0":
                pass
            else:
                print("Invalid input :(")
                continue

            pass
        elif choice == "3":
            print(
                "\n1. Add Product\n2. Remove Product\n3. Update Product\n4. Display All Producrs\n5. Sell Product\n0. Return"
            )
            action = input("Action: ")

            if action == "1":
                pass
            elif action == "2":
                pass
            elif action == "3":
                pass
            elif action == "0":
                pass
            else:
                print("Invalid input :(")
                continue

            pass
        elif choice == "4":
            pass
        else:
            print("Invalid Input, try again :(")
            continue  # restart loop when invalid input is provided


if __name__ == "__main__":
    main()
