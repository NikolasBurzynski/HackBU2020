import socket
import threading
import cv2
import numpy as np

class SocketHandler:
    def __init__(self, on_data, on_image):
        self.lt = threading.Thread(target=self.handle_connections, daemon=True)
        
        self.on_data = on_data
        self.on_image = on_image
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.s.bind(("", 16505))
        self.s.listen(5)
     
    
    def start_listeners(self):
        self.lt.start()
        
    
    def handle_connections(self):
        while True:
            (cs, addr) = self.s.accept()
            
            data = cs.recv(5000000)
            
            header = ""
            str_data = ""
            
            for b in data:
                header = header + chr(b)
                if chr(b) == "}":
                    break
                    
            if header[len(header) - 4:len(header) - 1] == "IMG":
                data = data[len(header):len(data)]
                data = np.fromstring(data, np.uint8)
                image = cv2.imdecode(data, cv2.IMREAD_COLOR)
                cs.send(self.on_image(header.decode("utf-8", image)))
            else:
                str_data = data.decode("utf-8")
                cs.send(self.on_data(str_data).encode("utf-8"))
            
            cs.close()
    
