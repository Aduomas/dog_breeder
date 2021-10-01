from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def shred_row(img, count):
    crop_height_size = count * (img.shape[0] // count)
    crop_width_size = count * (img.shape[1] // count)
    images = np.vsplit(img[:crop_height_size,:crop_width_size, :], count)
    return np.concatenate((images[::2], images[1::2]), axis=2)


def shred_col(img, count):
    crop_height_size = count * (img.shape[0] // count)
    crop_width_size = count * (img.shape[1] // count)
    images = np.hsplit(img[:crop_height_size, :crop_width_size, :], count)
    return np.concatenate((images[::2], images[1::2]), axis=1)


image = np.array(Image.open("769157.jpg"))


output = image.copy()

# parts = 200  # must be even
# iterrations = 2 # must be even
# for i in range(iterrations):
#     output = np.concatenate((shred_row(output, parts)), axis=0)
#     output = np.concatenate((shred_col(output, parts)), axis=1)

parts = 200  # must be even
iterrations = 2 # must be even
for j in range(200, 1200, 200):
    parts = j
    for z in range(1, 5):
        iterrations = z
        for i in range(iterrations):
            output = np.concatenate((shred_row(output, parts)), axis=0)
            output = np.concatenate((shred_col(output, parts)), axis=1)

        im = Image.fromarray(output)
        output = image.copy()
        im.save(f"./results/{iterrations**2}_{iterrations**2}_dogs_{j}_parts.jpg")

plt.imshow(output)
plt.show()
