from optparse import OptionParser
import numpy as np
from PIL import Image
from crop_recover import *

def get_args():
	parser = OptionParser()
	parser.add_option('-e', '--cropped_image_height', dest='crop_height', default=256, 
			type='int',help='cropped image height')
	parser.add_option('-i', '--cropped_image_width', dest='crop_width', default=256,
			type='int', help='cropped image width')
	parser.add_option('-l', '--overlap_coefficient', dest='oc', default=2,
			type='int', help='how many times a image is cropped')
	(options, args) = parser.parse_args()
	return options

if __name__ == '__main__':
	args = get_args()
	image = np.array(Image.open('../test_images/1.tif'))
	cropped_images = crop_image(image, args.crop_height, args.crop_width, args.oc)
	print(cropped_images.shape)
	recovered_image = recover_image(cropped_images, image.shape[0], image.shape[1], args.crop_height, args.crop_width, args.oc)
	recovered_image = Image.fromarray(recovered_image)
	recovered_image.save('../test_images/output_1.png')


	
	






