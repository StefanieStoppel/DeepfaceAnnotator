class Gender2Mapper:
    GENDER_LABELS_DEEPFACE = ['Woman', 'Man']

    def __init__(self, analysis_dict: dict):
        self._genders = analysis_dict["gender"]
        self._most_likely_gender = analysis_dict["dominant_gender"]

    @property
    def probability_female(self):
        return self._genders[self.GENDER_LABELS_DEEPFACE[0]]

    @property
    def probability_male(self):
        return self._genders[self.GENDER_LABELS_DEEPFACE[1]]

    @property
    def values(self):
        return self._genders.values()

    @property
    def keys(self):
        return self._genders.keys()

    @property
    def items(self):
        return self._genders.items()

    @property
    def most_likely_gender(self):
        return 'Female' if self._most_likely_gender is self.GENDER_LABELS_DEEPFACE[0] else 'Male'
