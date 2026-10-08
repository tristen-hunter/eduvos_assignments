import socket

# Globals
HOST = "127.0.0.1"
PORT = 5055
BUFFER_SIZE = 1024
DELIMITER = "|"


# --- Helpers ---
def parse_alert(message):
    # Split the message, raise error if malformed
    fields = message.split(DELIMITER)
    if len(fields) != 4:
        raise ValueError(f"Expected 4 fields, got {len(fields)}")
    return fields


def display_alert(code, facility, level, reason):
    # Print the alert
    print("\nEMERGENCY EQUIPMENT ALERT")
    print(f"Equipment   : {code}")
    print(f"Facility    : {facility}")
    print(f"Alert Level : {level}")
    print(f"Reason      : {reason}")


# --- Server ---
def main():
    server_socket = None
    conn = None

    try:
        # Step 1: Create TCP socket, bind and listen
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.settimeout(60)  # give up after 60secs
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print("=" * 52)
        print(" METROCARE CENTRAL OPERATIONS SERVER")
        print("=" * 52)
        print(f"Server address : {HOST}")
        print(f"Port           : {PORT}")
        print("[SERVER] Waiting for regional alerts...")

        # Step 2: Accept the client
        conn, addr = server_socket.accept()
        conn.settimeout(10)
        print("[CONNECTED] Regional client connected.")

        # Step 3: Receive bytes and decode to string
        data = conn.recv(BUFFER_SIZE)
        message = data.decode("utf-8")

        # Step 4: Parse, display and build the acknowledgement
        try:
            code, facility, level, reason = parse_alert(message)
            display_alert(code, facility, level, reason)
            reply = f"ACK|{code}|Alert received by Central Operations"
        except ValueError as e:
            print(f"[SERVER] Invalid alert: {e}")
            reply = f"ERROR|Invalid alert format: {e}"

        # Step 5: Encode and send the reply
        conn.sendall(reply.encode("utf-8"))
        print("\n[SERVER] Acknowledgement transmitted.")

    except socket.timeout:
        print("[ERROR] Timed out waiting for a client or data.")
    except ConnectionResetError:
        print("[ERROR] Client closed the connection unexpectedly.")
    except OSError as e:
        print(f"[ERROR] Network error (is port {PORT} already in use?): {e}")
    finally:
        # Step 6: release resources
        if conn is not None:
            conn.close()
        if server_socket is not None:
            server_socket.close()
        print("[SERVER] Connection closed.")


if __name__ == "__main__":
    main()
