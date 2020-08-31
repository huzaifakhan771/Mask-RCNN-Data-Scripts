# Mask-RCNN-Data-Scripts

This repository contains two python scripts

1. polytobinary_and_overlay.py creates binary mask images/maps annotation overlay on original images depending on the given flag.

2. create_json_from_binary.py creates annotations for MaskRCNN in JSON format. The input for creating annotations will be binary images, the same size as the RGB images in the training set. Currently, it works for a single object per image.

# Libraries to install for using the scripts

- pip3 install scikit-image
- pip3 install numpy
- pip3 install opencv-contrib-python==3.4.1.15
