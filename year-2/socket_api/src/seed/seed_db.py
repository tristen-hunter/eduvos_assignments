import sqlite3
from pathlib import Path

SRC_FILE = Path(__file__).resolve().parent.parent
DB_PATH = SRC_FILE / "store.db"


"""
Creates 10 store products
"""

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS store (
        id INTEGEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        rating REAL,
        description TEXT
    )
""")

cur.execute("""
    INSERT INTO store VALUES(
        1, 
        'MOUSE', 
        650.99, 
        9.2, 
        'Best mouse ever produced, wow'
    )
""")

cur.execute("""
    INSERT INTO store VALUES(
        2, 
        'KEYBOARD', 
        1249.99, 
        9.4, 
        'Best keyboard ever produced, wow'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        3, 
        'MONITOR', 
        3499.99, 
        9.6, 
        '27-inch IPS gaming monitor with vibrant colors'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        4, 
        'HEADSET', 
        899.99, 
        8.9, 
        'Comfortable headset with crystal clear audio'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        5, 
        'WEBCAM', 
        799.99, 
        8.7, 
        '1080p webcam perfect for meetings and streaming'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        6, 
        'USB HUB', 
        299.99, 
        8.5, 
        'Four-port USB 3.0 hub for extra connectivity'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        7, 
        'EXTERNAL SSD', 
        1799.99, 
        9.5, 
        'Fast portable SSD with 1TB of storage'
    )
""")

cur.execute("""
    INSERT INTO store VALUES(
        8, 
        'LAPTOP STAND', 
        449.99, 
        8.8, 
        'Ergonomic aluminum stand for laptops up to 17 inches'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        9, 
        'SPEAKERS', 
        1399.99, 
        9.1, 
        'Powerful stereo speakers with deep bass'
        )
""")

cur.execute("""
    INSERT INTO store VALUES(
        10, 
        'MICROPHONE', 
        1599.99, 
        9.3, 
        'Professional USB microphone for recording and streaming'
        )
""")

con.commit()
con.close()
print("Seed data inserted")
