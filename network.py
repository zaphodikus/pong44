import socket
from ponglogger import MyLoggerBase
from server import server, port


class Network(MyLoggerBase):

    def __init__(self, role='client'):
        super(Network, self).__init__(name=None, file_name=role)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.info(f"TODO: remove localhost LAN hack")
        self.server = server  # todo: local lan hack
        self.port = port  # todo: local lan hack
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        self.info(f"We got '{self.pos}'")

    def get_pos(self):
        return self.pos

    def connect(self):
        self.info(f"connecting to... {self.server}:{self.port}")
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            self.error(f"Error connecting to {self.server}:{self.port}")

    def send(self, data: str):
        self.debug(data)
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            self.error(f"Sock error on send/recv: {e}")
