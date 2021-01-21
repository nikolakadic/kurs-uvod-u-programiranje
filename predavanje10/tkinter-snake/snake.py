import tkinter as tk # alias 
from PIL import Image, ImageTk

root = tk.Tk()
root.title('Snake game')
root.resizable(False,False)

MOVE_INCREMENT = 20

class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(width=620, height=600, bg='black', highlightthickness=0)
        self.load_assets()
        self.snake_body_positions = [(80,100),(60,100),(40,100)]
        self.food_position = (200,400)
        self.score=0
        self.create_objects()
        self.perform_actions()

    def load_assets(self):
        try:
            self.snake_body_image = Image.open('/home/nikola/Desktop/kurs-uvod-u-programiranje/predavanje10/tkinter-snake/assets/snake.png')
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.snake_food_image = Image.open('/home/nikola/Desktop/kurs-uvod-u-programiranje/predavanje10/tkinter-snake/assets/food.png')
            self.snake_food = ImageTk.PhotoImage(self.snake_food_image)
        except IOError as io_error:
            print(io_error)
            root.destroy() # metoda klase Tk koju cu da pokrenem da unistim sve prozore
    
    def create_objects(self):
        # Shows snake body
        self.create_text(45,12,text='Score %s' % self.score, tag='score', fill="#fff")
        for x_position, y_position in self.snake_body_positions:
            self.create_image(x_position, y_position, image=self.snake_body, tag="snake")
        # Shows food
        self.create_image(*self.food_position, image=self.snake_food, tag="food")
        self.create_rectangle(7,27,613,590, outline="#525d69")

    def move_snake(self):
        head_x_position, head_y_position = self.snake_body_positions[0]
        new_head_position = (head_x_position , head_y_position+ MOVE_INCREMENT)
        self.snake_body_positions = [new_head_position] + self.snake_body_positions[:-1]

        
        segments = self.find_withtag("snake")
        positions = self.snake_body_positions
        i=0
        while i < len(segments):
            self.coords(segments[i], positions[i])
            i+=1
    
    def perform_actions(self):
        if self.check_collisions():
            return
        self.move_snake()
        self.after(75, self.perform_actions)

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_body_positions[0]

        return (
            head_x_position in (0, 600) or
            head_y_position in (20, 620)
            or (head_x_position, head_y_position) in self.snake_body_positions[1:]
        )


board = Snake()
board.pack()

root.mainloop()