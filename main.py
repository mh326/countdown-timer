import flet as ft

from views.timer import TimerView
from views.edit import EditView

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--min", help="Initial value (minutes)")
parser.add_argument("-s", "--sec", help="Initial value (seconds)")
parser.add_argument(
    "-w",
    "--window-always-on-top",
    action="store_true",
    help='Turn on "window always on top"',
)
parser.add_argument(
    "-a",
    "--auto-start",
    action="store_true",
    help="Start timer automatically",
)

args = parser.parse_args()
arg_min = None
arg_sec = None
try:
    arg_min = int(args.min)
except Exception:
    pass
try:
    arg_sec = int(args.sec)
except Exception:
    pass


def main(page: ft.Page):
    seconds = 60 * 10
    if arg_min or arg_sec:
        seconds = 0
        if arg_min:
            seconds += arg_min * 60
        if arg_sec:
            seconds += arg_sec

    page.window_always_on_top = args.window_always_on_top

    page.window_width = 300
    page.window_height = 180

    timer_view = TimerView(
        "/timer",
        page,
        seconds=seconds,
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
    if args.auto_start:
        page.go("/timer")
    else:
        page.go("/edit")


ft.app(target=main, assets_dir="assets")
