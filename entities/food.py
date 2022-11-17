import random

import settings


class Food:
    def __init__(self, location):
        x = random.randint(0, (settings.GAME_WIDTH // settings.SPACE_SIZE) - 1) * settings.SPACE_SIZE
        y = random.randint(0, (settings.GAME_HEIGHT // settings.SPACE_SIZE) - 1) * settings.SPACE_SIZE

        self.coordinates = [x, y]

        location.create_oval(x,
                             y,
                             x + settings.SPACE_SIZE,
                             y + settings.SPACE_SIZE,
                             fill=settings.FOOD_COLOR,
                             tag="food",
                             )
