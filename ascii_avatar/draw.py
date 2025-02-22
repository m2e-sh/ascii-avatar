from ascii_avatar.enums import CharacterEnum


class FeatureZone:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.buffer = [[CharacterEnum.SPACE.value for _ in range(width)] for _ in range(height)]
    
    def set_emotion(self, emotion):
        raise NotImplementedError(f"set_emotion(emotion={emotion}) is not implemented in `FeatureZone` class.")
    
    def render_to_screen(self, screen):
        for row_idx, row in enumerate(self.buffer):
            screen.addstr(self.y + row_idx, self.x, "".join(row))
    
    def generate_zone(self, pattern):
        for y, row in enumerate(pattern):
            for x, char in enumerate(row):
                self.buffer[y][x] = char.value

class ScreenManager:
    def __init__(self):
        self.zones = []
    
    def add_zone(self, zone):
        self.zones.append(zone)
    
    def render(self, screen):
        screen.clear()
        for zone in self.zones:
            zone.render_to_screen(screen)
        screen.refresh()
