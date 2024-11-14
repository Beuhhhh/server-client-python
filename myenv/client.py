import socket 
from pynput import keyboard

# Define the servers IP address 
HOST = "127.0.0.1"  
# Define the port number to connect to (same as the server's listening port)
PORT = 65432  

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET specifies IPv4 and SOCK_STREAM specifies a TCP connection
    
    #connects to the server
    s.connect((HOST, PORT))

    # Start an infinite loop 
    while True:
        # Receive data from the server in chunks of up to 4096 bytes
        data = s.recv(4096)

        # If data is empty means the server closed the connection
        if not data:
            print("Connection closed by server.")  
            break  

        # Decode the received data (bytes) back into a string for display
        command = data.decode("utf-8")
        print(f"Server says: {command}")

        # Check if the server sent the 'exit' command to close the connection
        if command.lower() == 'exit':
            print("Server requested to close the connection.") #debugging
            break  



