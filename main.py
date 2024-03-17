import flet as ft

from views.timer import TimerView
from views.edit import EditView


def main(page: ft.Page):
    timer_view = TimerView(
        "/timer",
        page,
        seconds=60 * 10,
        interval=0.1,
        text_kwargs={
            "size": 90,
            "color": ft.colors.BLACK,
            "text_align": ft.TextAlign.CENTER,
        },
        text_timeover_kwargs={
            "size": 50,
            "color": ft.colors.RED,
            "text_align": ft.TextAlign.CENTER,
        },
    )

    edit_view = EditView("/edit", page, timer_view.countdown_timer)

    def route_change(handler):
        troute = ft.TemplateRoute(handler.route)

        page.views.clear()
        if troute.match("/timer"):
            page.views.append(timer_view)
        elif troute.match("/edit"):
            page.views.append(edit_view)
        page.update()

        if troute.match("/timer"):
            timer_view.countdown_timer.start()

    page.on_route_change = route_change
    page.go("/edit")

    page.window_width = 300
    page.window_height = 180


ft.app(main)
