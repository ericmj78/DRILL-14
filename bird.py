from sprite_sheet import FRAMES


FLAP_FPS = 18
FLAP_PERIOD = len(FRAMES) / FLAP_FPS


class Bird:
    def __init__(self, offset_x, altitude, phase_seconds):
        self.offset_x = offset_x
        self.altitude = altitude
        self.phase_seconds = phase_seconds

    def frame_at(self, elapsed):
        return FRAMES[int((elapsed + self.phase_seconds) * FLAP_FPS) % len(FRAMES)]
