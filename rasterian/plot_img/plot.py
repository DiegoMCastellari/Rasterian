import numpy as np
import matplotlib.pyplot as plt

def plot_color(image, band_1, band_2, band_3):

    band_1_position = band_1 -1
    band_2_position = band_2 -1
    band_3_position = band_3 -1
    b1 = image[band_1_position]
    b2 = image[band_2_position]
    b3 = image[band_3_position]

    rgb = np.dstack((b1,b2,b3))
    norm = (rgb * (255 / np.max(rgb))).astype(np.uint8)

    # plot RGB
    plt.imshow(norm)

def plot_band_and_hist(image_band, bins=256):
    """Plot an image along with its histogram and cumulative histogram."""
    
    fig, axs = plt.subplots(1, 2) # , sharey=True, tight_layout=True

    # Display image
    ax_img = axs[0]
    ax_img.imshow(image_band) # , cmap=plt.cm.gray     img = mpimg.imread('your_image.png')
    ax_img.set_axis_off()

    # Display histogram
    ax_hist = axs[1]
    ax_hist.hist(image_band.ravel(), bins=bins)
    ax_hist.set_xlabel('Pixel intensity')