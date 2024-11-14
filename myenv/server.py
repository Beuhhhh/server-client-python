import socket


HOST = "127.0.0.1"
PORT = 65432

# Define the pre-built commands
commands = [
    """def click(x, y):
        import win32api, win32con
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)""",
    "click(100, 200)",  # Example of calling the function after defining it
    # Add more commands or function calls as needed
]

# Set up the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for a connection...")
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")

        # Send each command from the list
        for command in commands:
            print(f"Sending command: {command}")
            conn.sendall(command.encode("utf-8"))

            # Receive and print the client's response
            response = conn.recv(1024).decode("utf-8")
            print(f"Client response: {response}")
