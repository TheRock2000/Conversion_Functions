def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    
    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """

    if not num_string or num_string[0] == ".":
        return False, 0
    if "." not in num_string:
        return True, int(num_string)
    if "." in num_string:
        left = num_string.split(".",1)[0]
        if left.isdigit():
            return True, int(left)
        return False,0
    if num_string.isdigit():
        return True, int(num_string)
    
    return False, 0

def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    
    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """
    if not num_string or num_string[0] == ".":
        return False, 0,0
        
    if "." not in num_string:
        return True, 0, 1
        
    if "." in num_string:
        right = num_string.split(".",1)[1]
        return True, int(right), 10**len(right)
