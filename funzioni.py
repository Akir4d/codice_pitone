
def stampaqui(nome, cognome):
    print("ti chiami", nome, cognome)

stampaqui("Pinco", "Pallino")

# un modo alternativo per unire piu' stringhe al string + string
# e' anteporre f ai doppi apici ed inserire le stringhe con {string}

def tichiami(nome, cognome):
    return f"ti chiami {nome} {cognome}"

nuova_stringa = tichiami("Pinco", "Pallino")
print(nuova_stringa)

# in python i nomi degli argomenti posso essere richiamati in modo 
# non posizionale ovvero argomento=valore

print(tichiami(cognome="Labarca", nome="Remo"))

# alcuni usano ''' o """ per fare commenti
# di fatto sono dichiarazioni di stringe multiriga

sss="kjlkjkld"
a=f'''djdkj {sss}
jdkjdk
jkdjdkh'''
print(a)