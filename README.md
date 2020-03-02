# Mask-RCNN-Data-Scripts

This repository contains two python scripts

1. polytobinarymask.py creates binary mask images from the polygons read from JSON annotation files.

2. mapmaskoverlay.py creates overlays of those masks on the original images to visualize the masks' accuracy.

# Libraries to install for using the scripts

pip3 install scikit-image
pip3 install numpy
pip3 install opencv-contrib-python==3.4.1.15
