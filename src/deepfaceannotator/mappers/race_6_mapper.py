class Race6Mapper:
    RACE_6_LABELS = ['asian', 'indian', 'black', 'white', 'middle eastern', 'latino hispanic']
    RACE_4_LABELS = ['White', 'Black', 'Asian', 'Indian']  # FairFace labels
    RACE_7_LABELS = ['White', 'Black', 'Latino_Hispanic', 'East Asian',
                     'Southeast Asian', 'Indian', 'Middle Eastern']  # FairFace labels

    def __init__(self, analysis_dict: dict):
        self._race_6_dict = analysis_dict["race"]
        # This is a HORRIBLE KEY NAME!!! Sorry for everyone reading this,
        # the author of deepface somehow thoughr this name was okay to use... :(
        self._most_likely_race = analysis_dict["dominant_race"]

    @property
    def race_6_values(self):
        return self._race_6_dict.values()

    @property
    def race_6_keys(self):
        return self._race_6_dict.keys()

    @property
    def race_6_items(self):
        return self._race_6_dict.items()

    @property
    def most_likely_race(self):
        return self._most_likely_race
