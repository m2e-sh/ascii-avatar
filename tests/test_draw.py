import unittest
from unittest.mock import Mock
from ascii_avatar.enums import CharacterEnum
from ascii_avatar.draw import FeatureZone, ScreenManager

class TestFeatureZone(unittest.TestCase):
    def setUp(self):
        self.feature_zone = FeatureZone(5, 5, 3, 3)
    
    def test_initialization(self):
        self.assertEqual(self.feature_zone.x, 5)
        self.assertEqual(self.feature_zone.y, 5)
        self.assertEqual(self.feature_zone.width, 3)
        self.assertEqual(self.feature_zone.height, 3)
        self.assertEqual(len(self.feature_zone.buffer), 3)
        self.assertEqual(len(self.feature_zone.buffer[0]), 3)
        self.assertEqual(self.feature_zone.buffer[0][0], CharacterEnum.SPACE.value)
    
    def test_generate_zone(self):
        pattern = [
            [CharacterEnum.HASH, CharacterEnum.HASH, CharacterEnum.HASH],
            [CharacterEnum.SPACE, CharacterEnum.HASH, CharacterEnum.SPACE],
            [CharacterEnum.HASH, CharacterEnum.HASH, CharacterEnum.HASH]
        ]
        self.feature_zone.generate_zone(pattern)
        self.assertEqual(self.feature_zone.buffer[0][0], CharacterEnum.HASH.value)
        self.assertEqual(self.feature_zone.buffer[1][1], CharacterEnum.HASH.value)
        self.assertEqual(self.feature_zone.buffer[1][0], CharacterEnum.SPACE.value)
    
    def test_set_emotion_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.feature_zone.set_emotion("happy")

class TestScreenManager(unittest.TestCase):
    def setUp(self):
        self.screen_manager = ScreenManager()
        self.mock_screen = Mock()
    
    def test_add_zone(self):
        zone = Mock()
        self.screen_manager.add_zone(zone)
        self.assertIn(zone, self.screen_manager.zones)
    
    def test_render_calls_render_to_screen(self):
        zone = Mock()
        self.screen_manager.add_zone(zone)
        self.screen_manager.render(self.mock_screen)
        self.mock_screen.clear.assert_called_once()
        zone.render_to_screen.assert_called_once_with(self.mock_screen)
        self.mock_screen.refresh.assert_called_once()

if __name__ == "__main__":
    unittest.main()
