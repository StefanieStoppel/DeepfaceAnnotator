from deepface import DeepFace


def analyze_face_image(face_image):
    obj = DeepFace.analyze(face_image, actions=['age', 'gender', 'race', 'emotion'])
    print(obj["age"], " years old ", obj["dominant_race"], " ", obj["dominant_emotion"], " ", obj["gender"])


def analyze_all_face_images(face_images: list):
    objs = DeepFace.analyze(face_images)
    for i in range(len(objs)):
        obj = objs[f'instance_{i+1}']
        print(face_images[i], ":", obj["age"], " years old, ", obj["dominant_race"], ", ", obj["dominant_emotion"], ", ", obj["gender"])


if __name__ == '__main__':
    analyze_all_face_images(['./test_images/norah_jones.jpeg', './test_images/boris.jpeg'])
