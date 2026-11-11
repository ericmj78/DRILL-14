from typing import NamedTuple


class BirdFrame(NamedTuple):
    left: int
    bottom: int
    width: int
    height: int


SHEET_HEIGHT = 506
CELL_WIDTH = 182
ROW_EDGES = (0, 170, 340, 506)
ROW_COUNTS = (5, 5, 4)

FRAMES = tuple(
    BirdFrame(
        column * CELL_WIDTH,
        SHEET_HEIGHT - ROW_EDGES[row + 1],
        CELL_WIDTH,
        ROW_EDGES[row + 1] - ROW_EDGES[row],
    )
    for row, count in enumerate(ROW_COUNTS)
    for column in range(count)
)
