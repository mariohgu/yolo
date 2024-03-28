# https://storage.googleapis.com/openimages/web/index.html
# descargar estos archivos csv
"""
oidv6-train-annotations-bbox.csv: https://storage.googleapis.com/openimages/v6/oidv6-train-annotations-bbox.csv
validation-annotations-bbox.csv: https://storage.googleapis.com/openimages/v5/validation-annotations-bbox.csv
test-annotations-bbox.csv: https://storage.googleapis.com/openimages/v5/test-annotations-bbox.csv


"""

import os


alpaca_id = "/m/0gxl3"

ubicacion = os.path.dirname(os.path.abspath(__file__))

train_bboxes_filename = os.path.join(ubicacion, "oidv6-train-annotations-bbox.csv")
validation_bboxes_filename = os.path.join(ubicacion, "validation-annotations-bbox.csv")
test_bboxes_filename = os.path.join(ubicacion, "test-annotations-bbox.csv")
image_list_file_path = os.path.join(ubicacion, "image_list_file")

image_list_file_list = []
for j, filename in enumerate(
    [train_bboxes_filename, validation_bboxes_filename, test_bboxes_filename]
):
    print(filename)
    with open(filename, "r") as f:
        line = f.readline()
        while len(line) != 0:
            id, _, class_name, _, x1, x2, y1, y2, _, _, _, _, _ = line.split(",")[:13]
            if class_name in [alpaca_id] and id not in image_list_file_list:
                image_list_file_list.append(id)
                with open(image_list_file_path, "a") as fw:
                    fw.write("{}/{}\n".format(["train", "validation", "test"][j], id))
            line = f.readline()

        f.close()
