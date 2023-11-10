def calculate_area_triangle(base, height):
    try:
        if base >= 0 and height >= 0:
            area = 0.5 * base * height
            return area
        else:
            return ValueError("Invalid input! Please enter valid number for base and height.")
    except ValueError as e:
        return str(e)