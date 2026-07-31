from person import Person


class Employee(Person):
    def insert_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO employees
            VALUES(?, ?, ?, ?)
        """,
            (self.name, self.surname, self.cell_num, self.email),
        )

        conn.commit()

    def delete_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM employees
            WHERE email = ?
        """,
            (self.email,),
        )

        conn.commit()

    def display_all(self, conn):

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM employees
        """)

        return cursor.fetchall()


# Function to Create a new Employee (basic error handling)
def create_employee():
    while True:
        name = input("First name: ").strip()

        if name.isalpha():
            break

        print("Only letters are allowed.")

    while True:
        surname = input("Surname: ").strip()

        if surname.isalpha():
            break

        print("Only letters are allowed.")

    while True:
        cell = input("Cell number: ").strip()

        if len(cell) == 10 and cell.isdigit():
            break

        print("Cell number must contain exactly 10 digits.")

    while True:
        email = input("Email: ").strip()

        if "@" in email and "." in email:
            break

        print("Invalid email address.")

    return Employee(name, surname, cell, email)
