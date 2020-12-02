from dataclasses import dataclass
from typing import List


@dataclass
class AnnotatedDataPoint:
    image_path: str
    race_6: str  # deepface
    race_4: str  # fairface
    gender_2: str
    age: str
    race_6_scores: List[float]
    race_4_scores: List[float]
    gender_2_scores: List[float]
    age_scores: List[float]
