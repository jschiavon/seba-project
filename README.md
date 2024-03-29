```
                _____                              __  __       _        _      
               |_   _|                            |  \/  |     | |      (_)     
                 | |  _ __ ___   __ _  __ _  ___  | \  / | __ _| |_ _ __ ___  __
                 | | | '_ ` _ \ / _` |/ _` |/ _ \ | |\/| |/ _` | __| '__| \ \/ /
                _| |_| | | | | | (_| | (_| |  __/ | |  | | (_| | |_| |  | |>  < 
               |_____|_| |_| |_|\__,_|\__, |\___| |_|  |_|\__,_|\__|_|  |_/_/\_\
                                       __/ |                                    
                                      |___/                                     
```

A small script to generate a grid of random images

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
Now you are ready to install the required packages. First, update the `pip` package with
```bash
python -m pip install --upgrade pip
```
and then install the required packages:
```bash
python -m pip install -r requirements.txt
```
Finally, you need to prepare the images for the script: place them within some folder in the same root of the program. The folders and images names are irrelevant.

## Use the script
To use the script simply run
```bash
python generate_images.py [floders ...]
```
in the same terminal. Notice that a mandatory argument is required: the folders to use. It is enough to provide the names of the folders that we want to use separated by spaces.

An example of call then is `python generate_images.py red black colorful` to generate a matrix of random images pulled randomly from the red, black and colorful folder. 
Notice that all these folders should be stored within a parent `imgs` folder (that exists, empty, in the repository).

Other possible options are shown in the help of the program, obtained by running `python generate_images.py --help` and is provided here:
```bash
usage: generate_images.py [-h] [--output OUTPUT] [--format {jpg,png}] [--bg BG] [-m ROWS] [-n COLS]
                          [-v] [-r REP]
                          folders [folders ...]

Generate a grid of random images taken from a group of folders.

positional arguments:
  folders               the folders to use

options:
  -h, --help            show this help message and exit
  --output OUTPUT       output file name (default: don't save)
  --format {jpg,png}    output format (default: png)
  --bg BG               hex code of the background color (only for jpg images)
  -m ROWS, --rows ROWS  Number of row of the grid (default 3)
  -n COLS, --cols COLS  Number of columns of the grid (default 3)
  -v, --verbose         Verbosity of the script (default False)
  -r REP, --repeat REP  how many repeating of the generation (default 1)

All the images to be used should be saved within one (or more folder). Only the folders' name is required, and all the images within the selected folders will then be used.
```

If the `--output` option is chosen and an output name is provided, the resulting image will be saved in the folder `outputs`.
