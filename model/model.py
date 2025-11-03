from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """

        # TODO
        # connessione con database
        conn = get_connection()
        # se connessione fallita
        if conn is None:
            return None

        cursor = conn.cursor()
        query = "SELECT * FROM automobile"
        # eseguo la query sul database
        cursor.execute(query)
        # mi restituisce i risultati presi dal database in una lista di tuple
        risultati = cursor.fetchall()

        automobili = []
        for row in risultati:
            auto = Automobile(
                codice=row[0],
                marca=row[1],
                modello=row[2],
                anno=row[3],
                posti=row[4],
                disponibile=row[5]
            )
            automobili.append(auto)

        cursor.close()
        conn.close()

        return automobili if automobili else None




    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        # connessione con database
        conn = get_connection()
        # se connessione fallita
        if conn is None:
            return None

        # un oggetto cursore che mi permette di recuperare risultati della query
        cursor = conn.cursor()
        query = """ SELECT * 
                    FROM automobile 
                    WHERE modello = %s """
        # eseguo la query sul database
        cursor.execute(query,(modello,))
        # mi restituisce i risultati presi dal database in una lista di tuple
        risultati = cursor.fetchall()

        automobili = []
        for row in risultati:
            auto = Automobile(
                codice=row[0],
                marca=row[1],
                modello=row[2],
                anno=row[3],
                posti=row[4],
                disponibile=row[5]
            )
            automobili.append(auto)

        cursor.close()
        conn.close()
        return automobili if automobili else None