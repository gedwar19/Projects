#client
import socket
client = socket.socket()
client.connect(("localhost", 8093))
msg = input("Enter a message ").lower().strip()
while msg != "q":
    try:
        client.send(str.encode(msg))
        data = client.recv(64)
        print(data.decode())
        msg = input("Enter a message: ").lower().strip()
    except:
        print("There was a problem")
client.send(str.encode(msg))
client.close()
