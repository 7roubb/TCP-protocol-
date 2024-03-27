import socket
port = 9000
# MAX_BYTE = 65535
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",port))
print(f" client hass been assignd socket name {client.getsockname()}")

data = b"#" * 66 # Large data, e.g., 1 MB
total_sent = 0
data_length = len(data)

try:
    # Send data
    data = b"#" * 1024 * 1024  
    client.sendall(data)
    print("Data sent successfully.")
except socket.error as e:
    print(f"Error sending data: {e}")
finally:
    client.close()