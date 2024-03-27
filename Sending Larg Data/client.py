import socket
port = 9000
# MAX_BYTE = 65535
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",port))
print(f" client hass been assignd socket name {client.getsockname()}")
Data = b"#"*1024*1024
try:
    # Manually send data in chunks
    client.send(Data)
    print("Data sent successfully.")
except socket.error as e:
    print(f"Error sending data: {e}")
socket.close(0)
