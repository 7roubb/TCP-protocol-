import socket
import time 
port =9000
# Your setup code
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1",port))
print(f" client hass been assignd socket name {client.getsockname()}")
data = b"#" * 1024 * 1024 # Large data, e.g., 1 MB
total_sent = 0
data_length = len(data)


try:
    # Manually send data in chunks
    while total_sent < data_length:
     
        sent = client.send(data[total_sent:total_sent+16])
        if sent == 0:
            raise RuntimeError("Socket connection broken")
        total_sent += sent
        total_sent += 16
        time.sleep(0.11)
        print(total_sent)
    print("Data sent successfully.")
except socket.error as e:
    print(f"Error sending data: {e}")
finally:
    client.close()