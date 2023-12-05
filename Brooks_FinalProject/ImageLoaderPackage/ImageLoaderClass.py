# ImageLoader.py
from PIL import Image

class ImageLoader:
    def __init__(self, file_path):
        '''
      Constructor for the ImageLoaderClass
      @Param: file_path: The path to the image
      '''
        # Constructor to initialize the file path
        self.file_path = file_path

    def load_image(self):
        '''
        Returns an image
        @Return: Image
        '''
        try:
            # Try opening the image file using PIL's Image.open method
            with Image.open(self.file_path) as img:
                # Show the image using PIL's show method
                img.show()
                # Return the loaded image object
                return img
        except FileNotFoundError:
            # Handle the case where the file is not found
            print('Image not found')