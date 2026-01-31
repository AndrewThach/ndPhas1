from socket import *

serverName = '127.0.0.1'
serverPort = 12000
CHUNK = 1024

clientSocket = socket(AF_INET, SOCK_DGRAM)

filename = "toffee.pdf"
clientSocket.sendto(filename.encode(), (serverName, serverPort))

with open(filename, "rb") as f:
    while True:
        data = f.read(CHUNK)
        if not data:
            break
        clientSocket.sendto(data, (serverName, serverPort))

clientSocket.sendto(b"__END__", (serverName, serverPort))
clientSocket.close()
