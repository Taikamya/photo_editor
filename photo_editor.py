from PIL import Image, ImageFilter
import os

# where unedited images are
photos_folder = "./photos/"
# where edited images will be
edited_folder = "./editedPhotos/"

# function to sharpen a single image
def sharpen(file: str) -> None:
    '''This function applies the SHARPEN filter to an image file. '''
    # test photo
    test_photo = photos_folder + file
    img = Image.open(test_photo)
    # Slight sharpen effect
    filtered_img = img.filter(ImageFilter.SHARPEN)
    # Clean filename to save it as something else
    clean_filename = os.path.splitext(file)[0]
    filtered_img.save(f"{edited_folder}/{clean_filename}_edited.jpg")


# function to sharpen ALL the photos inside a folder
def sharpen_all() -> None:
    '''This function applies the SHARPEN filter to all photos inside a folder. '''
    for filename in os.listdir(photos_folder):
        img = Image.open(photos_folder + filename)
        # Changed WxH resolution of the image and tilted to 90º. Used "rotate" to correct that.
        filtered_img = img.filter(ImageFilter.SHARPEN)
        # Clean filename to save it as something else
        clean_filename = os.path.splitext(filename)[0]
        filtered_img.save(f"{edited_folder}{clean_filename}_edited.jpg")


if __name__=="__main__":
    # sharpen("face.jpg")
    sharpen_all()
