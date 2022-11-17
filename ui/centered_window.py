from tkinter import *


class CenteredWindow(Tk):

    def center_window(self):
        self.update()
        wn_width = self.winfo_width()
        wn_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width / 2) - (wn_width / 2))
        y = int((screen_height / 2) - (wn_height / 2))

        self.geometry(f"{wn_width}x{wn_height}+{x}+{y}")
