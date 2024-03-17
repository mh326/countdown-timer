import math
import time
import threading

import flet as ft


class CountdownTimer(ft.UserControl):
    def __init__(self, seconds, interval=0.1):
        super().__init__()
        self._last_time = None
        self._is_running = False
        self._interval = interval

        def on_click_timer(e):
            self.toggle()

        self.countdown = ft.TextSpan("", on_click=on_click_timer)
        self.set_seconds(seconds, run_update=False)

    def will_unmount(self):
        self._is_running = False

    def update_timer(self):
        while self._left_seconds > 0 and self._is_running:
            current_time = time.time()
            elapsed_time = current_time - self._last_time
            left_seconds = max(self._left_seconds - elapsed_time, 0)
            self.set_seconds(left_seconds)
            self._last_time = current_time
            time.sleep(self._interval)

    def set_seconds(self, seconds, run_update=True):
        self._left_seconds = seconds
        self.update_text(run_update)

    def update_text(self, run_update=True):
        if self._left_seconds > 0:
            seconds = math.floor(self._left_seconds)
            mins, secs = divmod(seconds, 60)
            self.countdown.text = "{:02d}:{:02d}".format(mins, secs)
        else:
            self.countdown.text = "Time Over"

        if run_update:
            self.update()

    def start(self):
        if self._is_running:
            return

        self._is_running = True
        self._last_time = time.time()

        self._thread_timer = threading.Thread(
            target=self.update_timer, args=(), daemon=True
        )
        self._thread_timer.start()

    def stop(self):
        if not self._is_running:
            return

        self._is_running = False

    def toggle(self):
        if self._is_running:
            self.stop()
        else:
            self.start()

    def build(self):
        return ft.Text(
            spans=[self.countdown],
        )