import cv2
import numpy as np
import json
import os

def get_contour(img):
    imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imggray, 127, 255, 0)
    _ , contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnt = contours[0]
    # print("area", cv2.contourArea(cnt))   # another way for cnt area
    contours = np.vstack(contours).squeeze()
    return contours

def create_json(input_path):
    data = {}
    for file in os.listdir(input_path):
        if file.endswith('json'):
            continue
        print(file)
        img = cv2.imread(os.path.join(input_path, file))
        contours = get_contour(img)
        all_x = [int(i[0]) for i in contours]
        all_y = [int(i[1]) for i in contours]
        # data[file] = {}
        data[file] = ({
            'filename': file,
            'regions': [{"shape_attributes": {"name": "polygons", "all_points_x": all_x, "all_points_y": all_y},
            'region_attributes': {}}],
            'file_attributes': {}
        })
        with open(os.path.join(input_path, 'bin_annt.json'), 'w') as outfile:
            json.dump(data, outfile)


def main():
    input_path = "binary_images"
    create_json(input_path)

if __name__ == "__main__":
    main()
