from espositore import Espositore
from stand import Stand, Prese, Premium


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.elencoStand = []
        self.elencoEspositori = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        with open(file_path) as infile:
            for line in infile:
                line = line.strip()
                parti = line.split(',')

                if len(parti) == 3:         #se la lunghezza è 3 allora Espositore
                    espositore = Espositore(parti[0], (parti[1]), (parti[2]))
                    self.elencoEspositori.append(espositore)

                elif len(parti) == 4:       #se la lunghezza è 4 allora è stand standard
                    stand = Stand(parti[0], int(parti[1]), int(parti[2]), float(parti[3]))
                    self.elencoStand.append(stand)

                elif len(parti) == 5:       #se la lunghezza è 5 devo controllare se Premium o Prese

                    if parti[4].isdigit():  #Prese
                        prezzoBase = float(parti[3])
                        numeroPrese = int(parti[4])
                        prezzoFinale = prezzoBase * (1 + 0.07 * numeroPrese)
                        stand = Prese(parti[0], int(parti[1]), int(parti[2]), prezzoFinale, numeroPrese)
                        self.elencoStand.append(stand)

                    else:                   #Premium
                        prezzoBase = float(parti[3])
                        prezzoFinale = prezzoBase * 1.30
                        stand = Premium(parti[0], int(parti[1]), int(parti[2]), prezzoFinale, parti[4])
                        self.elencoStand.append(stand)

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        standTrovato = None
        espositoreTrovato = None

        for stand in self.elencoStand:              #controllo esistenza Stand
            if stand.codice == codice_stand:
                standTrovato = stand
                break
        if standTrovato is None:
            raise ValueError('Lo stand non esiste')

        for espositore in self.elencoEspositori:    #controllo esistenza espositore
            if espositore.codice == codice_espositore:
                espositoreTrovato = espositore
                break
        if espositoreTrovato is None:
            raise ValueError("L'espositore non esiste")

        if standTrovato.espositoreAssociato is not None:
            raise ValueError('Lo stand è già stato assegnato')

        if espositoreTrovato.standAssociato is not None:
            raise ValueError("L'espositore ha già uno stand")

        standTrovato.espositoreAssociato = espositoreTrovato
        espositoreTrovato.standAssociato = standTrovato

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.elencoEspositori:
            print(espositore)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.elencoStand)