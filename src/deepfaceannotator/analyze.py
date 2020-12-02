import logging

from deepface import DeepFace

from deepfaceannotator.annotation.csv_annotator import AnnotatedDataPoint, CsvAnnotator
from deepfaceannotator.mappers.age_mapper import AgeMapper
from deepfaceannotator.mappers.gender_2_mappers import Gender2Mapper
from deepfaceannotator.mappers.race_6_mapper import Race6Mapper


_logger = logging.getLogger(__name__)


def analyze_face_image(image_path):
    obj = DeepFace.analyze(image_path, actions=['age', 'gender', 'race', 'emotion'])
    print(obj["age"], " years old ", obj["dominant_race"], " ", obj["dominant_emotion"], " ", obj["dominant_gender"])


def analyze_face_images(image_paths: list, output_csv_path: str):
    analysis_results = DeepFace.analyze(image_paths)
    annotated_data_points = list()
    for i in range(len(analysis_results)):
        single_result = analysis_results[f'instance_{i + 1}']
        age_mapper = AgeMapper(single_result)
        race_6_mapper = Race6Mapper(single_result)
        gender_2_mapper = Gender2Mapper(single_result)
        annotated_data_point = \
            AnnotatedDataPoint(image_paths[i], race_6_mapper.most_likely_race,
                               '', gender_2_mapper.most_likely_gender,
                               age_mapper.most_likely_age_group, list(race_6_mapper.values),
                               [], list(gender_2_mapper.values), [])
        annotated_data_points.append(annotated_data_point)
    _logger.info("Saving annotations...")
    CsvAnnotator.to_csv(annotated_data_points, output_csv_path)


if __name__ == '__main__':
    analyze_face_images(['./test_images/norah_jones.jpeg', './test_images/boris.jpeg'])

# todo: update age mapping from deepface to return 9 values (1 per fairface age group)
#todo: what to do if package is installed, bc then the changes are not present?