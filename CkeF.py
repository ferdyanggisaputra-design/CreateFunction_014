def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        converted = (value * 9/5) + 32
        return f"{converted:.2f} F"
    elif unit == 'F':
        converted = (value - 32) * 5/9
        return f"{converted:.2f} C"
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit."

print(convert_temperature(70, 'C'))

circle_area = lambda radius: 3.14 * radius ** 2
radius = float(input("Enter the radius: "))
result = circle_area(radius)
print("Area of the circle is:", result)