import socket
port = 9000
MAX_BYTE = 65535
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind(("localhost",9000))
server.listen(1)
print(f"lisetening at {server.getsockname}")
# def recvall(sock, length):
#     """Receive all bytes of data specified by length."""
#     data = b''
#     while len(data) < length:
#         more = sock.recv(length - len(data))
#         if not more:
#             raise IOError("Socket closed before receiving all data")
#         data += more
#     return data


# while True:
#     sc ,sockname = server.accept()
#     print(f'we have accept a connection form {sockname}')
#     print(f'sock name {sc.getsockname()}')
#     print(f'peer name {sc.getpeername()}')
#     messege = sc.recv(16)
#     print(len(messege))
#     print(f'icoomming {len(messege)} bytes messege {repr(messege)}')
#     sc.send(b'ferewell, client  ffffff')
#     sc.close()
#     print('Replay sent , socket closed ')




while True:
    sc, sockname = server.accept()
    print(f'We have accepted a connection from {sockname}')
    try:
        received_data = b'' 
        while True:
            chunk = sc.recv(16) 
            if not chunk:
                break  # no receved Data 
            received_data += chunk
        print(f"Received data: {received_data[:50]}...")  
        print(len(received_data))
    finally:
        sc.close()
        print('Connection closed')
        
#the idea of this code the same idea of recvall() method in ppt file          
