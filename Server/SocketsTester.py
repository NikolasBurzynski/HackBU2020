import ServerSockets

def retrieve(data):
    print(data)
    return "GOT!!"
    
def ret_image(data, image):
    pass
    
net = ServerSockets.SocketHandler(retrieve, ret_image)

net.start_listeners()

while True:
    pass