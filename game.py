from tkinter import Label, Canvas

import settings
from entities.food import Food
from entities.snake import Snake


class Game:
    def __init__(self, window):
        self.window = window
        self.score = 0
        self.direction = 'down'

        self.label = Label(self.window, text=f"Score: {self.score}", font=('consolas', 40))
        self.label.pack()

        self.canvas = Canvas(window,
                             bg=settings.BACKGROUND_COLOR,
                             height=settings.GAME_HEIGHT,
                             width=settings.GAME_WIDTH)
        self.canvas.pack()

        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)

        self.next_turn()

    def next_turn(self):
        x, y = self.snake.coordinates[0]  # snake head
        x, y = self.snake.move(self.direction, grow=self.eat(x, y))

        if self.check_collision(x, y):
            self.game_over()
        else:
            self.window.after(settings.SPEED, self.next_turn)

    def eat(self, x, y):
        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.configure(text=f"Score: {self.score}")
            self.canvas.delete("food")
            self.food = Food(self.canvas)
            return True
        return False

    def bind_controls(self):
        self.window.bind('<Left>', lambda event: self.chane_direction('left'))
        self.window.bind('<Right>', lambda event: self.chane_direction('right'))
        self.window.bind('<Up>', lambda event: self.chane_direction('up'))
        self.window.bind('<Down>', lambda event: self.chane_direction('down'))

    def chane_direction(self, new_direction):
        if new_direction == "left":
            if self.direction != "right":
                self.direction = new_direction
        elif new_direction == "right":
            if self.direction != "left":
                self.direction = new_direction
        elif new_direction == "up":
            if self.direction != "down":
                self.direction = new_direction
        elif new_direction == "down":
            if self.direction != "up":
                self.direction = new_direction

    def start_game(self):
        self.next_turn()
        self.bind_controls()

    def check_collision(self, x, y):
        if x < 0 or x > settings.GAME_WIDTH:
            return True
        elif y < 0 or y > settings.GAME_HEIGHT:
            return True

        for body_part in self.snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
        return False

    def game_over(self):
        self.canvas.delete('all')
        self.canvas.create_text(self.canvas.winfo_width() / 2, self.canvas.winfo_height() / 2,
                                font=('consolas', 70), text="GAME OVER", fill="red", tag="game_over")
