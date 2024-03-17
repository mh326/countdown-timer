import flet as ft
from timer import CountdownTimer


def main(page: ft.Page):
    countdown_timer = CountdownTimer(
        60 * 10, interval=0.1, text_kwargs={"size": 80, "color": ft.colors.BLACK}
    )

    def handle_fab_pressed(e):
        countdown_timer.stop()
        page.go("/edit")

    floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.EDIT,
        bgcolor=ft.colors.LIME_300,
        on_click=handle_fab_pressed,
    )

    def handle_window_event(event):
        if event.data == "focus":
            floating_action_button.visible = True
            page.update()
        elif event.data == "blur":
            floating_action_button.visible = False
            page.update()

    page.on_window_event = handle_window_event

    def timer_view():
        view = ft.View(
            "/timer",
            [
                countdown_timer,
            ],
        )
        view.floating_action_button = floating_action_button
        return view

    def edit_view():
        mins, secs = countdown_timer.get_minutes_and_seconds()
        text_minutes = ft.TextField(
            label="minutes",
            value=str(mins),
            input_filter=ft.NumbersOnlyInputFilter(),
            width=100,
        )
        text_seconds = ft.TextField(
            label="seconds",
            value=str(secs),
            input_filter=ft.NumbersOnlyInputFilter(),
            width=100,
        )

        def button_clicked(e):
            minutes = int(text_minutes.value)
            seconds = int(text_seconds.value)
            total_seconds = minutes * 60 + seconds
            countdown_timer.set_seconds(total_seconds, run_update=False)
            page.go("/timer")

        button_play = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked
        )
        view = ft.View(
            "/edit",
            [ft.Row([text_minutes, text_seconds, button_play])],
        )
        return view

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)

        page.views.clear()
        if troute.match("/timer"):
            page.views.append(timer_view())
        elif troute.match("/edit"):
            page.views.append(edit_view())
        page.update()

        if troute.match("/timer"):
            countdown_timer.start()

    page.on_route_change = route_change
    page.go("/edit")


ft.app(main)
