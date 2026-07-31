from person import Person
import helpers


class Employee(Person):
    def insert_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO employees (
                empName,
                empSurname,
                empCell,
                empEmail
            )
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
            (self.email),
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
    name = helpers.getName()
    surname = helpers.getSurname()
    cell = helpers.getCell()
    email = helpers.getEmail()

    return Employee(name, surname, cell, email)
