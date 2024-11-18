def cel_to_far_kel(temp_c):
    # Celsius to Fahrenheit
    cel_far = (9 / 5) * temp_c + 32
    # Celsius to kelvin
    cel_kel = temp_c + 273.15
    return cel_far, cel_kel

def far_to_cel_kel(temp_f):
    # Fahrenheit to Celsius
    far_cel = 5 / 9 * (temp_f - 32)
    # Fahrenheit to kelvin
    far_kel = far_cel + 273.15
    return far_cel, far_kel

def kel_to_cel_far(temp_k):
    # Fahrenheit to Celsius
    kel_cel = temp_k - 273.15
    # Fahrenheit to kelvin
    kel_far = 9 / 5 * kel_cel + 32
    return kel_cel, kel_far
