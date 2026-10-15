class Stand:

    def __init__(self, codice, superficie, padiglione, prezzo):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__espositoreAssociato = None

    @property
    def codice(self):
        return self.__codice

    @property
    def superficie(self):
        return self.__superficie

    @property
    def padiglione(self):
        return self.__padiglione

    @property
    def prezzo(self):
        return self.__prezzo

    @property
    def espositoreAssociato(self):
        return self.__espositoreAssociato
    @espositoreAssociato.setter
    def espositoreAssociato(self, value):
        self.__espositoreAssociato = value

    def __str__(self):
        return f'{self.__codice}: Standard | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo: {self.__prezzo:.2f}'

    def __lt__(self, other):
        return self.__prezzo < other.__prezzo

class Prese(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, numeroPrese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__numeroPrese = numeroPrese

    def __str__(self):
        return f'{self.codice}: Prese Aggiuntive | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo: {self.prezzo:.2f} - Prese aggiuntive: {self.__numeroPrese}'

class Premium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, tipoPremium):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.__tipoPremium = tipoPremium

    def __str__(self):
        return f'{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo: {self.prezzo:.2f} - Posizione: {self.__tipoPremium}'