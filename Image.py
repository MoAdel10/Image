import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

class ColorImage:
    def __init__(self, path, width=10, height=5, title="Untitled", xLabel="Pixel Intensity", yLabel="Number of Pixels", lim=[0, 255]) -> None:
        self.path = path
        self.width = width
        self.height = height
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.lim = lim
        self.imageMatrix = self.load_image()  
        self.equalizedMatrix = None 

    def load_image(self): 
        """Load the image as an RGB array."""
        image = Image.open(self.path).convert('RGB')
        return np.array(image)

    def get_image(self): 
        """Return the original image matrix."""
        return self.imageMatrix

    def equalize_image(self): 
        """Equalize the image and store the result."""
        equalized_channels = []
        for i in range(3): 
            channel = Image.fromarray(self.imageMatrix[..., i])
            equalized_channel = ImageOps.equalize(channel)
            equalized_channels.append(np.array(equalized_channel))

        self.equalizedMatrix = np.stack(equalized_channels, axis=-1)
        return self.equalizedMatrix

    def cancel_color_channel(self, channels_to_cancel):
        """Cancel specified color channels."""
        channel_indices = {'red': 0, 'green': 1, 'blue': 2}

        for channel in channels_to_cancel:
            if channel.lower() not in channel_indices:
                raise ValueError("Channels must be 'red', 'green', or 'blue'.")

        canceled_image = np.copy(self.imageMatrix)

        for channel in channels_to_cancel:
            canceled_image[..., channel_indices[channel.lower()]] = 0

        return canceled_image

    def draw_histogram(self, images=None, bins=256, range=(0, 255), colors=["red", "green", "blue"], show_image=False):
        """Draw separate histograms for each channel (R, G, B)."""
        if images is None:
            images = [self.imageMatrix]  
        
        for i, image in enumerate(images):
            plt.figure(figsize=(self.width, self.height + (self.height if show_image else 0)))

            for j, color in enumerate(colors): 
                plt.subplot(4 if show_image else 3, 1, j + 1) 
                plt.hist(image[..., j].flatten(), bins=bins, range=range, color=color)
                plt.title(f"{color.upper()} Channel Histogram")
                plt.xlabel(self.xLabel)
                plt.ylabel(self.yLabel)
                plt.xlim(self.lim)
                plt.grid(True)

            if show_image:
                plt.subplot(4, 1, 4)  
                plt.imshow(image)
                plt.axis('off')
                plt.title("Image")

            plt.tight_layout()
            plt.show()

    def draw_images(self, images=None):
        """Draw the original or equalized images."""
        if images is None:
            images = [self.imageMatrix]  
        
        plt.figure(figsize=(10, 5 * len(images)))

        for i, image in enumerate(images):
            plt.subplot(len(images), 1, i + 1)
            plt.title(f"Image {i + 1}")
            plt.imshow(image)
            plt.axis('off')

        plt.tight_layout()
        plt.show()

# Usage example
# color_image = ColorImage("image.jpg")
# color_image.draw_histogram(show_image=True)


class GrayImage:
    def __init__(self, path, width=10, height=5, title="Untitled", xLabel="Pixel Intensity", yLabel="Number of Pixels", lim=[0, 255]) -> None:
        self.path = path
        self.width = width
        self.height = height
        self.title = title
        self.xLabel = xLabel
        self.yLabel = yLabel
        self.lim = lim
        self.imageMatrix = self.load_image()
        self.equalizedMatrix = None  

    def load_image(self): 
        """Load the image as a grayscale array."""
        image = Image.open(self.path).convert('L')  
        return np.array(image)

    def get_image(self): 
        """Return the original grayscale image."""
        return self.imageMatrix

    def equalize_image(self): 
        """Equalize the grayscale image and return the result."""
        image = Image.fromarray(self.imageMatrix) 
        self.equalizedMatrix = ImageOps.equalize(image)  
        return np.array(self.equalizedMatrix)

    def draw_histogram(self, images=None, bins=256, range=(0, 255), color="gray", alpha=1):
        """Draw a histogram of an image or a list of images."""
        if images is None:
            images = [self.imageMatrix]  
        
        plt.figure(figsize=(self.width, self.height))

        for i, image in enumerate(images):
            plt.subplot(len(images), 1, i + 1)
            plt.hist(image.flatten(), bins=bins, range=range, color=color, alpha=alpha)
            plt.title(f"Histogram of Image {i + 1}")
            plt.xlabel(self.xLabel)
            plt.ylabel(self.yLabel)
            plt.xlim(self.lim)
            plt.grid()  

        plt.tight_layout()
        plt.show()

    def draw_images(self, images=None):
        """Draw an image or a list of images."""
        if images is None:
            images = [self.imageMatrix]
        
        plt.figure(figsize=(10, 5 * len(images)))

        for i, image in enumerate(images):
            plt.subplot(len(images), 1, i + 1)
            plt.title(f"Image {i + 1}")
            plt.imshow(image, cmap='gray')
            plt.axis('off')

        plt.tight_layout()
        plt.show()

# Usage example for GrayImage
# gray_image = GrayImage("image.jpg") use raw string for better results 
# equalized_image = gray_image.equalize_image()
# gray_image.draw_images()
# gray_image.draw_images(images=[gray_image.get_image(), gray_image.equalize_image()])
# gray_image.draw_histogram()
# gray_image.draw_histogram(images=[equalized_image])
