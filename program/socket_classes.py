import socket

class Server:
    def __init__(self, addr, port,conn_lim):
        self.setup()
        self.establish_connection(addr, port, conn_lim)
    def establish_connection(self, addr, port, conn_lim):
        self.socket = socket.socket()
        self.socket.bind((addr, port))
        self.socket.listen(conn_lim)
        [self.connection, self.address] = self.socket.accept()
    def setup(self):
        #all the specific code to set up the client 
        pass
    def serve (self):
        pass
    def send(self, msg):
        self.connection.send(str.encode(msg))
    def recv(self, size):
        buf = self.connection.recv(size)
        if len(buf) > 0:
            return buf.decode()
        else:
            return ""
    def close(self):
        self.socket.close()

class Client:
    def __init__(self, addr, port):
        self.establish_connection(addr,port)
    def establish_connection(self, addr, port):
        self.socket = socket.socket()
        self.socket.connect((addr,port))
    def send(self, size):
        self.socket.send(str.encode(msg))
    def recv(self, size):
        buf = self.socket.recv(size)
        if len(buf) > 0:
            return buf.decode()
        else:
            return ""

    def perform(self):
        pass
    def close(self):
        self.socket.close()
