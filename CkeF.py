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

print(convert_temperature(70, 'C'))  # Output: 120.00 F