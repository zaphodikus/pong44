import socket
from _thread import start_new_thread
import sys
from ponglogger import MyLoggerBase
from client_base import ClientBase

server = socket.gethostbyname(socket.gethostname())
port = 5555
num_listens = 2

pos = [(0, 0), (100, 100)]  # 2 players

class Server(MyLoggerBase):

    def __init__(self):
        super(Server, self).__init__(name=None, file_name="pongserver")


    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.info(f"Binding to {server}:{port}")
            s.bind((server, port))
        except socket.error as e:
            self.error(e)

        s.listen(num_listens)
        self.info("Listening")

        current_player = 0
        while True:
            conn, addr = s.accept()
            self.info("Connected")
            start_new_thread(Server.threaded_client, (self, conn, current_player))
            current_player += 1
            if current_player > 1:
                current_player = 0

    def threaded_client(self, conn, player):
        self.info(f"threaded_client() called with {conn} ({player})")
        reply = ""
        self.info("Initiate loop")
        #conn.send(str.encode("Connected"))
        conn.send(str.encode(ClientBase.make_pos(pos[player])))
        while True:
            try:
                data = ClientBase.read_pos(conn.recv(2048).decode())
                pos[player] = data
                if not data:
                    self.info("disconnected")
                    break
                else:
                    self.info(f"got {data}")
                    if player == 1:
                        reply = pos[0]
                    else:
                        reply = pos[1]


                self.info(f"sending {reply}")
                conn.sendall(str.encode(ClientBase.make_pos(reply)))
            except socket.error as e:
                self.error(f"Server socket error {e}")
            except Exception as e:
                self.error("oopsie : exception occurred: \n\t{e}")
                break
        self.info("Lost connection")
        conn.close()
