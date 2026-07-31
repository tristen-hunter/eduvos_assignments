import sqlite3
import socket
from pathlib import Path

# --- 1. Connect to DB ---
SRC_FILE = Path(__file__).resolve().parent
DB_PATH = SRC_FILE / "store.db"

store = sqlite3.connect(DB_PATH)
cur = store.cursor()


# --- 2. Create the socket on port 9999 ---
# TCP based Internet socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socker to local host on port 999
server_socket.bind(("127.0.0.1", 9999))
# Listen, 1 request queue
server_socket.listen(1)
print("Server listening on port 9999...")


# --- 3. Accept connections ---
client, addr = server_socket.accept()
print(f"Client connected from {addr}")


# --- 4. Receive the request in raw bytes
raw_request = client.recv(1024)
request = raw_request.decode()
print("Received: ", request)


# --- 5. Parse the Request ---
"""
    received the request as astring "request items in here, split by (,)"
    Take the request and split it into it's parts with split

    parts = [request_item_1, request_item_2]

    By default the COMMAND is the first item
"""
parts = request.split(",")
command = parts[0]


# --- 6. correctly handle the command (mimics a @RestController)
if parts[0] == "GET_STOCK":
    product_id = int(parts[1])
    cur.execute("SELECT * FROM store WHERE id = ?", (product_id,))
    row = cur.fetchone()

    if row:
        res = f"{row[0]}, {row[1]}"
    else:
        res = "NOT_FOUND"
else:
    res = "UNKNOWN_COMMAND"

# --- 7. Send the result of the socket
client.send(res.encode())

# --- 8. Clean up
client.close()
server_socket.close()
store.close()
