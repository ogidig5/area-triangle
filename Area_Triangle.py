import math 

print("""Choose a formular you want to use to calculate the area of your triangle.
        1. Heron's Formula
        2. 1/2 * base * height
        3. 1/2 * ab * sin(angle)""")
question = int(input("Which formular do you wish to use?(1, 2 or 3): "))

def main():
    if question == 1:
        herons_formula = area_herons()
        print(f"The area of your triangle is: {herons_formula:.2f} cm2")
    elif question == 2:
        base_height_formula = area_base_height()
        print(f"The area of your triangle is: {base_height_formula:.2f} cm2")
    elif question == 3:
        sine_formula = area_sine()
        print(f"The area of your triangle is: {sine_formula:.2f} cm2")
    
def area_herons():
    ''' This function is meant to calculate the semi-perimeter of the
    triangle by suming up all the length of the sides
    of the triangle. The formula to achieve this is: S = 1/2(a+b+c),
    where a, b, and c are the length of the sides of the triangle.
    After that, we will calculate the area using the heron's formula.

    Parameter: Nothing
    Return: Area.
    '''

    side_1 = float(input("Please input the length of the first side of your triangle: "))
    side_2 = float(input("Please input the length of the second side of your triangle: "))
    side_3 = float(input("Please input the length of the third side of your triangle: "))

    semi_perimeter = 1/2 * (side_1 + side_2 + side_3)
    area = math.sqrt((semi_perimeter*(semi_perimeter-side_1)*(semi_perimeter-side_2)*(semi_perimeter-side_3)))
    return area

def area_base_height():
    '''This function calculates the area of a triangle when the base and height have been provided.
    Parameter: None
    Return: Area
    '''
    base = float(input("Please input the base of your triangle: "))
    height = float(input("Please input the height of your triangle: "))

    area = 1/2 * base * height
    return area

def area_sine():
    '''This function calculates the area of a triangle when two sides and an angle have been provided.
    Parameter: None
    Return: Area
    '''
    side_a = float(input("Please input the first side length of your triangle: "))
    side_b = float(input("Please input the second side length of your triangle: "))
    angle = float(input("Please enter the size of the angle subtended by the triangle: "))

    area = 1/2 * (side_a * side_b) * math.sin(math.radians(angle))
    return area

if __name__ == "__main__":
    main()
