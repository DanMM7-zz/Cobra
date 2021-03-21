import tkinter as tk
from PIL import Image, ImageTk

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="brown", highlightthickness=0)

        self.load_assets()

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.jpg")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.jpg")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()


root = tk.Tk()
root.title("Cobra")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()


