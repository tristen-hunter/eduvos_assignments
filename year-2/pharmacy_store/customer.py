from person import Person

# TODO:: Add residentail address


class Customer(Person):
    def insert_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers (
                custName,
                custSurname,
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
            DELETE FROM customers
            WHERE email = ?
        """,
            (self.email),
        )

        conn.commit()

    @classmethod
    def display_all(cls, conn):

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM customers
        """)

        return cursor.fetchall()
