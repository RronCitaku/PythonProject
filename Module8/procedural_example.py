def calculate_area(lenght, width):
    return lenght * width

def calculate_perimeter(lenght, width):
    return 2 * (lenght + width)

lenght = 5
width = 3

area = calculate_area(lenght, width)
perimeter = calculate_perimeter(lenght, width)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
