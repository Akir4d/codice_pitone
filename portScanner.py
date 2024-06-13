import socket as so

target = input("Inserisci l'IP da scansionare: ")
portrange = input("inserisci il range di porte da scansire (es 5-200): ")

lowport = int(portrange.split("-")[0])
highport = int(portrange.split("-")[1])

print(f"Verra' scansito da {lowport} a {highport}")

closedPort = []
filteredPort = []
for port in range(lowport, highport+1):
    s = so.socket(so.AF_INET, so.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print(f"*** Porta {port} - Aperta ***")
    else:
        if(status == 111):
            closedPort.append(port)
        else:
            filteredPort.append(port)
    s.close()
print(filteredPort)
yesno = input("\nVuoi che ti mostri le porte chiuse? (S/N): ")
if(yesno.startswith("S")): print(f"\ntrovate chiuse {closedPort}")