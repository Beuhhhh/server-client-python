import socket
import threading

# servers IP address and port
HOST = "127.0.0.1"
PORT = 65432

# list to keep track of active clients
active_clients = []


def handle_client(conn, addr):
    print(f"Client {addr} connected.")
    active_clients.append((addr, conn))

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                print(f"Connection closed by {addr}.")
                break
            command = data.decode("utf-8").strip()
            print(f"Received command from {addr}: {command}")

            if command.lower() == "exit":
                print(f"Closing connection with {addr}")
                break
    except ConnectionResetError:
        print(f"Connection lost with {addr}")
    finally:
        active_clients.remove((addr, conn))
        conn.close()
        print(f"Client {addr} disconnected.")


# display and select clients manually
def display_and_select_client():
    while True:
        print("\nActive Clients (Enter '0' to refresh):")
        if active_clients:
            for i, (addr, _) in enumerate(active_clients, 1):
                print(f"{i}. {addr}")
        else:
            print("No active clients connected.")

        try:
            choice = int(input("\nSelect client by number or '0' to refresh: "))
            if choice == 0:
                continue  # refresh

            elif 1 <= choice <= len(active_clients):
                selected_addr, selected_conn = active_clients[choice - 1]
                print(f"Selected client: {selected_addr}")

                # send commands
                command = input(
                    "Enter command to send to the client (or 'exit' to stop): "
                )
                selected_conn.sendall(command.encode("utf-8"))
                if command.lower() == "exit":
                    selected_conn.close()
                    active_clients.remove((selected_addr, selected_conn))
                    print(f"Connection with client {selected_addr} closed.")
            else:
                print("Invalid choice. Please select a valid client number.")
        except ValueError:
            print("Please enter a valid number.")


# listen for incoming connections
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Server is waiting for connections...")

        while True:
            conn, addr = s.accept()
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
