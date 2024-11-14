import socket

HOST = "127.0.0.1"
PORT = 65432

# Connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        # Receive the command from the server
        data = s.recv(4096)  # Larger buffer for function definitions
        if not data:
            break

        command = data.decode("utf-8")
        print(f"Executing command: {command}")

        try:
            # Execute the command or function definition
            exec(command)
            if "(" in command and ")" in command:
                s.sendall(b"Function call executed successfully")
            else:
                s.sendall(b"Function defined successfully")

        except Exception as e:
            error_message = f"Error: {str(e)}"
