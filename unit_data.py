length_units = {
    "meter": 1,
    "kilometer": 1000,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.34,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254
}

weight_units = {
    "kilogram": 1,
    "gram": 0.001,
    "milligram": 0.000001,
    "metric ton": 1000,
    "pound": 0.453592,
    "ounce": 0.0283495
}

temperature_units=("Fahrenheit", "Kelvin", "Celsius")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert input to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        value = value - 273.15

    # Convert Celsius to target
    if to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    elif to_unit == "Celsius":
        return value

volume_units = {
    "liter": 1,
    "milliliter": 0.001,
    "cubic meter": 1000,
    "cubic centimeter": 0.001,
    "cubic inch": 0.0163871,
    "cubic foot": 28.3168,
    "gallon (US)": 3.78541,
    "quart (US)": 0.946353,
    "pint (US)": 0.473176,
    "cup (US)": 0.24,
    "fluid ounce (US)": 0.0295735,
    "tablespoon (US)": 0.0147868,
    "teaspoon (US)": 0.00492892
}


time_units = {
    "second": 1,
    "minute": 60,
    "hour": 3600,
    "day": 86400,
    "week": 604800
}

area_units = {
    "square meter": 1,
    "square kilometer": 1_000_000,
    "square centimeter": 0.0001,
    "square millimeter": 0.000001,
    "square mile": 2_589_988.11,
    "square yard": 0.836127,
    "square foot": 0.092903,
    "square inch": 0.00064516,
    "hectare": 10_000,
    "acre": 4046.86
}

speed_units = {
    "m/s": 1,
    "km/h": 0.277778,
    "mph": 0.44704,
    "knot": 0.514444,
    "ft/s": 0.3048
}

energy_units = {
    "joule": 1,
    "kilojoule": 1000,
    "calorie": 4.184,
    "kilocalorie": 4184,
    "watt-hour": 3600,
    "kilowatt-hour": 3_600_000,
    "electronvolt": 1.60218e-19,
    "BTU": 1055.06
}

pressure_units = {
    "pascal": 1,
    "kilopascal": 1000,
    "bar": 100000,
    "atmosphere": 101325,
    "mmHg": 133.322,
    "torr": 133.322,
    "psi": 6894.76
}

power_units = {
    "watt": 1,
    "kilowatt": 1000,
    "megawatt": 1_000_000,
    "horsepower": 745.7,
    "BTU/hour": 0.293071,
    "calorie/second": 4.184
}

frequency_units = {
    "hertz": 1,
    "kilohertz": 1_000,
    "megahertz": 1_000_000,
    "gigahertz": 1_000_000_000
}

data_storage_units = {
    "bit": 0.125,                  # 1 bit = 1/8 byte
    "byte": 1,
    "kilobyte (KB)": 1024,
    "megabyte (MB)": 1024**2,
    "gigabyte (GB)": 1024**3,
    "terabyte (TB)": 1024**4,
    "petabyte (PB)": 1024**5
}
# binary units (base 1024)

angle_units = {
    "degree": 1,
    "radian": 57.2958,     # 1 radian ≈ 57.2958 degrees
    "gradian": 0.9,        # 1 gradian = 0.9 degree
    "minute of arc": 1 / 60,
    "second of arc": 1 / 3600
}


# general conversion function, not for temperature


categories={"Length": length_units, "Weight/Mass": weight_units, "Temperature": temperature_units, "Volume": volume_units, "Area": area_units, "Speed": speed_units, "Time": time_units, 
            "Energy": energy_units, "Pressure": pressure_units, "Power": power_units, "Frequency": frequency_units, "Data Storage": data_storage_units,
              "Angles": angle_units, "": ""}