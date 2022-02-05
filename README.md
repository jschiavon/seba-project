# Seba-project
A small script to generate a grid of random rotated images

## Install and satisfy requirements
Open a terminal and move to the root folder of the project, then create a virtual environment
```bash
python -m venv .venv
```
and activate it (for windows)
```bash
.venv\Scripts\activate.bat
```
(and for Unix / MacOS)
```bash
source .venv/bin/activate
```
Now you are ready to install the required packages. Firstly, update the `pip` package with
```bash
python -m pip install --upgrade pip
```
and then install the required packages:
```bash
python -m pip install -r requirements.txt
```
Finally, you need to prepare the images for the script: place them within the folder `img/` with for names integer number padded to two digits (*i.e.* `01.jpg`, `02.jpg`, ..., `10.jpg`, `11.jpg`, ...)

## Use the script
To use the script simply run
```bash
python generate_images.py [images ...]
```
in the same terminal. Notice that a mandatory argument is required: the images to be selected. It is enough to provide the *un*-padded numbers (for instance `1 2 5`).

An example of call then is `python generate_images.py 1 2 5`. Other possible options are shown in the help of the program, obtained by running `python generate_images.py --help` and is provided here:
```bash
usage: generate_images.py [-h] [--folder FOLDER] [--output OUTPUT] [-m ROWS] [-n COLS] [-v]
                          images [images ...]

Generate a grid of randomly rotated images.

positional arguments:
  images                the numbers of the selected images

options:
  -h, --help            show this help message and exit
  --folder FOLDER       image folder (default: img)
  --output OUTPUT       output file (default: out.jpg)
  -m ROWS, --rows ROWS  Number of row of the grid (default 3)
  -n COLS, --cols COLS  Number of columns of the grid (default 3)
  -v, --verbose         Verbosity of the script (default False)
```
