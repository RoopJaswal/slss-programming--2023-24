# Colour Helper 
# Author: Roop 
# Dec 19, 2023 

from PIL import Image
import colour_helper

def is_light(pixel: tuple) -> bool: 
    """Returns true if the pixel is a "light" pixel
    
    Params: 
        pixel - 3-tuple of values r, g, b
    
    red, green, blue = pixel 
    """

    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128: 
        return True

    else: 
        return False
    

def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Return a gray version of the given pixel"""

    red, green, blue = pixel

    gray = int(red * 0.3 + green * 0.59 + blue * 0.11) 

    return (gray, gray, gray)

def picture_to_grayscale(filename: str) -> None: 
    """Convert a picture to grayscale"""

    with Image.open(f"./Images/{filename}") as im: 
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel(((x, y)))
               
                gray_pixel = colour_helper.pixel_to_grayscale(pixel)

                im.putpixel((x, y), gray_pixel)

        im.save("./Images/grayscale.jpg")

picture_to_grayscale("best_pizza.jpg")

# Test? 
light_pixel = (125, 125, 125)
light_gray = (140, 140, 140)
dark_gray = (170, 170, 170)
dark_pixel = (175, 175, 175)



print(is_light(light_pixel))
print(is_light(light_gray))
print(is_light(dark_pixel))
print(is_light(dark_gray))


with Image.open("./Images/best_pizza.jpg") as im: 

 for y in range(im.height):
        for x in range(im.width):
             pixel = im.getpixel((x, y))

             if is_light(pixel): 
                 im.putpixel((x, y), light_pixel)
             else:
                im.putpixel((x, y), dark_pixel)

im.save("./Images/grey_scaled.jpg")