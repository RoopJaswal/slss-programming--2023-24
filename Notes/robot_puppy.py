# Robot Puppy 
# Author: Roop Jaswal 
# Jan 15, 2024 

from PIL import Image 
import colour_helper

red = (255,0,0)

def pixel_to_name(pixel: tuple) -> str:
    """Given a 3-tuple, return a string representing
    its colour

    Params:
        pixel = 3-tuple of values (red, green, blue)

    Returns:
        name of the colour
    """
    red, green, blue = pixel

    # TODO: detect red pixels
    if red < 200 and blue < 200 and green > 220:
        return "green"
    elif red > 170 and green < 60 and blue < 60:
        return "red"
    else:
        return "colour unknown"

# Identify the red pixels in the image 

# Pinpoint the location of the red pixels in the image 

# Locate the x, y of the centre of the red ball 





