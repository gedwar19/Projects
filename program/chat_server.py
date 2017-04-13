from socket_classes import Server

class Chat_Server(Server):
    def serve(self):
        keep_going = True
        while keep_going == True:
            msg = self.recv(64).strip()
            if msg != "":
                self.send("Message recieved.")
                print (msg)
                if msg == "q":
                    print("Connection terminated.")
                    self.connection.close()
                    keep_going = False
        self.close()

chatsrv = Chat_Server("localhost", 8092,1)
chatsrv.serv()    
