import sqlite3
from pathlib import Path


def initialize_database():
    CWD = Path(__file__).resolve().parent

    # Connect to the right DB
    DB_PATH = CWD / "pharmacy_database.db"

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    # 1. Employees (empID, empName, empSurname, empCell, empEmail)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            empID INTEGER PRIMARY KEY,
            empName TEXT,
            empSurname TEXT,
            empCell TEXT,
            empEmail TEXT
        )
    """)

    # 2. Customers (custID, custName, custSurname, custCell, custEmail, residentialAddress)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            custID INTEGER PRIMARY KEY,
            custName TEXT,
            custSurname TEXT,
            custCell TEXT,
            custEmail TEXT,
            residentialAddress TEXT
        )
    """)

    # 3. Products (prodID, prodName, prodPrice, prodQuantity)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            prodID INTEGER PRIMARY KEY AUTOINCREMENT,
            prodName TEXT,
            prodPrice REAL,
            prodQuantity INTEGER
        )
    """)

    # 4. Sales (saleID, prodName, saleDate, saleTotal)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            saleID INTEGER PRIMARY KEY AUTOINCREMENT,
            prodName TEXT,
            saleDate TEXT,
            saleTotal REAL
        )
    """)

    # Clean up
    print("Database Schema successfully created / validated!")
    conn.commit()
    conn.close()
