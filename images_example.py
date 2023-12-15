# Images 
# Author: Roop Jaswal
# Dec 14, 2023 


from PIL import Image

# open up kid green

def pixel_to_name(pixel: tuple) -> str:
    """Given a pixel, return the name of the colour"""

    # red less than 25
    # blue less than 25
    # green is more than 250
    r, g, b = pixel

    if r < 120 and b < 120 and g > 220:
        return "green"
    else:
        return "unknown colour"

with Image.open("./Images/kid-green.jpg") as im:
    # grab the pixel at the top left cornuh
    image_width, image_height = im.width, im.height

    bg_im = Image.open("./Images/beach.jpg")

    # top -> bottom
    # left -> right
    for y in range(image_height):
        for x in range(image_width):
            pixel = im.getpixel((x, y))

            # if current pixel is green
            if pixel_to_name(pixel) == "green":
                # replace it with bg_im pixel in same loc
                bg_pixel = bg_im.getpixel((x, y))

                im.putpixel((x, y), bg_pixel)

    bg_im.close()

    # Save image
    im.save("./Images/output.jpg")