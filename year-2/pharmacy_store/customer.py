from person import Person
import helpers

# TODO:: Add residentail address


class Customer(Person):
    def __init__(
        self,
        name: str,
        surname: str,
        cell_num: str,
        email: str,
        residential_address: str,
    ):
        super().__init__(name, surname, cell_num, email)
        self.residential_address = residential_address

    def insert_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO customers (
                custName,
                custSurname,
                empCell,
                empEmail,

            )
            VALUES(?, ?, ?, ?, ?)
        """,
            (
                self.name,
                self.surname,
                self.cell_num,
                self.email,
                self.residential_address,
            ),
        )

        conn.commit()

    def delete_person(self, conn):
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM customers
            WHERE custEmail = ?
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


def create_customer():
    name = helpers.getName()
    surname = helpers.getSurname()
    cell = helpers.getCell()
    email = helpers.getEmail()

    return
