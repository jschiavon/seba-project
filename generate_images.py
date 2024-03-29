import os
import argparse
import re

from libimgs import *

from pyfiglet import Figlet

parser = argparse.ArgumentParser(description="Generate a grid of random images taken from a group of folders.",
                                 epilog="""All the images to be used should be saved within one (or more folder). 
                                 Only the folders' name is required, and all the images within the selected folders 
                                 will then be used.""")
parser.add_argument('folders', type=str, nargs='+',
                    help='the numbers of the folders to use')
parser.add_argument('--output', type=str, default=None,
                    help="output file name (default: don't save)")
parser.add_argument('--format', type=str, choices=['jpg', 'png'], default='png',
                    help="output format (default: png)")
parser.add_argument('--bg', type=str, default=None,
                    help="hex code of the background color (only for jpg images)")
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

    images = []
    for dirs in args.folders:
        dir_name = os.path.join("imgs", dirs)
        images += [os.path.join(dir_name, f) for f in os.listdir(dir_name)
                   if ((f[0] != '.') and os.path.isfile(os.path.join(dir_name, f)))]

    if args.verbose:
        print(images)

    if args.format == 'jpg' and args.bg is None:
        raise ValueError("Background color is required for jpg images!")
    if args.bg is not None:
        bg = args.bg
        if bg[0] != '#':
            bg = '#' + bg
        if not re.search("^#(?:[0-9a-fA-F]{3}){1,2}$", bg):
            raise ValueError(f"Bg color specified wrongly: it has to be a 6-digit hex code, got {bg} instead")
    else:
        bg = None
    M = args.rows  # Number of rows
    N = args.cols  # Number of columns

    if args.rep > 1:
        for i in range(args.repeat):
            if args.verbose:
                print(f"Repetition {i+1}:")
            if args.output is None:
                out = None
            else:
                try:
                    os.makedirs('outputs')
                except FileExistsError:
                    pass
                out = os.path.join('outputs', f"{args.output}_{i}.{args.format}")
            grid = create_grid(images, M, N, verbose=args.verbose)
            if args.verbose:
                print(f"Grid created with ({M} x {N}) images")
            plot_grid(grid, out=out, verbose=args.verbose, bg=bg)
    else:
        if args.output is None:
            out = None
        else:
            try:
                os.makedirs('outputs')
            except FileExistsError:
                pass
            out = os.path.join('outputs', f"{args.output}.{args.format}")
        grid = create_grid(images, M, N, verbose=args.verbose)
        if args.verbose:
            print(f"Grid created with ({M} x {N}) images")
        plot_grid(grid, out=out, verbose=args.verbose, bg=bg)
