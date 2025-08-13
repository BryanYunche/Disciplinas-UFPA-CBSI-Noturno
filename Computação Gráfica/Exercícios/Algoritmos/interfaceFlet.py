from desenhaRetaCG import *
from desenhaMatriz import *
from rotacionaRetaCG import *
import flet as ft

def main(page: ft.Page):

    algBresenhan = ft.Row(controls=[
        ft.TextField(label="X", width=50, height=50),
        ft.ElevatedButton(text="Say my name!")
    ])

    page.add(
        ft.Column(controls=[
            ft.Text("Funções de CG"),
            algBresenhan,
            ft.Text("Rodar uma reta: ")
            ]
        )
    )






ft.app(target=main)