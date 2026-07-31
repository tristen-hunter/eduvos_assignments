# Helpers for Person related entities


def getName():
    while True:
        name = input("Enter first name: ").strip()
        clean = name.replace(" ", "").replace("-", "").replace("'", "")

        if len(name) >= 2 and clean.isalpha():
            return name.title()

        print("Name must contain only letters and be at least 2 characters long.")


def getSurname():
    while True:
        surname = input("Enter surname: ").strip()

        if len(surname) >= 2 and surname.replace(" ", "").isalpha():
            return surname.title()

        print("Surname must contain only letters and be at least 2 characters long.")


def getCell():
    while True:
        cell = input("Enter cellphone number: ").strip()

        # Remove spaces for convenience
        cell = cell.replace(" ", "")

        if cell.isdigit() and len(cell) == 10:
            return cell

        print("Cell number must contain exactly 10 digits.")


def getEmail():
    while True:
        email = input("Enter email address: ").strip().lower()

        if "@" in email and "." in email and email.index("@") < email.rindex("."):
            return email

        print("Please enter a valid email address.")


def getResidentialAddress():
    while True:
        address = input("Enter residential address: ").strip()

        if len(address) >= 5:
            return address

        print("Address is too short.")


def getProductName():
    while True:
        name = input("Enter product name: ").strip()

        if len(name) >= 2:
            return name

        print("Product name must be at least 2 characters long.")


# TODO: fix these refactor to be more simple
def getProductPrice():
    while True:
        try:
            price = float(input("Enter product price: R"))

            if price > 0:
                return price

            print("Price must be greater than 0.")

        except ValueError:
            print("Please enter a valid price.")


def getProductQuantity():
    while True:
        try:
            quantity = int(input("Enter product quantity: "))

            if quantity >= 0:
                return quantity

            print("Quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid whole number.")


def getProductID():
    while True:
        try:
            product_id = int(input("Enter product ID: "))

            if product_id > 0:
                return product_id

            print("Product ID must be greater than 0.")

        except ValueError:
            print("Please enter a valid product ID.")


def getSaleQuantity():
    while True:
        try:
            quantity = int(input("Enter quantity to sell: "))

            if quantity > 0:
                return quantity

            print("Sale quantity must be greater than 0.")

        except ValueError:
            print("Please enter a valid whole number.")


## Functions for fetching from the DB
def find_employee_by_id(email, conn):
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * 
        FROM employees 
        WHERE empEmail = ?
    """,
        (email,),
    )
    return cur.fetchone()


def find_customer_by_id(email, conn):
    cur = conn.cursor()

    cur.execute(
        """
        SELECT * 
        FROM customers 
        WHERE custEmail = ?
    """,
        (email,),
    )
    return cur.fetchone()
