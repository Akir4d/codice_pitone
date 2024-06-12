class Studente:
    numero_stundenti = 0

    def __init__(self, nome, cognome, matricola):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        Studente.numero_stundenti += 1

    def scheda_personale(self):
        return f"Scheda Studente\n Matricola: {self.matricola}\n Nome: {self.nome}\n Cognome: {self.cognome}"
    
    def in_classe(self):
        s = "studente"
        if (self.numero_stundenti > 1): s = "studenti"
        return f"in classe ci sono {self.numero_stundenti} {s}"

marco = Studente("Marco", "Giacomelli", 123482)
giovanna = Studente("Giovanna", "Posa", 7987839)
print(marco.scheda_personale())
print(marco.in_classe())
# print(Studente.scheda_personale(marco))