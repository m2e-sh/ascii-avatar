from enum import Enum

class CharacterEnum(Enum):
    # Basic Symbols
    SPACE = chr(32)  #  
    EXCLAMATION = chr(33)  # !
    DOUBLE_QUOTE = chr(34)  # "
    HASH = chr(35)  # #
    DOLLAR = chr(36)  # $
    PERCENT = chr(37)  # %
    AMPERSAND = chr(38)  # &
    SINGLE_QUOTE = chr(39)  # '
    PAREN_LEFT = chr(40)  # (
    PAREN_RIGHT = chr(41)  # )
    ASTERISK = chr(42)  # *
    PLUS = chr(43)  # +
    COMMA = chr(44)  # ,
    MINUS = chr(45)  # -
    DOT = chr(46)  # .
    SLASH = chr(47)  # /
    
    # Numbers 0-9
    DIGIT_0 = chr(48)  # 0
    DIGIT_1 = chr(49)  # 1
    DIGIT_2 = chr(50)  # 2
    DIGIT_3 = chr(51)  # 3
    DIGIT_4 = chr(52)  # 4
    DIGIT_5 = chr(53)  # 5
    DIGIT_6 = chr(54)  # 6
    DIGIT_7 = chr(55)  # 7
    DIGIT_8 = chr(56)  # 8
    DIGIT_9 = chr(57)  # 9
    
    # More Symbols
    COLON = chr(58)  # :
    SEMICOLON = chr(59)  # ;
    LESS_THAN = chr(60)  # <
    EQUAL = chr(61)  # =
    GREATER_THAN = chr(62)  # >
    QUESTION = chr(63)  # ?
    AT = chr(64)  # @
    
    # Brackets
    SQUARE_BRACKET_OPEN = chr(91)  # [
    BACKSLASH = chr(92)  # \
    SQUARE_BRACKET_CLOSE = chr(93)  # ]
    CARET = chr(94)  # ^
    UNDERSCORE = chr(95)  # _
    BACKTICK = chr(96)  # `
    CURLY_BRACKET_OPEN = chr(123)  # {
    CURLY_BRACKET_CLOSE = chr(125)  # }
    TILDE = chr(126)  # ~
    
    # Box Drawing & Blocks
    LIGHT_SHADE = chr(9617)  # ░
    MEDIUM_SHADE = chr(9618)  # ▒
    DARK_SHADE = chr(9619)  # ▓
    BLOCK = chr(9608)  # █
    HALF_BLOCK_UPPER = chr(9600)  # ▀
    HALF_BLOCK_LOWER = chr(9604)  # ▄
    HALF_BLOCK_LEFT = chr(9612)  # ▌
    HALF_BLOCK_RIGHT = chr(9616)  # ▐
    
    # Line Drawing
    HORIZONTAL_LINE = chr(9472)  # ─
    VERTICAL_LINE = chr(9474)  # │
    TOP_LEFT_CORNER = chr(9484)  # ┌
    TOP_RIGHT_CORNER = chr(9488)  # ┐
    BOTTOM_LEFT_CORNER = chr(9492)  # └
    BOTTOM_RIGHT_CORNER = chr(9496)  # ┘
    CROSS = chr(9532)  # ┼
    
    # Miscellaneous Symbols
    SMILEY = chr(9786)  # ☺
    BLACK_SMILEY = chr(9787)  # ☻
    HEART = chr(9829)  # ♥
    DIAMOND = chr(9830)  # ♦
    CLUB = chr(9827)  # ♣
    SPADE = chr(9824)  # ♠
    
    # Arrows
    ARROW_UP = chr(8593)  # ↑
    ARROW_DOWN = chr(8595)  # ↓
    ARROW_LEFT = chr(8592)  # ←
    ARROW_RIGHT = chr(8594)  # →
    
    # Mathematical Symbols
    INFINITY = chr(8734)  # ∞
    SUMMATION = chr(8721)  # ∑
    PI = chr(960)  # π
    
    # Unicode Emojis (UTF-8)
    THUMBS_UP = "\U0001F44D"  # 👍
    FIRE = "\U0001F525"  # 🔥
    STAR = "\U00002B50"  # ⭐
    CHECK_MARK = "\U00002705"  # ✅
    EMOJI_HEART = "\U00002764"  # ❤
    BROKEN_HEART = "\U0001F494"  # 💔
    HEART_WITH_ARROW = "\U0001F498"  # 💘
    HEART_WITH_SPARKLES = "\U0001F496"  # 💖
    HEART_WITH_RIBBON = "\U0001F49D"  # 💝
    BLACK_HEART = "\U0001F5A4"  # 🖤
    BLUE_HEART = "\U0001F499"  # 💙
    GREEN_HEART = "\U0001F49A"  # 💚
    YELLOW_HEART = "\U0001F49B"  # 💛
    PURPLE_HEART = "\U0001F49C"  # 💜
    FACE_WITH_TEARS_OF_JOY = "\U0001F602"  # 😂
    LOUDLY_CRYING_FACE = "\U0001F62D"  # 😭
    ANGRY_FACE = "\U0001F620"  # 😠
    PENSIVE_FACE = "\U0001F614"  # 😔
    SMILING_FACE_WITH_HEARTS = "\U0001F970"  # 🥰
    EXPLODING_HEAD = "\U0001F92F"  # 🤯
    FACE_WITH_SYMBOLS_OVER_MOUTH = "\U0001F92C"  # 🤬
    FACE_SCREAMING_IN_FEAR = "\U0001F631"  # 😱
    PARTY_POPPER = "\U0001F389"  # 🎉
    CLAPPING_HANDS = "\U0001F44F"  # 👏
    FLEXED_BICEPS = "\U0001F4AA"  # 💪
    SPARKLES = "\U00002728"  # ✨
    COLLISION = "\U0001F4A5"  # 💥
    ZZZ = "\U0001F4A4"  # 💤

class Emotion(Enum):
    NEUTRAL = "neutral"
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"
    SURPRISED = "surprised"
    FEARFUL = "fearful"
    DISGUSTED = "disgusted"
    CONTEMPT = "contempt"
    LAUGHING = "laughing"
    LOVE = "love"
