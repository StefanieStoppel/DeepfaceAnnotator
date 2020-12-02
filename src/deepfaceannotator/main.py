from deepface import DeepFace

from deepfaceannotator.mappers.age_mapper import AgeMapper


def analyze_face_image(face_image):
    obj = DeepFace.analyze(face_image, actions=['age', 'gender', 'race', 'emotion'])
    print(obj["age"], " years old ", obj["dominant_race"], " ", obj["dominant_emotion"], " ", obj["dominant_gender"])


def analyze_all_face_images(face_images: list):
    objs = DeepFace.analyze(face_images)
    for i in range(len(objs)):
        obj = objs[f'instance_{i + 1}']
        age_mapper = AgeMapper(obj)
        print(face_images[i], ":", obj["age"], " years old, ", age_mapper.age_group_fair_face, " FairFace age group, ",
              obj["dominant_race"], ", ", obj["dominant_emotion"], ", ", obj["dominant_gender"])


if __name__ == '__main__':
    analyze_all_face_images(['./test_images/norah_jones.jpeg', './test_images/boris.jpeg'])

# face_name_align,race,race4,gender,age,race_scores_fair,race_scores_fair_4,gender_scores_fair,age_scores_fair

# age groups Fairface: '0-2', '3-9', '10-19', '20-29', '30-39', '40-49', '50-59','60-69', '70+'
# gender order FairFace: male, female
# race order 4 FairFace: White, black, asian, indian