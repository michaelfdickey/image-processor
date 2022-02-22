# image-processor

## Final project for CIS555 Mastering Data Structures:

- you write a function that takes an image as input and produces a new image as output.
- All of your work will be on the file `plugins.py`
- use `pictool.py` to check your work (like a test script)
- there are several pictures in the folder `images`, which you will process
- The folder `solutions` shows what the images should look like after processing

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
