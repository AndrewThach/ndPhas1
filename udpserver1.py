from socket import *

serverPort = 12000
CHUNK = 2048

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("Server ready to receive")

with open("File.pdf", "wb") as f:
    while True:
        data, addr = serverSocket.recvfrom(CHUNK)
        if data == b"__END__":
            break
        f.write(data)

serverSocket.close()
print("Server saved received_toffee.pdf")
