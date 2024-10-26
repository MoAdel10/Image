# Image Processing Classes Documentation

## Overview
This project provides two classes, `ColorImage` and `GrayImage`, designed for loading, processing, and visualizing color and grayscale images. These classes allow users to perform image equalization, histogram generation, and channel manipulation.

## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Classes](#classes)
  - [ColorImage](#colorimage)
  - [GrayImage](#grayimage)
- [Usage Examples](#usage-examples)
  - [Example for ColorImage](#example-for-colorimage)
  - [Example for GrayImage](#example-for-grayimage)
- [Author](#author)

## Installation
To get started with this project, follow the steps below:

1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Install the required dependencies using pip:

```bash
pip install numpy Pillow matplotlib
```

## Dependencies
- numpy
- Pillow
- matplotlib



## Usage Examples
### Example for ColorImage
```python

color1 = ColorImage(r"C:\coding\python\Image\Images\color1.png") # load the image
eq_color = color1.equalize_image() #create a equalized image of the color1 loaded image
color1.draw_images([color1.get_image(),eq_color]) # draw the array of images provided
color1.draw_histogram([color1.get_image()]) # draw the histogram for the provided images

```

### Example for GrayImage
```python
gray1 = GrayImage(r"C:\coding\python\Image\Images\gray1.jpg") # load the image
gray1.draw_images([gray1.get_image()]) # draw the array of images provided
gray1.draw_histogram([gray1.get_image()]) # draw the histogram for the provided images

```


## Author
Mohamed Adel - feel free to use , edit and push updates 🗣
