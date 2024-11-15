# Keylogger and Server Communication

This project consists of two Python scripts: `client.py` and `server.py`. The client script logs key presses to a local file and communicates with a server to send the log data. The server script listens for incoming client connections, allows the server operator to interact with connected clients, and sends commands to them.

## Files

### `client.py`

The `client.py` script performs the following tasks:

- Logs key presses to a file located at `AppData/Roaming/RiotGames/log.txt`.
- Hides the log file for security purposes.
- Establishes a socket connection to a server.
- Waits for server commands and performs actions based on those commands:
  - `LOG`: Sends the content of the log file to the server.
  - `exit`: Closes the connection to the server.

### `server.py`

The `server.py` script performs the following tasks:

- Listens for incoming client connections
- Maintains a list of active client connections.
- Displays a list of active clients and allows the server operator to:
  - Select a client by number.
  - Send commands to the selected client.
  - Close the connection with the client.

## Requirements

- Python 3.x
- External Libraries:
  - `keyboard` (Install with `pip install keyboard`)

## Usage

### Running the Server

1. Start the server by running `server.py`.
2. The server will listen for incoming connections from clients.
3. Once a client connects, the server operator can interact with the client by selecting it from the list of active clients and sending commands.

### Running the Client

1. Start the client by running `client.py`.
2. The client will attempt to connect to a remote server on port `xxxxx`.
3. The client will log key presses to `AppData/Roaming/RiotGames/log.txt` and send the log file to the server when prompted.

### Available Commands

#### Client Commands:

- **LOG**: Sends the content of the `log.txt` file to the server.
- **exit**: Closes the connection to the server.

## Notes

- Ensure that the server and client are using the correct IP addresses and port numbers.
- The client attempts to reconnect every 10 seconds if it fails to connect to the server.
- The log file is hidden using the `attrib +h` command to avoid easy access.

## Security Disclaimer

This project is intended for educational purposes only. Unauthorized use of keylogging and network monitoring can violate privacy and legal standards. Always obtain proper consent before deploying or using such tools.

## License

This project is open source under the MIT License.
