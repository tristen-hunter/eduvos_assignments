import helpers


class Product:
    def __init__(self, name, price, quantity, prod_id=None) -> None:
        self.prod_id = (prod_id,)
        self.name = (name,)
        self.price = (price,)
        self.quantity = quantity


class Sale:
    def __init__(self, prod_name, sale_date, sale_total, sale_id=None):
        self.sale_id = (sale_id,)
        self.prod_name = (prod_name,)
        self.sale_date = (sale_date,)
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

        cursor.execute("""
            DELETE FROM products
            WHERE prodName = ?
        """)

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

    def display_products(self, conn): ...

    def sell_product(self, conn, product_id, quantity): ...

    def display_sales(self, conn): ...


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
