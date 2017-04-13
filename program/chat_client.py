from socket_classes import Client
class Chat_Client(Client):
    def perform(self):
        msg = input("Enter message: ")
        msg = msg.strip()
        while msg != "q":
            try:
                self.send(msg)
                data = self.recv(64)
                print(data)
                msg = input("Enter message: ")
            except:
                print("There was an error")
            self.send(msg)
            self.close()

chatcli = Chat_Client("localhost", 8092)
chatcli.perform()
