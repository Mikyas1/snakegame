import settings


class Snake:

    def __init__(self, location):
        self.body_size = settings.BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.location = location

        for i in range(0, self.body_size):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            self._create_snake_square(x, y, at_start=False)

    def move_head(self, x, y):
        self.coordinates.insert(0, [x, y])
        self._create_snake_square(x, y, at_start=True)

    def _create_snake_square(self, x, y, at_start):
        square = self.location.create_rectangle(x, y, x + settings.SPACE_SIZE, y + settings.SPACE_SIZE,
                                                fill=settings.SNAKE_COLOR, tag=f"snake-{x}x{y}")
        if at_start:
            self.squares.append(square)
        else:
            self.squares.insert(0, square)

    def delete_last_square(self):
        l_x, l_y = self.coordinates[-1]
        del self.coordinates[-1]
        self.location.delete(f"snake-{l_x}x{l_y}")
        del self.squares[-1]

    def move(self, direction, grow):
        x, y = self.coordinates[0]
        if direction == "up":
            y -= settings.SPACE_SIZE
        if direction == "down":
            y += settings.SPACE_SIZE
        if direction == "left":
            x -= settings.SPACE_SIZE
        if direction == "right":
            x += settings.SPACE_SIZE

        self.move_head(x, y)
        if not grow:
            self.delete_last_square()
        return x, y