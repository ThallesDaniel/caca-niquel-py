import random
import flet as ft

def main(page: ft.Page):
    def jogar_jackpot(e):
        rodadas = []
        for _ in range(3):
            rodadas.append(random.randint(0, 7))

        label1.value = str(rodadas[0])
        label2.value = str(rodadas[1])
        label3.value = str(rodadas[2])

        if all(num >= 7 for num in rodadas):
            mensagem.value = "Parabéns! Você ganhou o jackpot!" 
        elif all(num == rodadas[0] and num < 7 for num in rodadas ):
            mensagem.value = "Não desanime!\nVoce ganhou o prêmio mínimo!"
        else:
            mensagem.value = f"Que pena! Tente novamente. "#Seus números foram: {rodadas}

        page.update()

    page.title = "Caça-níqueis"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Estilos personalizados
    estilo_numeros = ft.TextStyle(
        font_family="Roboto",
        size=36,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLUE_GREY_400
    )
    estilo_botao = ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=5),
        bgcolor=ft.colors.LIGHT_BLUE_400,
        padding=ft.Padding(left=20, right=20, top=10, bottom=10)
    )

    label_titulo = ft.Text("HAKARI BET", size=24, weight=ft.FontWeight.BOLD)
    label1 = ft.Text("?", style=estilo_numeros)
    label2 = ft.Text("?", style=estilo_numeros)
    label3 = ft.Text("?", style=estilo_numeros)
    mensagem = ft.Text("", size=18)
    botao_jogar = ft.ElevatedButton("JOGAR", on_click=jogar_jackpot, style=estilo_botao)

    page.add(
        label_titulo,
        ft.Row(
            [label1, label2, label3],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        mensagem,
        botao_jogar,
    )

ft.app(target=main)
