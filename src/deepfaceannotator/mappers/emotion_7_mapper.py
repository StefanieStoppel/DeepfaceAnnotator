class Emotion7Mapper:
    EMOTION_LABELS = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

    def __init__(self, analysis_dict: dict):
        self._emotion_dict = analysis_dict["emotion"]
        self._most_likely_emotion = analysis_dict["dominant_emotion"]

    @property
    def values(self):
        return self._emotion_dict.values()

    @property
    def keys(self):
        return self._emotion_dict.keys()

    @property
    def items(self):
        return self._emotion_dict.items()

    @property
    def most_likely_emotion(self):
        return self._most_likely_emotion
