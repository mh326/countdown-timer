import flet as ft
from timer import CountdownTimer


def main(page: ft.Page):
    countdown_timer = CountdownTimer(
        60 * 10, interval=0.1, text_kwargs={"size": 80, "color": ft.colors.BLACK}
    )
    page.add(countdown_timer)


ft.app(main)
