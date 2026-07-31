from person import Person

# TODO:: Add residentail address


class Customer(Person):
    def insert_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers
            VALUES(?, ?, ?, ?)
        """,
            (self.name, self.surname, self.cell_num, self.email),
        )

        conn.commit()

    def delete_person(self, identifier, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM customers
            WHERE email = ?
        """,
            (identifier,),
        )

        conn.commit()

    def display_all(self, conn):

        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM customers
        """)

        return cursor.fetchall()
