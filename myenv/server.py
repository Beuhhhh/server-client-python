import socket  

# Define the servers IP address
HOST = "127.0.0.1"  
# Define the port number 
PORT = 65432  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET specifies that we’re using IPv4 addresses
    # SOCK_STREAM specifies that we’re using a TCP connection 

    # Bind the server to the specified IP address and port
    s.bind((HOST, PORT))

    # Start listening for incoming connections
    s.listen()
    print("Waiting for a connection...")  # server is ready

    # Accept a connection from a client
    conn, addr = s.accept()
    # conn is the new socket object to communicate with the client
    # addr is the address of the client that connected (IP address and port number)

    with conn:  # Use a with statement to ensure the connection is closed automatically at the end of the block
        print(f"Connected by {addr}")  # Debug

        # Start an infinite loop to keep sending messages to the client
        while True:
            # Prompt the server user to input a command or message
            command = input("Enter command to send to client (or 'exit' to close): ")

            # We encode the string message into bytes (needed for network communication)
            conn.sendall(command.encode("utf-8"))

            # Check if the server wants to end the communication by typing 'exit'
            if command.lower() == 'exit':
                print("Closing connection with client.")  # Debug
                break  
