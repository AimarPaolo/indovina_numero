import random

from view import View
from model import Model
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def handleNewGame(self, e):
        self._view._numeroMax.value = f"{random.randint(1, 150)}"
        tentativi = random.randint(4, 10)
        self._view._indovina.read_only = False
        self._view._TentativiRimanenti.value = f"{tentativi}"
        self._view._TentativiMax.value = f"{tentativi}"
        self._view._btnIndovina.disabled = False
        self._view._numeroCasuale = random.randint(1, int(self._view._numeroMax.value))
        self._view._indovina.value = ""
        self._view._lvOut.controls.clear()
        self._view.update()

    def handleIndovina(self, e):
        try:
            indovina = int(self._view._indovina.value)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text(value="il valore inserito deve essere un numero", color="red"))
            self._view._indovina.value = ""
            self._view.update()
            return

        if indovina == int(f"{self._view._numeroCasuale}"):
            self._view._lvOut.controls.append(ft.Text(f"Grande! il numero segreto era {self._view._numeroCasuale}"))
            self._view._indovina.read_only = True
            self._view._btnIndovina.disabled = True
            self._view.update()
            return

        elif indovina < int(f"{self._view._numeroCasuale}"):
            self._view._lvOut.controls.append(ft.Text(f"il numero segreto è più grande di {self._view._indovina.value}"))
            self._view._indovina.value = ""
            self._view._TentativiRimanenti.value = str(int(self._view._TentativiRimanenti.value) - 1)
            if self._view._TentativiRimanenti.value == "0":
                self._view._lvOut.controls.append(ft.Text(f"Hai finito i tentativi, mi spiace hai perso!", color="blue"))
                self._view._indovina.read_only = True
                self._view._btnIndovina.disabled = True
                self._view.update()
                return

        else:
            self._view._lvOut.controls.append(ft.Text(f"il numero segreto è più piccolo di {self._view._indovina.value}"))
            self._view._indovina.value = ""
            self._view._TentativiRimanenti.value = str(int(self._view._TentativiRimanenti.value) - 1)
            if self._view._TentativiRimanenti.value == "0":
                self._view._lvOut.controls.append(ft.Text(f"Hai finito i tentativi, mi spiace hai perso!", color="blue"))
                self._view._indovina.read_only = True
                self._view._btnIndovina.disabled = True
                self._view.update()
                return
        self._view.update()
