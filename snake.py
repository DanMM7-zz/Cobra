import tkinter as tk
from PIL import Image, ImageTk

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=600, height=620, background="brown", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = (200, 100)

        self.load_assets()
        self.create_objects()

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("./assets/snake.jpg")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("./assets/food.jpg")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            print(error)
            root.destroy()

    def create_objects(self):
        for x_position, y_position in self.snake_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")

        self.create_image(self.food_position[0], self.food_position[1], image=self.food, tag="food")


root = tk.Tk()
root.title("Cobra")
root.resizable(False, False)

board = Snake()
board.pack()

root.mainloop()


