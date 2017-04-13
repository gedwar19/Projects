#implements a chat server
import socket
server = socket.socket()
server.bind(("localhost", 8093))
server.listen(5)
[connection, address] = server.accept()
print("Connected to client")
keep_going = True
while keep_going:
    buf= connection.recv(64)
    if len(buf) > 0:
        connection.send(str.encode("Messagge received by server"))
        msg= buf.decode()
        print(msg)
        if msg == "q":
            print("Connection closing.")
            connection.close()
            keep_going = False
server.close()
