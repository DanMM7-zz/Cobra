import tkinter as tk

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="brown", highlightthickness=0)


root = tk.Tk()
root.title("Cobra")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()


