# Map overlays of the ROI in binary masks on the original image and save them to a directory
# Changes needed in the code: imgfolder, maskfolder, output_dir

import cv2
import os
import numpy as np

imgfolder = "/home/huzaifakhan771/Documents/dataset"
maskfolder = "/home/huzaifakhan771/Documents/res"
output_dir = "/home/huzaifakhan771/Documents/maskmap/"


imgname = []
images = []
mask = []

# read original images from the given folder
for filename in sorted(os.listdir(imgfolder)):
	if not filename.endswith(".json"): # Do not read the JSON file if in same folder
		images.append(cv2.imread(os.path.join(imgfolder,filename)))
		imgname.append(filename)

# read binary masks from given foler
for filename in sorted(os.listdir(maskfolder)):
	mask.append(cv2.imread(os.path.join(maskfolder, filename), 0))

# create a red overlay on ROI to verify bounding polygons
for i in range(len(mask)):
	redImg = np.zeros(images[i].shape, images[i].dtype)
	redImg[:,:] = (0, 0, 255)
	redMask = cv2.bitwise_and(redImg, redImg, mask=mask[i])
	cv2.addWeighted(redMask, 1, images[i], 1, 0, images[i])
	cv2.imwrite(output_dir + imgname[i], images[i])
