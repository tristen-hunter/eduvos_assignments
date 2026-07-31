import sqlite3
from database import initialize_database
import employee
import helpers


def main():
    # Create DB if not created yet (skips if it has)
    initialize_database()

    # DB Setup
    conn = sqlite3.connect("pharmacy_database.db")

    print("Welcome To The Pharmacy Store!\nWhat do you want to do today?")

    while True:
        print("\n\n1. Employees\n2. Customers\n3. Products\n4. Sales\n0. Quit\n\n")

        choice = input("Choice: ")

        if choice == "1":
            print(
                "\n1. Add Employee\n2. Delete Employee (by email)\n3. Display all\n0. Return\n"
            )
            action = input("Action: ")

            if action == "1":
                newEmployee = employee.create_employee()
                newEmployee.insert_person(conn)

                print(f"{newEmployee.name} Added Successfully!")
                continue

            elif action == "2":
                email = helpers.getEmail()
                row = helpers.findByEmail(email, conn)

                if row is None:
                    print("Employee Not Found.")
                else:
                    employeeTBD = employee.Employee.from_row(row)
                    employeeTBD.delete_person(conn)
                    print(f"{employeeTBD.name} Successfully Deleted")

                continue

            elif action == "3":
                employees = employee.Employee.display_all(conn)

                print("\nEmployees:")
                for emp in employees:
                    print(emp)
                print("\n")
                continue

            elif action == "0":
                continue
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
