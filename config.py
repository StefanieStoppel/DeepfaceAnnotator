from enum import Enum



class Emotion(Enum):
    ANGRY = 0
    DISGUST = 1
    FEAR = 2
    HAPPY = 3
    SAD = 4
    SURPRISE = 5
    NEUTRAL = 6


class Race(Enum):
    ASIAN = 0
    INDIAN = 1
    BLACK = 2
    WHITE = 3
    MIDDLE_EASTERN = 4
    LATINO_HISPANIC = 5


class Race4(Enum):
    WHITE = 0
    BLACK = 1
    ASIAN = 2
    INDIAN = 3


class GENDER(Enum):
    WOMAN = 0
    MAN = 1
