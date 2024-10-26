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

## Classes

### ColorImage
```
from Image import ColorImage


# Initialize the ColorImage class
color_image = ColorImage("path/to/color_image.jpg", width=10, height=5, title="Color Image Example") // all optional except paths which is the first argument

# Load the original image
original_image = color_image.get_image()
print("Original Image Shape:", original_image.shape)

# Equalize the image
equalized_image = color_image.equalize_image()
print("Equalized Image Shape:", equalized_image.shape)

# Cancel the red color channel
canceled_red = color_image.cancel_color_channel(['red'])
color_image.draw_images(images=[original_image, canceled_red])

# Draw histograms for the original image
color_image.draw_histogram(images=[original_image], show_image=True)

# Draw histograms for the equalized image
color_image.draw_histogram(images=[equalized_image], show_image=True)
```
### GrayImage
```
from Image import GrayImage

# Initialize the GrayImage class
gray_image = GrayImage("path/to/gray_image.jpg", width=10, height=5, title="Gray Image Example")  // all optional except paths which is the first argument

# Load the original grayscale image
original_gray_image = gray_image.get_image()
print("Original Grayscale Image Shape:", original_gray_image.shape)

# Equalize the grayscale image
equalized_gray_image = gray_image.equalize_image()
print("Equalized Grayscale Image Shape:", equalized_gray_image.shape)

# Draw histogram for the original grayscale image
gray_image.draw_histogram(images=[original_gray_image], color="gray")

# Draw histogram for the equalized grayscale image
gray_image.draw_histogram(images=[equalized_gray_image], color="gray")

# Draw images: original and equalized
gray_image.draw_images(images=[original_gray_image, equalized_gray_image])
```

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
