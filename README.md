# image-processor

## Final project for CIS555 Mastering Data Structures:

### Objectives:
- you write a function that takes an image as input and produces a new image as output.
- All of your work will be on the file `plugins.py`
- use `pictool.py` to check your work (like a test script)
- there are several pictures in the folder `images`, which you will process
- The folder `solutions` shows what the images should look like after processing

### Usage:

Image processing is executed as such:

```
python3 pictool.py [plugin] images/[picture].png [processed-picture].png
```

for example, `dered` removes red:

```
python3 pictool.py dered images/Walker.png Walker2-dered.png
```

Some plugins have additional options, added as a `--option=True` flag:

```
python3 pictool.py mono images/Walker.png Walker2.png --sepia=True
```

### Note:

I also added a more useful, imo, text output / grid display in the `display` module for troubleshooting image processing.  Resulting output lists each pixel in a grid array with RGBA values. For example, `block_small_3.png` looks like:

```
['R255', 'R255', 'R255', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G255', 'G255', 'G255']
['B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']

['R255', 'R255', 'R255', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G255', 'G255', 'G255']
['B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']

['R255', 'R255', 'R255', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G255', 'G255', 'G255']
['B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ', 'B0  ']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']

['R0  ', 'R0  ', 'R0  ', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G254', 'G254', 'G254']
['B255', 'B255', 'B255', 'B255', 'B255', 'B255']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']

['R0  ', 'R0  ', 'R0  ', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G254', 'G254', 'G254']
['B255', 'B255', 'B255', 'B255', 'B255', 'B255']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']

['R0  ', 'R0  ', 'R0  ', 'R255', 'R255', 'R255']
['G0  ', 'G0  ', 'G0  ', 'G254', 'G254', 'G254']
['B255', 'B255', 'B255', 'B255', 'B255', 'B255']
['A255', 'A255', 'A255', 'A255', 'A255', 'A255']
```
