from os.path import join
import argparse

from libimgs import *

from pyfiglet import Figlet

parser = argparse.ArgumentParser(description="Generate a grid of randomly rotated images.",
                                 epilog="""The images in the image folder should be named 'X.jpg' with X a 2-digits
                                        padded number starting from '01.jpg'. Dealing with formats different from 
                                        jpg is still not implemented.""")
parser.add_argument('images', type=int, nargs='+',
                    help='the numbers of the selected images')
parser.add_argument('--folder', type=str, default='img',
                    help='image folder (default: img)')
parser.add_argument('--output', type=str, default=None,
                    help="output file name root (default: don't save)")
parser.add_argument('-m', '--rows', type=int, default=3,
                    help='Number of row of the grid (default 3)')
parser.add_argument('-n', '--cols', type=int, default=3,
                    help='Number of columns of the grid (default 3)')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='Verbosity of the script (default False)')
parser.add_argument('-r', '--repeat', type=int, default=1, dest='rep',
                    help='how many repeating of the generation (default 1)')

if __name__ == '__main__':
    f = Figlet(font='big')
    print(f.renderText('Image Matrix'))

    args = parser.parse_args()

    images = [join(args.folder, f"{i:02}.jpg") for i in args.images]  # Selected images

    M = args.rows  # Number of rows
    N = args.cols  # Number of columns

    if args.rep > 1:
        for i in range(args.repeat):
            if args.output is None:
                out = None
            else:
                out = join(args.folder, f"{args.output}_{i}.jpg")
            grid = create_grid(images, M, N, verbose=args.verbose)
            plot_grid(grid, out=out)
    else:
        if args.output is None:
            out = None
        else:
            out = join(args.folder, f"{args.output}.jpg")
        grid = create_grid(images, M, N, verbose=args.verbose)
        plot_grid(grid, out=out)
