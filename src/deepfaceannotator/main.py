from deepface import DeepFace

from deepfaceannotator.annotation.csv_annotator import AnnotatedDataPoint, CsvAnnotator
from deepfaceannotator.mappers.age_mapper import AgeMapper
from deepfaceannotator.mappers.gender_2_mappers import Gender2Mapper
from deepfaceannotator.mappers.race_6_mapper import Race6Mapper


def analyze_face_image(face_image):
    obj = DeepFace.analyze(face_image, actions=['age', 'gender', 'race', 'emotion'])
    print(obj["age"], " years old ", obj["dominant_race"], " ", obj["dominant_emotion"], " ", obj["dominant_gender"])


def analyze_all_face_images(face_images: list):
    objs = DeepFace.analyze(face_images)
    annotated_data_points = list()
    for i in range(len(objs)):
        obj = objs[f'instance_{i + 1}']
        age_mapper = AgeMapper(obj)
        race_6_mapper = Race6Mapper(obj)
        gender_2_mapper = Gender2Mapper(obj)
        annotated_data_point = \
            AnnotatedDataPoint(face_images[i], race_6_mapper.most_likely_race,
                               '', gender_2_mapper.most_likely_gender,
                               age_mapper.most_likely_age_group, list(race_6_mapper.values),
                               [], list(gender_2_mapper.values), [])
        annotated_data_points.append(annotated_data_point)
        print(face_images[i], ":", obj["age"], " years old, ", age_mapper.most_likely_age_group,
              " FairFace age group, ",
              obj["dominant_race"], ", ", obj["dominant_emotion"], ", ", obj["dominant_gender"])
    CsvAnnotator.to_csv(annotated_data_points, './test_outputs/annotations.csv')


if __name__ == '__main__':
    analyze_all_face_images(['./test_images/norah_jones.jpeg', './test_images/boris.jpeg'])

# face_name_align,race,race4,gender,age,race_scores_fair,race_scores_fair_4,gender_scores_fair,age_scores_fair

# age groups Fairface: '0-2', '3-9', '10-19', '20-29', '30-39', '40-49', '50-59','60-69', '70+'
# gender order FairFace: male, female
# race order 4 FairFace: White, black, asian, indian

# todo: update age mapping from deepface to return 9 values (1 per fairface age group)