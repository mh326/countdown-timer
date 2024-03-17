import flet as ft
from timer import CountdownTimer


def main(page: ft.Page):
    def handle_fab_pressed(e):
        print("clicked")

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.EDIT,
        bgcolor=ft.colors.LIME_300,
        on_click=handle_fab_pressed,
    )

    def handle_window_event(event):
        if event.data == "focus":
            page.floating_action_button.visible = True
            page.update()
        elif event.data == "blur":
            page.floating_action_button.visible = False
            page.update()

    page.on_window_event = handle_window_event

    countdown_timer = CountdownTimer(
        60 * 10, interval=0.1, text_kwargs={"size": 80, "color": ft.colors.BLACK}
    )

    page.add(countdown_timer)


ft.app(main)
