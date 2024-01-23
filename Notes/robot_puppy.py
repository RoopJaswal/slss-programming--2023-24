# Robot Puppy 
# Author: Roop Jaswal 
# Jan 15, 2024 

from PIL import Image 

ball_image = Image.open("./Images/Red Ball.jpeg")

for y in range(ball_image.height):
    for x in range(ball_image.width):
        r, g, b = ball_image.getpixel((x,y))

        if 220 < r < 255 and 59 < g < 70 and 50 < b < 70: 
            red_pixel_locs.append((x,y))

x_coords = []

for loc in red_pixel_locs: 
    x_coords.append(loc[0])
    y_coords.append(loc[1])

min_x = 1_000_000
max_x = -1

min_x 

print(min_x, max_x, min_y, max_y)

mid_x = max_x - (max_x - min_x)
mid_y = max_y - (max_y - min_y)

print(mid_x, mid_y)

ball_image.putpixel((mid_x, mid_y) 255, 255, 0)
ball_image.putpixel((mid_x +1 mid_y) 255, 255, 0)
ball_image.putpixel((mid_x -1 mid_y) 255, 255, 0)
ball_image.putpixel((mid_x, mid_y) 255, 255, 0)
ball_image.putpixel((mid_x, mid_y) 255, 255, 0)
