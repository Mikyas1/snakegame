from tkinter import *

import game
from ui.centered_window import CenteredWindow

if __name__ == '__main__':
    window = CenteredWindow()
    window.title("Sneak game")
    window.resizable(False, False)

    new_game = game.Game(window)
    new_game.start_game()

    window.center_window()
    window.mainloop()
