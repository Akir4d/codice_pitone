import http.client as hc

host = input("Inserisci host/IP del sistema target: ")
port = input("Inserisci la porta del sistema target (default: 80 http/443 https): ")
path = '/'
https = False

if(host.startswith('https://')):
    https = True
    if (port == ""): port = 443
    host = host.replace('https://', '')
else:
    host = host.replace('http://', '')
    if(port == ""): port = 80

pc = host.split("/")

if(len(pc) > 1):
    host = pc[0]
    del pc[0]
    path = "/" + "/".join(pc)
    print(path)

try:
    connection = ""
    if (https):
        connection = hc.HTTPSConnection(host, port)
    else:
        connection = hc.HTTPConnection(host, port)
    
    connection.request('OPTIONS', path)
    response = connection.getresponse()
    print(f"i metodi abilitati sono: {response.getheader('Allow')}")
    connection.close()
except ConnectionRefusedError:
    print("connessione fallita")