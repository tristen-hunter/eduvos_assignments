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
