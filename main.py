import flet as ft
from timer import CountdownTimer


def main(page: ft.Page):
    countdown_timer = CountdownTimer(60)
    page.add(countdown_timer)


ft.app(main)
