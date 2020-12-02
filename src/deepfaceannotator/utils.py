import csv


def get_image_paths_from_csv(csv_path: str):
    data = None
    with open(csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file)
        data = [item for sublist in list(reader) for item in sublist]
    return data
