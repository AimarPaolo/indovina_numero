import random

import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._page.add(self._titolo)
        self._numeroMax = ft.TextField(label="Numero Max",
                                       value=f"{random.randint(1, 150)}",
                                       read_only=True,
                                       width=150)
        self._btnStartGame = ft.ElevatedButton(text="Nuova Partita",
                                               width=150,
                                               on_click=self._controller.handleNewGame)
        row1 = ft.Row([self._numeroMax, self._btnStartGame],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1)

        tentativi = random.randint(4, 10)
        self._TentativiRimanenti = ft.TextField(label="Tentativi Rimanenti", value=f"{tentativi}", width=150)
        self._TentativiMax = ft.TextField(label="Tentativi Max",
                                       value=f"{tentativi}",
                                       read_only=True,
                                       width=150)
        row2 = ft.Row([self._TentativiRimanenti, self._TentativiMax], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row2)
        self._numeroCasuale = random.randint(1, int(self._numeroMax.value))
        self._indovina = ft.TextField(hint_text="Valore", width=150)
        self._btnIndovina = ft.ElevatedButton(text="Indovina", on_click=self._controller.handleIndovina, width=150)
        self._lvOut = ft.ListView()
        self._lvOut.controls.append(ft.Text("indovina a quale numero sto pensando: "))
        row3 = ft.Row([self._indovina, self._btnIndovina], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row3)
        self._page.add(self._lvOut)

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()

