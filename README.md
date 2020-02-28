# overlap-crop-and-recover-image
In some image segmentation task (such as nuclei segmentation), because large image size, it can not be input into the neural network directly. It is a good choice to crop large images into small ones as input of neural network. But one of the defects of this method is that the edge information may be lost, for example, some cells are cut in half in small nuclei images. In order to solve this problem, this programme uses the method of overlapping crop to get the small overlapped image. After putting the small image into the neural network and getting the segmentation resulting images, only the middle part of each resulting image is taken and the edge part is discarded, and all the middle parts are recovered to the original image size segmentation result.
# visualization effect
original image:

![image](https://github.com/flyingdingding/overlap-crop-and-recover-image/blob/master/test_images/resize_2.png)

cropped images:

![image](https://github.com/flyingdingding/overlap-crop-and-recover-image/blob/master/test_images/resize_3.jpg)

recovered image:

![image](https://github.com/flyingdingding/overlap-crop-and-recover-image/blob/master/test_images/resize_2.png)

## Prerequisites
- Python 3.x
- numpy
- pillow
