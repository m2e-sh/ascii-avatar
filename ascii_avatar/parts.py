from ascii_avatar.draw import FeatureZone
from ascii_avatar.enums import CharacterEnum, Emotion


class Mouth(FeatureZone):
    def __init__(self, x, y):
        super().__init__(x, y, 7, 2)
    
    def set_emotion(self, emotion):
        patterns = {
            Emotion.HAPPY: [
                [CharacterEnum.SPACE] * 7,
                [CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.BACKSLASH, CharacterEnum.UNDERSCORE, CharacterEnum.SLASH, CharacterEnum.SPACE, CharacterEnum.SPACE]
            ],
            Emotion.SAD: [
                [CharacterEnum.SPACE] * 7,
                [CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SLASH, CharacterEnum.OVERLINE, CharacterEnum.BACKSLASH, CharacterEnum.SPACE, CharacterEnum.SPACE]
            ],
            Emotion.ANGRY: [
                [CharacterEnum.SPACE] * 7,
                [CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.BACKSLASH, CharacterEnum.UNDERSCORE, CharacterEnum.UNDERSCORE, CharacterEnum.SLASH, CharacterEnum.SPACE]
            ],
            Emotion.LAUGHING: [
                [CharacterEnum.SPACE] * 7,
                [CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.FACE_WITH_TEARS_OF_JOY, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE]
            ],
            Emotion.NEUTRAL: [
                [CharacterEnum.SPACE] * 7,
                [CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.MINUS, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE]
            ],
        }
        self.generate_zone(patterns.get(emotion, patterns[Emotion.NEUTRAL]))

class Eyes(FeatureZone):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 2)
    
    def set_emotion(self, emotion):
        patterns = {
            Emotion.HAPPY: [[CharacterEnum.CARET, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.CARET]],
            Emotion.SAD: [[CharacterEnum.MINUS, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.MINUS]],
            Emotion.ANGRY: [[CharacterEnum.GREATER_THAN, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.LESS_THAN]],
            Emotion.SURPRISED: [[CharacterEnum.CAPITAL_O, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.CAPITAL_O]],
            Emotion.NEUTRAL: [[CharacterEnum.LOWERCASE_O, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.SPACE, CharacterEnum.LOWERCASE_O]],
        }
        self.generate_zone(patterns.get(emotion, patterns[Emotion.NEUTRAL]))

class Face:
    def __init__(self, x, y):
        self.eyes = Eyes(x + 2, y + 2)
        self.mouth = Mouth(x + 4, y + 6)
        self.features = [self.eyes, self.mouth]
    
    def set_emotion(self, emotion):
        for feature in self.features:
            feature.set_emotion(emotion)
    
    def render_to_screen(self, screen):
        for feature in self.features:
            feature.render_to_screen(screen)
