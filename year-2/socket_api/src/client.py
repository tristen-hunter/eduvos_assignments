import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9999))


# --- 1. Build the expected requests & send ---
def sendRequest(cli, comm, context):
    request = f"{comm}, {context}"
    print("SENDING REQUEST: ", request)

    cli.send(request.encode())


# --- 2. Receive response, decode, return to user ---
# raw_resp = client.recv(1024)
# resp = raw_resp.decode()
# print("Server replied: ", resp)
def recvResp(cli):
    raw_resp = cli.recv(1024)
    resp = raw_resp.decode()
    print("Server replied: ", resp)


print("Welcome to The Tech Store\n")

while True:
    print("\n1. View Stock\n2. Add a Product\n3. Delete a Product\n0. To Quit")
    inp = input("Choice: ")

    if inp == "1":
        command = "GET_STOCK"
        product_id = input("Enter Product ID (0 to return all): ")

        sendRequest(client, command, product_id)
        recvResp(client)

    elif inp == "2":
        command = "ADD_PRODUCT"
        # Build the product (
        #   id, next number in the sequence (i + 1)
        #   name, TEXT
        #   price, REAL
        #   rating, REAL
        #   description, TEXT
        #   )
        print("Under Construction ...")
        continue

    elif inp == "3":
        command = "DELETE_PRODUCT"
        product_id = input("Enter Product ID")

    elif inp == "0":
        print("Thanks, come again!")
        break

    else:
        print("Invalid option (1-3, 0 to quit")
        continue


# --- 3. Clean up ---
client.close()
