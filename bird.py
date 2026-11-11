from sprite_sheet import FRAMES


SPRITE_SCALE = 0.42
FLAP_FPS = 18
FLAP_PERIOD = len(FRAMES) / FLAP_FPS


class Bird:
    def __init__(self, offset_x, altitude, phase_seconds):
        self.offset_x = offset_x
        self.altitude = altitude
        self.phase_seconds = phase_seconds

    def frame_at(self, elapsed):
        return FRAMES[int((elapsed + self.phase_seconds) * FLAP_FPS) % len(FRAMES)]

    def draw(self, sheet, center_x, elapsed):
        frame = self.frame_at(elapsed)
        center_y = self.altitude + (frame.eye_y - frame.height / 2) * SPRITE_SCALE
        sheet.clip_composite_draw(
            frame.left, frame.bottom, frame.width, frame.height,
            0, '', center_x + self.offset_x, center_y,
            round(frame.width * SPRITE_SCALE), round(frame.height * SPRITE_SCALE),
        )
