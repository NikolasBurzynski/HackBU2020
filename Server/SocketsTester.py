import ServerSockets

def retrieve(data):
    print(data)
    return "GOT!!"
    
net = ServerSockets.SocketHandler(retrieve)

net.start_listeners()

while True:
    pass