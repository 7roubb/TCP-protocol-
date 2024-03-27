import socket
port = 9000
# MAX_BYTE = 65535
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",port))
print(f" client hass been assignd socket name {client.getsockname()}")
Data = b"#"*32
replay = client.recv(6)
print(f"the server said {repr(replay)}")
socket.close(0)