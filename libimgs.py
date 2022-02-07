from numpy.random import default_rng
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from typing import Optional, Sequence


def select_random_image(files: Sequence, rng):
    img_path = rng.choice(files)
    try:
        return Image.open(img_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The image {img_path} does not exist")


# def generate_random_angle(rng):
#     factor = rng.integers(low=0, high=3, endpoint=True)
#     return factor * 90


# def generate_image(files: Sequence, rng):
#     im = select_random_image(files, rng)
#     ang = generate_random_angle(rng)
#     return im.rotate(ang, expand=True)




def create_grid(files: Sequence, m: int = 2, n: int = 2, verbose: bool = False, seed: Optional[int] = None) -> Sequence:
    """
    Creates a grid of random images with random rotations.

    :param files: list of image paths where the images will be randomly chosen
    :param m: number of rows in the grid
    :param n: number of columns in the grid
    :param verbose: boolean, if True print proceeding of the program
    :param seed: used to seed the random number generator, may be omitted
    :return: a list of list with, in each cell, an `Image` randomly selected from the given sequence
    and randomly rotated of a multiple of 90°
    """
    if seed is None:
        rng = default_rng()
    else:
        rng = default_rng(seed)
    img_grid = []
    for i in range(m):
        if verbose: print(f"row : {i}")
        img_row = []
        for j in range(n):
            if verbose: print(f"\tcolumn : {j}", end='\t')
            img = np.asarray(select_random_image(files, rng))
            check = False
            k = 1
            if j > 0:
                check = (img == img_row[-1]).all()
            if i > 0:
                check = check or (img == img_grid[i - 1][j]).all()
            while check:
                k += 1
                img = np.asarray(select_random_image(files, rng))
                if j > 0:
                    check = (img == img_row[-1]).all()
                if i > 0:
                    check = check or (img == img_grid[i - 1][j]).all()
            if verbose: print(f"{k} tries")
            img_row.append(img)
        img_grid.append(img_row)
    return img_grid


def plot_grid(grid: Sequence, out: Optional[str] = None, verbose: bool = True, bg: Optional[str] = None):
    """
    Plot an image grid.

    :param grid: a list of lists containing `Image` objects to plot
    :param out: a filename that allows to output the resulting image. If omitted, does not save the image
    :param verbose: if true, show the plot before closing
    :param bg: background color when saving to jpg. Default to None but required if jpg
    """
    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            plt.subplot(m, n, n * i + j + 1)
            plt.imshow(grid[i][j])
            plt.axis('off')

    plt.tight_layout()
    if out is not None:
        out_format = out.split('.')[-1]
        if out_format == 'png':
            plt.savefig(out, transparent=True)
        else:
            if bg is None:
                raise ValueError("bg is required if the output format is jpg")
            plt.savefig(out, facecolor=bg)
    if verbose:
        plt.show()
    else:
        plt.close()
