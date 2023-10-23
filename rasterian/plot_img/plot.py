def plot_img_and_hist(image, bins=256):
    """Plot an image along with its histogram and cumulative histogram."""
    
    fig, axs = plt.subplots(1, 2) # , sharey=True, tight_layout=True

    # Display image
    ax_img = axs[0]
    ax_img.imshow(image) # , cmap=plt.cm.gray     img = mpimg.imread('your_image.png')
    ax_img.set_axis_off()

    # Display histogram
    ax_hist = axs[1]
    ax_hist.hist(image.ravel(), bins=bins)
    ax_hist.set_xlabel('Pixel intensity')


""" clipped = rasterio.open(out_file)
show((clipped, 3), cmap='terrain') """