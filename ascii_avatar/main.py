

import curses

from ascii_avatar.draw import ScreenManager
from ascii_avatar.enums import Emotion
from ascii_avatar.parts import Face


def main(stdscr):
    curses.curs_set(0)
    screen_manager = ScreenManager()
    face = Face(30, 10)
    screen_manager.add_zone(face.eyes)
    screen_manager.add_zone(face.mouth)
    
    while True:
        screen_manager.render(stdscr)
        key = stdscr.getch()
        if key == ord('q'):
            break
        elif key == ord('h'):
            face.set_emotion(Emotion.HAPPY)
        elif key == ord('s'):
            face.set_emotion(Emotion.SAD)
        elif key == ord('a'):
            face.set_emotion(Emotion.ANGRY)
        elif key == ord('l'):
            face.set_emotion(Emotion.LAUGHING)
    
if __name__ == "__main__":
    curses.wrapper(main)
