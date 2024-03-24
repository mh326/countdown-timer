import flet as ft


class EditView(ft.View):
    def __init__(self, route, page, countdown_timer):
        super().__init__(route=route)
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

        def handle_text_field_changed(e):
            value = e.control.value
            try:
                int(value)
            except ValueError:
                e.control.value = "0"
                page.update()

        text_minutes.on_change = handle_text_field_changed
        text_seconds.on_change = handle_text_field_changed

        def button_clicked(e):
            minutes = int(text_minutes.value)
            seconds = int(text_seconds.value)
            total_seconds = minutes * 60 + seconds
            countdown_timer.set_seconds(total_seconds, run_update=False)
            page.go("/timer")

        button_play = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=button_clicked
        )

        def handle_switch_window_on_always_top_changed(e):
            page.window_always_on_top = e.control.value
            page.update()

        switch_window_on_always_top = ft.Switch(
            label="keep on top of other windows",
            on_change=handle_switch_window_on_always_top_changed,
            value=page.window_always_on_top,
        )

        def handle_switch_sound_on_time_over(e):
            countdown_timer.sound_on_time_over = e.control.value

        switch_sound_on_time_over = ft.Switch(
            label="sound on time over",
            on_change=handle_switch_sound_on_time_over,
            value=countdown_timer.sound_on_time_over,
        )
        self.controls = [
            ft.Row([text_minutes, text_seconds, button_play]),
            switch_window_on_always_top,
            switch_sound_on_time_over,
        ]
