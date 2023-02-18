def validate_gender(gender):
    return gender == "M" or gender == "F"

def validate_positive_integer(number):
    try:
        integer = int(number)
        
        return integer > 0
    except ValueError:
        return False

def validate_bit(bit):
    return bit == "0" or bit == "1"
