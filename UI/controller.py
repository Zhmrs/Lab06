import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_lista_auto(self,e):
        self._view.lista_auto.controls.clear()
        for auto in self._model.get_automobili():
            self._view.lista_auto.controls.append(ft.Text(f"{auto}")) # Lo aggiungo alla ListView
        self._view.update()


    def cerca_automobile(self,e):
        # modello= testo inserito dall'utente
        modello=self._view.input_modello_auto.value.strip()
        # ogni volta che inserisco un nuovo modello mi si aggiorna la lista eliminando quello precedente
        self._view.lista_auto_ricerca.controls.clear()

        if not modello:
            self._view.alert.show_alert("⚠️ Inserisci un modello")

        # se il modello inserito dall'utente non è presente nel database allora scatena un eccezione
        elif self._model.cerca_automobili_per_modello(modello) is None:
            self._view.alert.show_alert("⚠️ Non esiste il modello nel database")

        else: # altrimenti stampa la lista degli automobili dei quel modello
            for auto in self._model.cerca_automobili_per_modello(modello):
                self._view.lista_auto_ricerca.controls.append(ft.Text(f"{auto}")) # Lo aggiungo alla ListView

        # dopo aver schiacciato il tasto CERCA elimina il campo di inserimento
        self._view.input_modello_auto.value=''
        self._view.update()



