# =============================================================================
# PYTHON TUTORIAL - CLEAN VS DIRTY CODE
# =============================================================================

'''
This tutorial will give an example of clean vs dirty code with an easy example and explanation.
We will calculate the area of a rectangle in both clean and dirty code styles.
'''

# =============================================================================
# EXAMPLE I - CLEAN CODE
# =============================================================================
'''
Clean Code:
    - Uses a function with a descriptive name (calculate_area) for reusability and organization.
    - Includes a docstring explaining the function's purpose, arguments, and return value.
    - Uses meaningful variable names (rectangle_length, rectangle_width).
    - Adds comments to explain the calculation step.
    - Uses f-strings for clear labeling of the output.
'''

# This function calculates the area of a rectangle
def calculate_area(length, width):
    """
    This function calculates the area of a rectangle.

    Args:
        length (int)    : The length of the rectangle.
        width (int)     : The width of the rectangle.

    Returns:
        int             : The area of the rectangle.
    """
    area = length * width
    return area

# Get rectangle dimensions
rectangle_length = 5
rectangle_width  = 3

# Calculate and print the area
area             = calculate_area(rectangle_length, rectangle_width)
print(f"The area of the rectangle is: {area}")

# =============================================================================
# EXAMPLE I - DIRTY CODE
# =============================================================================
'''
Dirty Code:
    - Lacks function encapsulation, making the code less reusable.
    - Doesn't explain the purpose of the code.
    - Uses generic variable names (length, width).
    - Lacks comments for better understanding.
    - Uses a plain print statement without informative labels.
'''

# This code calculates the area of a rectangle
length  = 5                 # No explanation for variable
width   = 3                 # No explanation for variable
area    = length * width    # No comments explaining calculation
print(area)                 # No label for output

