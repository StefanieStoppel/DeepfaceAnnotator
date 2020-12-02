import pandas as pd

from typing import List
from deepfaceannotator.annotation.annotated_data_point import AnnotatedDataPoint


class CsvAnnotator:
    @staticmethod
    def to_csv(annotated_data_point: List[AnnotatedDataPoint], target_path: str):
        df = pd.DataFrame(annotated_data_point)
        columns = AnnotatedDataPoint.__annotations__.keys()
        df[columns].to_csv(target_path, index=False)
