import socket

# Define the server's IP address and port
HOST = "127.0.0.1"  
PORT = 65432   

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET specifies IPv4 and SOCK_STREAM specifies TCP connection
    s.bind((HOST, PORT))  # Bind to the specified address and port
    s.listen()
    print("Waiting for a connection...")  # Server is ready

    # Accept a connection from a client
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")  # Debug

        # Start an infinite loop to keep listening for commands
        while True:
            command = input("Enter command to send to client (or 'exit' to close): ")
            conn.sendall(command.encode("utf-8"))  # Send the command to the client

            # Check if the server wants to close the connection
            if command.lower() == 'exit':
                print("Closing connection with client.")  
                break  

            # Check if the server requested the log file from the client
            elif command.upper() == "LOG":
                try:
                    # Receive the log data from the client
                    log_data = conn.recv(4096).decode("utf-8")
                    
                    # Print the log file content received from the client
                    print("Log file content received from client:")
                    print(log_data)
                except Exception as e:
                    print(f"Error receiving log data from client: {e}")
