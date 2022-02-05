from os.path import join
import argparse

from libimgs import *


parser = argparse.ArgumentParser(description='Generate a grid of randomly rotated images.')

parser.add_argument('images', type=str, nargs='+', action='append',
                    help='the numbers of the selected images')
parser.add_argument('--folder', type=str, default='img',
                    help='image folder (default: img)')
parser.add_argument('--output', type=str, default='out.jpg',
                    help='output file (default: out.jpg)')
parser.add_argument('-m', '--rows', type=int, default=3,
                    help='Number of row of the grid')
parser.add_argument('-n', '--cols', type=int, default=3,
                    help='Number of columns of the grid')

args = parser.parse_args()

_IMAGE_FOLDER = args.folder

images = [join(_IMAGE_FOLDER, "01.jpg"), join(_IMAGE_FOLDER, "02.jpg")]  # Selected images

M = args.rows  # Number of rows
N = args.cols  # Number of columns

grid = create_grid(images, M, N)
plot_grid(grid, out=args.output)
