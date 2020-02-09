import socket
import threading

class SocketHandler:
    def __init__(self, on_data):
        self.lt = threading.Thread(target=self.handle_connections, daemon=True)
        
        self.on_data = on_data
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.s.bind(("", 16505))
        self.s.listen(5)
     
    
    def start_listeners(self):
        self.lt.start()
        
    
    def handle_connections(self):
        while True:
            (cs, addr) = self.s.accept()
            
            data = cs.recv(1024)
            
            str_data = data.decode("utf-8")
            
            cs.send(self.on_data(str_data).encode("utf-8"))
            cs.close()