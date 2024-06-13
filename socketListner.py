import socket as so

SRV_ADDR = "127.0.0.1"
SRV_PORT = 44444

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

print(f"Il server e' avviato su {SRV_ADDR}:{SRV_PORT}")
connection, address = s.accept()
print(f"Client in ascolto all'indirizzo {address}")
connection.sendall(b"Ciao!\n faccio echo:\n")
while True:
    connection.sendall(b"$ ")
    data = connection.recv(1024)
    if not data: break
    connection.sendall(b"# ")
    command = data.decode('utf-8').replace("\n","")
    if(command == "ciao"):
        connection.sendall(b"Non abbiamo gia' stabilito il saluto?\n")
    elif(command == "ls"):
        connection.sendall(b"Ci hai provato?\n")
    else:
        connection.sendall(data)
    print(data.decode('utf-8'))
connection.close()