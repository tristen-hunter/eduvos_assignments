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
