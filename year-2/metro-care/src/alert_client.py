import socket

# Globals (copied from server)
HOST = "127.0.0.1"
PORT = 5055
BUFFER_SIZE = 1024
DELIMITER = "|"

# Sample test data (hard coded)
EQUIPMENT = "EQ-2045"
FACILITY = "Pretoria Central Clinic"
LEVEL = "CRITICAL"
REASON = "Defibrillator failed operational inspection"


def build_alert(code, facility, level, reason):
    # Join the four fields into a string (pipe delimited)
    return DELIMITER.join([code, facility, level, reason])


def main():
    client_socket = None

    try:
        # Step 1: Build the alert and encode it to bytes
        alert = build_alert(EQUIPMENT, FACILITY, LEVEL, REASON)
        data = alert.encode("utf-8")

        # Step 2: Create TCP socket and connect
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.settimeout(10)
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to Central Operations at {HOST}:{PORT}")

        # Step 3: Send the alert
        client_socket.sendall(data)
        print(f"[CLIENT] Alert sent: {alert}")

        # Step 4: Receive and decode the acknowledgement
        reply = client_socket.recv(BUFFER_SIZE).decode("utf-8")
        print(f"[CLIENT] Server response: {reply}")

    except ConnectionRefusedError:
        print("[ERROR] Connection refused. Is the server running?")
    except socket.timeout:
        print("[ERROR] Connection timed out.")
    except OSError as e:
        print(f"[ERROR] Network error: {e}")
    finally:
        # Step 5: Always close the socket
        if client_socket is not None:
            client_socket.close()
        print("[CLIENT] Connection closed.")


if __name__ == "__main__":
    main()
