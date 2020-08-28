# Convers polygons regions form JSON file into binary masks or overlay annotation maps on original images.
# Changes needed in the code: check main()

import os
import sys
import json
import numpy as np
import skimage.draw
import cv2


def create_overlay(image, mask):
	redImg = np.zeros(image.shape, image.dtype)
	redImg[:,:] = (0, 0, 255)
	redMask = cv2.bitwise_and(redImg, redImg, mask=mask)
	cv2.addWeighted(redMask, 1, image, 1, 0, image)
	return image


# Create binary masks from polygons read from JSON file
def overlay_annt_maps(dataset_dir, annotation_file, output_dir, binary_flag = True):
    # Load annotations from Json file
    annotations = json.load(open(os.path.join(dataset_dir, annotation_file)))
    annotations = list(annotations.values())  # don't need the dict keys
    annotations = [a for a in annotations if a['regions']]

    # Extract Polygons from the annotations list
    for a in annotations:
        print("a", a)
        if type(a['regions']) is dict:
            polygons = [r['shape_attributes'] for r in a['regions'].values()]
        else:
            polygons = [r['shape_attributes'] for r in a['regions']] 

        # read original image to get its height and width
        # image_path = os.path.join(dataset_dir, a['filename'])
        # image = cv2.imread(image_path)
        # height, width = image.shape[:2]
        
        # # Create a mask of zeroes of height and width
        # mask = np.zeros([height, width, len(polygons)], dtype=np.uint8)

        # # Extract x and y points from polygons and a set the polygon regions as 255, i-e white
        # for i, p in enumerate(polygons):
        #     rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
        #     mask[rr, cc, i] = (1*255)
        
        # # If binary flag is True, create binary images from annotation polygons, otherwise
        # # map overlays of annotation on original images
        # if binary_flag:
        #     cv2.imwrite(os.path.join(output_dir, a['filename']), mask)
        # else:
        #     overlayed_img = create_overlay(image, mask)
        #     cv2.imwrite(os.path.join(output_dir, a['filename']), overlayed_img)
        # print(a['filename'])



def main():
    dir_path = "crystal dataset MaskRCNN"
    annotation_file = "annotations.json"
    output_dir = "output"
    # set flag to map_overlay or binary_mas

    if not os.path.exists(output_dir):
        os.mkdir("output")

    # Execute the function to create binary images or map overlays based on flag
    overlay_annt_maps(dir_path, annotation_file, output_dir, binary_flag = True)

if __name__ == "__main__":
    main()