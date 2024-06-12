dizionario = {"nome": "Erika", "cognome": "Bianchi", "nascita": "10/03/1999"}

print (dizionario["nome"])

dizionario["nome"] = "Erica"

print(dizionario)
print(dizionario.keys())
print(list(dizionario.values()))

# destrutturazione dati data lista o tupla o oggetto direttamente convertibile in lista
numeri = (1,2,3,4)
# posso destrutturare gli elementi se voglio
# ignorare un elemento per convezione si usa _
x,y,z,_ = numeri

print("x=",x," y=",y," z=",z, sep="")

lista = [1,2,3,4,5]
# destrurazione con asterisco il valore iniziale
# o finale posso essere usati con * per raccogliere
# i dati rimanenti senza ricorrere a _
a, b, *resto = lista

*inizio, c, d = lista

print(resto)
print(inizio)

# verifico che sia direttamente convertibile in lista
print(list(dizionario.items()))

for key, value in dizionario.items():
    print(key, "=",value)