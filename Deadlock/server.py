# import socket 
# import sys
# port =9000
# server  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1',port))
# server.listen(5)
# print(f'listening at {server.getsockname()}')

# while True:
#     sc ,sockname = server.accept()
#     print(f'Proccessing at 1024 bytes at timefrom {sockname}')
#     n  =0 
#     while True:
#         data = sc.recv(1024)
#         if not data :
#             break
#         output = data.decode('ascii').upper().encode('ascii')
#         sc.send(output)
#         n+=len(data)
#         print('\r %d bytes processed so far '% (n,),end = '')
#         sys.stdout.flush()
#     print()
#     sc.close()
#     print('socket closed ')
        
import socket, sys

port = 9000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', port))
server.listen(5)
print(f'Listening at {server.getsockname()}')

while True:
    sc, sockname = server.accept()
    print(f'Processing up to 1024 bytes at a time from {sockname}')
    n = 0
    while True:
        data = sc.recv(1024)
        if not data:
            break
        output = data.decode('ascii').upper().encode('ascii')
        
        # Send confirmation to the client
        sc.sendall(b'ACK')

        # Now send the response back to the client
        sc.sendall(output)

        n += len(data)
        print(f'\r{n} bytes processed so far', end='')
        sys.stdout.flush()
    print("\nSocket closed.")
    sc.close()