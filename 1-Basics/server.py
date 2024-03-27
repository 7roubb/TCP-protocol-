import socket
port = 9000
MAX_BYTE = 65535
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("localhost",9000))#127.0.0.1
server.listen(1)
print(f"lisetening at {server.getsockname}") 


while True:
    sc ,peerclient = server.accept()
    print(f'we have accept a connection form {peerclient}')
    print(f'sock name {sc.getsockname()}')
    print(f'peer name {sc.getpeername()}')
    messege = b"localhost"
    print(f'icoomming 16 bytes messege {repr(messege)}')
    # print("client Socket name was {}".format(sc.getpeername()))
    sc.send(b'ferewell, client  ffffff')
    # data =server.recv(16)
    # print(len(data))
    
    sc.close()
    print('Replay sent , socket closed ')