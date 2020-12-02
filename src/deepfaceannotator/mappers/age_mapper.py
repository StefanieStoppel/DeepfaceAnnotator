class AgeMapper:
    AGE_LABELS = ['0-2', '3-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+']
    AGE_MAPPING = None

    def __init__(self, analysis_dict: dict):
        self._exact_age = analysis_dict["age"]
        self.AGE_MAPPING = self._create_age_mapping()

    def _create_age_mapping(self):
        age_mapping = {}
        for i, age_label in enumerate(self.AGE_LABELS):
            if i < len(self.AGE_LABELS) - 1:
                min_age, max_age = age_label.split('-')
            else:
                min_age = 70
                max_age = float("inf")
            age_mapping[age_label] = {"min": float(min_age), "max": float(max_age)}
        return age_mapping

    @property
    def exact_age(self):
        return self._exact_age

    @property
    def age_group_fair_face(self):
        age_group = None
        for label, group in self.AGE_MAPPING.items():
            if group["min"] <= self._exact_age <= group["max"]:
                age_group = label
                break
        return age_group
