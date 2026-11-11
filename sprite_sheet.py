from typing import NamedTuple


class BirdFrame(NamedTuple):
    left: int
    bottom: int
    width: int
    height: int
    eye_y: int


SHEET_HEIGHT = 506
CELL_WIDTH = 182
ROW_EDGES = (0, 170, 340, 506)
# 원본의 위쪽 기준으로 측정한 눈 중심의 y좌표다.
EYE_ROWS = (
    (93, 92, 91, 88, 85),
    (254, 253, 253, 254, 256),
    (429, 431, 432, 433),
)

FRAMES = tuple(
    BirdFrame(
        column * CELL_WIDTH,
        SHEET_HEIGHT - ROW_EDGES[row + 1],
        CELL_WIDTH,
        ROW_EDGES[row + 1] - ROW_EDGES[row],
        eye_y - ROW_EDGES[row],
    )
    for row, eye_row in enumerate(EYE_ROWS)
    for column, eye_y in enumerate(eye_row)
)
