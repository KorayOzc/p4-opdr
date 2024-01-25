import time
from threading import Thread
from tkinter import messagebox

class MyTimer:
    def __init__(self, label):
        self.label = label
        self.start_time = None
        self.running = False

    def start(self):
        self.start_time = time.time()
        self.running = True
        thread = Thread(target=self._update_timer)
        thread.start()

    def stop(self):
        self.running = False

    def reset(self):
        self.stop()
        self.start_time = None
        self.label.config(text="00:00:00")

    def _update_timer(self):
        while self.running:
            elapsed_time = int(time.time() - self.start_time)
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.label.config(text=time_string)
            time.sleep(1)

        if not self.running:
            self.label.config(text="00:00:00")
