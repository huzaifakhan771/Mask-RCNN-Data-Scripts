# Convers polygons regions form JSON file into binary masks.
# Changes needed in the code: dir_path, output_dir, JSON file name

import os
import sys
import json
import numpy as np
import skimage.draw
import cv2

dir_path = "/home/huzaifakhan771/Documents/dataset"
output_dir = "/home/huzaifakhan771/Documents/res/"

# Create binary masks from polygons read from JSON file
def polytobinmask(dataset_dir):
    # Load annotations from Json file
    annotations = json.load(open(os.path.join(dataset_dir, "annotations.json")))
    annotations = list(annotations.values())  # don't need the dict keys
    annotations = [a for a in annotations if a['regions']]

    # Extract Polygons from the annotations list
    for a in annotations:
        if type(a['regions']) is dict:
            polygons = [r['shape_attributes'] for r in a['regions'].values()]
        else:
            polygons = [r['shape_attributes'] for r in a['regions']] 

        # read original image to get its height and width
        image_path = os.path.join(dataset_dir, a['filename'])
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        
        # Create a mask of zeroes of height and width
        mask = np.zeros([height, width, len(polygons)], dtype=np.uint8)

        # Extract x and y points from polygons and a set the polygon regions as 255, i-e white
        for i, p in enumerate(polygons):
            rr, cc = skimage.draw.polygon(p['all_points_y'], p['all_points_x'])
            mask[rr, cc, i] = (1*255)
        
        # Save masks to the given directory
        cv2.imwrite(output_dir + a['filename'], mask)

# Execute the function to create binary images
polytobinmask(dir_path)
