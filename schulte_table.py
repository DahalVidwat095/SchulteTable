import tkinter as tk
from tkinter import PhotoImage
import random
from colorsys import hsv_to_rgb

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
GRID_SIZE = 5
SQUARE_SIZE = 300 / GRID_SIZE
GRID_TOTAL_SIZE = SQUARE_SIZE * GRID_SIZE

class SchulteTableGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Schulte Table Game")
        self.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")

        # Load and set the icon
        icon_image = PhotoImage(file="schulte.png")  # Ensure the icon.png file is in the same directory as the script
        self.iconphoto(False, icon_image)

        self.current_number = 1
        self.numbers = list(range(1, GRID_SIZE * GRID_SIZE + 1))
        random.shuffle(self.numbers)
        self.colors = self.generate_unique_colors(GRID_SIZE * GRID_SIZE)
        random.shuffle(self.colors)
        self.create_widgets()

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()
        self.label = self.canvas.create_text(
            CANVAS_WIDTH / 2, 
            25, 
            text="Number to select: 1",
            font=('Monospace', 20), 
            fill='black',
            anchor='center'
        )
        self.create_grid()

    def create_grid(self):
        start_x = (CANVAS_WIDTH - GRID_TOTAL_SIZE) / 2
        start_y = (CANVAS_HEIGHT - GRID_TOTAL_SIZE) / 2

        number_index = 0
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                x1 = start_x + j * SQUARE_SIZE
                y1 = start_y + i * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE

                rect = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=self.colors[number_index],
                    outline="black"
                )

                text = self.canvas.create_text(
                    x1 + SQUARE_SIZE / 2, 
                    y1 + SQUARE_SIZE / 2, 
                    text=str(self.numbers[number_index]),
                    font=('Monospace', 20), 
                    fill='black',
                    anchor='center'
                )
                
                self.canvas.tag_bind(rect, '<Button-1>', lambda event, number=self.numbers[number_index]: self.check_number(number))
                self.canvas.tag_bind(text, '<Button-1>', lambda event, number=self.numbers[number_index]: self.check_number(number))
                
                number_index += 1

    def check_number(self, number):
        if number == self.current_number:
            self.current_number += 1
            self.canvas.itemconfig(self.label, text=f"Number to select: {self.current_number}")
            if self.current_number > GRID_SIZE * GRID_SIZE:
                self.canvas.itemconfig(self.label, text="Congratulations !!!")

    def generate_unique_colors(self, num_colors):
        colors = []
        for i in range(num_colors):
            hue = i / num_colors
            lightness = 1
            saturation = 0.7
            r, g, b = hsv_to_rgb(hue, saturation, lightness)
            colors.append('#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255)))
        return colors

if __name__ == '__main__':
    game = SchulteTableGame()
    game.mainloop()
