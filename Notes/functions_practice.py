# Functions: Practice 
# Author: Roop Jaswal 
# Nov 24, 2023

# Function

def print_area_of_a_square(sidelength: float): 
	"""Calculates the area of a square.
	Results are in units squared.
	
	Params:
	
	sidelength - length of one side of the square"""

	area = sidelength ** 2
	
	print(f"The area of a square with side length = {sidelength} is: {area} square units")

def area_of_a_square(sidelength: float) -> float:
    '''Returns the area of a square with given side length

    Params: 

    sidelength - length of one side of a area_of_a_square
    '''

    area = sidelength ** 2 

    return area 


def stars(numstars: int) -> str: 
	""""""
	return

stars(2) #  ** 
stars(10) # **********



print_area_of_a_square(12)  
print_area_of_a_square(13)
print(area_of_a_square(2))

# sum_areas = area_of_a_square(12) + area_of_a_square(13)
print(area_of_a_square(2))
print(print_area_of_a_square(2))

def stars(num_stars: int) -> str:
    """Return out the number of stars of a given number
    
    Params:
    
    num_stars - the number of stars to return"""

    return "*" * num_stars


def pyramid(num_layers: int) -> None:
    """Print out a pyramid of stars that is
    the given height.
    
    Params:
    
    num_layers - how many rows are in the pyramid
    """

    for current_layer in range(1, num_layers+1):
        print("*" * current_layer)
        # print(stars(current_layer))

def pyramid_mirror(num_layers: int) -> None: 
    """Print a pyramid mirrored of given number of layers.
     
	Params: 
    num_layers - number of layers in the pyramid
    """ 	
    
for current_layer in range(1, num_layers+1):
        spaces = "" * (num_layers - current_layer)
        print(spaces + stars(current_layer))






pyramid()
pyramid_mirror(3)
print(stars())