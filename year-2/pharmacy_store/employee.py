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
            WHERE empEmail = ?
        """,
            (self.email,),
        )

        conn.commit()

    @classmethod
    def display_all(cls, conn):
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * 
            FROM employees
        """)

        return cursor.fetchall()

    # Bild the Employee object from the tuple returned by the DB (tuple = row)
    @classmethod
    def from_row(cls, row):
        return cls(row[1], row[2], row[3], row[4])


# Function to Create a new Employee (basic error handling)
def create_employee():
    name = helpers.getName()
    surname = helpers.getSurname()
    cell = helpers.getCell()
    email = helpers.getEmail()

    return Employee(name, surname, cell, email)
