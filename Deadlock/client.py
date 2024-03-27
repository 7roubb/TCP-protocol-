# import socket, sys

# host = 'localhost'
# port = 9000
# bytecount = 32*1024*1024*1024

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bytecount = (bytecount + 15) // 16 * 16  # round up to a multiple of 16
# message = b"capitalize this!"  # 16-byte message to repeat over and over
# print(f"Sending {bytecount} bytes of data, in chunks of 16 bytes")
# sock.connect((host, port))

# sent = 0
# while sent < bytecount:
#     sock.send(message)
#     sent += len(message)
#     print(f"\r{sent} bytes sent", end=' ')
#     sys.stdout.flush()

# print()
# sock.shutdown(socket.SHUT_WR)
# print("Receiving all the data the server sends back")

# received = 0
# while True:
#     data = sock.recv(42)
#     if not received:
#         print(f"The first data received says {repr(data)}")
#         break
#     if not data:
#         break
#     received += len(data)
#     print(f"\r {received} bytes received")
# print()
# sock.close()

import socket, sys

host = 'localhost'
port = 9000
bytecount = 32 *1024*1024 # For testing purposes, you can adjust this value as needed

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

message = b"capitalize this!"  # 16-byte message to repeat over and over
print(f"Sending {bytecount} bytes of data, in chunks of 16 bytes")

sent = 0
confirmed = 0
while sent < bytecount:
    sock.sendall(message)
    sent += len(message)
    print(f"\r{sent} bytes sent", end=' ')
    sys.stdout.flush()

    # Wait for server confirmation
    confirmation = sock.recv(16)
    confirmed += len(confirmation)

print("\nFinished sending data to server.")

sock.shutdown(socket.SHUT_WR)
print("Receiving all the data the server sends back...")

# Here, we should implement logic to receive data from the server if necessary

received = 0
while True:
    data = sock.recv(42)
    if not received:
        print(f"The first data received says {repr(data)}")
        break
    if not data:
        break
    received += len(data)
    print(f"\r {received} bytes received")
print()
sock.close()
