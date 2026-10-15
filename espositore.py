class Espositore:


    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome
        self.__standAssociato = None

    @property
    def codice(self):
        return self.__codice

    @property
    def standAssociato(self):
        return self.__standAssociato
    @standAssociato.setter
    def standAssociato(self, value):
        self.__standAssociato = value

    def __str__(self) :
        if self.__standAssociato is not None:
            return f" {self.__codice}: {self.__nome} {self.__cognome} - Stand: {self.__standAssociato.codice}"
        else:
            return f" {self.__codice}: {self.__nome} {self.__cognome} - Nessun uno stand assegnato"