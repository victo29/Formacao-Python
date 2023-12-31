import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_historigrams
from skimage.metrics import structural_similarity

def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Specify 2 images with de same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(gray_image1, gray_image2, full=True)
    print("Similarity of the images: ", score)
    normalized_diffrence_image = (difference_image-np.min(difference_image))/(np.max(difference_image)-np.min(difference_image))
    return normalized_diffrence_image

def transfer_histogram(image1, image2):
    matched_image = match_historigrams(image1, image2, multichannel=True)
    return matched_image