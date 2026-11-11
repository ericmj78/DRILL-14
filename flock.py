from bird import Bird, FLAP_PERIOD, SPRITE_SCALE
from sprite_sheet import CELL_WIDTH


FLIGHT_SPEED = 112.0  # pixels per second
SCREEN_MARGIN = 12
ROW_OFFSETS = (
    (-226, -122, -18, 86, 190),
    (-190, -86, 18, 122, 226),
)


def reflected_position(distance, left, right):
    """Return the center and heading after travelling distance from the left."""
    span = right - left
    progress = distance % (2 * span)
    if progress < span:
        return left + progress, True
    return right - (progress - span), False


class Flock:
    def __init__(self, width, height):
        self.elapsed = 0.0
        positions = [
            (offset, height * height_ratio)
            for offsets, height_ratio in zip(ROW_OFFSETS, (0.34, 0.66))
            for offset in offsets
        ]
        self.birds = [
            Bird(offset, altitude, index * FLAP_PERIOD / len(positions))
            for index, (offset, altitude) in enumerate(positions)
        ]

        half_sprite = round(CELL_WIDTH * SPRITE_SCALE) / 2
        offsets = [bird.offset_x for bird in self.birds]
        self.left = SCREEN_MARGIN + half_sprite - min(offsets)
        self.right = width - SCREEN_MARGIN - half_sprite - max(offsets)
        if self.right <= self.left:
            raise ValueError('Canvas is too narrow for the bird formation.')
        self.start_distance = (self.right - self.left) * 0.15

    def update(self, delta):
        self.elapsed += delta

    def draw(self, sheet):
        distance = self.start_distance + self.elapsed * FLIGHT_SPEED
        center, facing_right = reflected_position(distance, self.left, self.right)
        for bird in self.birds:
            bird.draw(sheet, center, self.elapsed)
