import socket
import threading
import time

# Define the server's IP address and port
HOST = "0.0.0.0"
PORT = 65432

# Dictionary to keep track of active clients, storing both the connection and last heartbeat time
active_clients = {}

# Heartbeat timeout in seconds (clients are considered disconnected if they haven't sent a heartbeat in this time)
HEARTBEAT_TIMEOUT = 10

# Function to handle each client connection
def handle_client(conn, addr):
    print(f"Client {addr} connected.")
    active_clients[addr] = (conn, time.time())  # Store the connection and current timestamp

    try:
        while True:
            data = conn.recv(4096)  # Receive data from the client
            if not data:
                print(f"Connection closed by {addr}.")
                break

            command = data.decode("utf-8").strip()

            # Update last heartbeat timestamp if a heartbeat message is received
            if command == 'heartbeat':
                active_clients[addr] = (conn, time.time())
                continue  # Skip printing to avoid spamming console with heartbeats

            # Handle other commands (e.g., LOG, exit)
            if command.upper() == "LOG":
                try:
                    log_data = conn.recv(4096).decode("utf-8")
                    print(f"Log data from {addr}:\n{log_data}")
                except Exception as e:
                    print(f"Error receiving log data from {addr}: {e}")

            elif command.lower() == 'exit':
                print(f"Closing connection with client {addr}.")
                break

    finally:
        # Remove client from active clients list when disconnected
        active_clients.pop(addr, None)
        conn.close()
        print(f"Client {addr} disconnected.")

# Function to display the active clients and let the user select one
def display_and_select_client():
    while True:
        # Refresh list only upon user request
        print("\nPress 0 to refresh the active client list.")
        print("Active Clients:")
        
        # Display only clients who have recently sent a heartbeat
        current_time = time.time()
        active_clients_list = [
            (addr, conn) for addr, (conn, last_heartbeat) in active_clients.items()
            if current_time - last_heartbeat < HEARTBEAT_TIMEOUT
        ]

        if active_clients_list:
            for i, (addr, _) in enumerate(active_clients_list, 1):
                print(f"{i}. {addr}")
        else:
            print("No active clients connected.")

        # Ask user to select a client
        try:
            choice = int(input("\nEnter the number of the client to interact with, or '0' to refresh: "))
            if choice == 0:
                continue  # Refresh the list

            elif 1 <= choice <= len(active_clients_list):
                selected_addr, selected_conn = active_clients_list[choice - 1]
                print(f"Selected client: {selected_addr}")

                # Send commands to selected client
                command = input("Enter the command to send to the client (or 'exit' to stop): ")
                selected_conn.sendall(command.encode("utf-8"))

                if command.lower() == 'exit':
                    selected_conn.close()
                    active_clients.pop(selected_addr, None)
                    print(f"Connection with client {selected_addr} closed.")
            else:
                print("Invalid choice. Please select a valid client number.")
        except ValueError:
            print("Please enter a valid number.")

# Main server function to listen for incoming connections
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is waiting for connections...")

        while True:
            conn, addr = s.accept()
            # Handle each client connection in a new thread
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.daemon = True
            client_thread.start()

# Start the server and client display threads
if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    # Start the client display function in the main thread
    display_and_select_client()
