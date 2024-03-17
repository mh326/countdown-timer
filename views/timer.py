import flet as ft
from timer import CountdownTimer


class TimerView(ft.View):
    def __init__(self, route, page, **kwargs):
        super().__init__(route=route)

        def handle_fab_pressed(e):
            self.countdown_timer.stop()
            page.go("/edit")

        floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.EDIT,
            bgcolor=ft.colors.LIME_300,
            on_click=handle_fab_pressed,
        )

        self.countdown_timer = CountdownTimer(**kwargs)

        def handle_window_event(event):
            if event.data == "focus":
                floating_action_button.visible = True
                page.update()
            elif event.data == "blur":
                floating_action_button.visible = False
                page.update()

        page.on_window_event = handle_window_event

        self.floating_action_button = floating_action_button
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.CENTER

        self.controls = [self.countdown_timer]
