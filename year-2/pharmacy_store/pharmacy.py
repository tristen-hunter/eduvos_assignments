from datetime import date
import helpers


class Product:
    def __init__(self, name, price, quantity, prod_id=None) -> None:
        self.prod_id = prod_id
        self.name = name
        self.price = price
        self.quantity = quantity

        @classmethod
        def from_row(cls, row):
            return cls(row[0], row[1], row[2], row[3])


class Sale:
    def __init__(self, prod_name, sale_date, sale_total, sale_id=None):
        self.sale_id = sale_id
        self.prod_name = prod_name
        self.sale_date = sale_date
        self.sale_total = sale_total


class PharmacyStore:
    def add_product(self, conn, product):
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO products (
                prodName,
                prodPrice,
                prodQuantity
            ) 
            VALUES (?, ?, ?)
        """,
            (product.name, product.price, product.quantity),
        )

        conn.commit()

    def remove_product(self, conn, product_id):
        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM products
            WHERE prodID = ?
        """,
            (product_id),
        )

        conn.commit()

    def update_product(self, conn, product):
        cursor = conn.cursor()

        cursor.execute(
            """
          UPDATE products
          SET
            prodName = ?,
            prodPrice = ?,
            prodQuantity = ?
        WHERE prodID = ?
        """,
            (product.name, product.price, product.quantity, product.prod_id),
        )

    def display_products(self, conn):
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM products
        """)

        return cursor.fetchall()

    def sell_product(self, conn, product_id, quantity):
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM products
            WHERE prodID = ?
        """,
            (product_id,),
        )

        productTuple = cursor.fetchone()

        if productTuple is None:
            print("Product not found.")
            return

        product_quantity = productTuple[3]

        new_quantity = int(product_quantity) - int(quantity)

        cursor.execute(
            """
            UPDATE products
            SET 
                prodQuantity = ?
            WHERE prodID = ?
        """,
            (new_quantity, product_id),
        )

        existingProduct = Product(
            prod_id=productTuple[0],
            name=productTuple[1],
            price=productTuple[2],
            quantity=productTuple[3],
        )

        newSale = create_sale(existingProduct, quantity)

        cursor.execute(
            """
            INSERT INTO sales (
                prodName,
                saleDate,
                saleTotal
            )
            VAlUES (?, ?, ?)
        """,
            (newSale.prod_name, newSale.sale_date, newSale.sale_total),
        )

        conn.commit()

    def display_sales(self, conn):
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM sales
        """)

        return cursor.fetchall()


def create_product():
    return Product(
        name=helpers.getProductName(),
        price=helpers.getProductPrice(),
        quantity=helpers.getProductQuantity(),
    )


def create_updated_product():
    return Product(
        prod_id=helpers.getProductID(),
        name=helpers.getProductName(),
        price=helpers.getProductPrice(),
        quantity=helpers.getProductQuantity(),
    )


def create_sale(product, quan):
    prodName = product.name
    saleDate = date.today()
    saleTotal = int(product.price) * int(quan)

    return Sale(prodName, saleDate, saleTotal)
