# resizer - resizes jpg images from a folder 
import cv2
import imutils
import time
import os

directory = "C:\\Users\\YOURUSERNAME\\Google Drive\\cat project\\"
output_folder = "C:\\Users\\YOURUSERNAME\\Google Drive\\cat project\\Katzenbuch Nr. 26\\out\\"

resize_min = 1000

def resizeImage(imgfile, filename):
	start = time.time()
	output_file = output_folder + filename
	
	img = cv2.imread(imgfile)
	img_w, img_h = img.shape[0:2]

	res_w = 1000
	res_h = 1000
	
	if img_h > img_w:
		res_h = int ( ( res_w / img_w ) * img_h)

	else:
		res_w = int ( ( res_h / img_h ) * img_w)

	res = cv2.resize(img, (res_h, res_w))
	cv2.imwrite(output_file + "_resized.jpg", res)
	end = time.time()
	elapsed = end - start

	print('[resizing done in'+ "{:6.3f}".format(elapsed) + 's for ' + filename + ']' + ' [img] w:' + str(img_w) + 'x' + str(img_h) + ' => ' + str(res_w) + 'x' + str(res_h) + ' writing to ' + output_file)

	# cv2.imshow("resized", imutils.resize(res, height = 200))
	# cv2.imshow("resized",res)
	# cv2.destroyAllWindows()



for filename in os.listdir(directory):
	#if filename.endswith(".jpg") or filename.endswith(".png"): 
	if filename.endswith(".jpg"): 
		filestr = os.path.join(directory, filename)
		resizeImage(filestr, filename)
		# cv2.waitKey(100)
		continue
	else:
		continue
