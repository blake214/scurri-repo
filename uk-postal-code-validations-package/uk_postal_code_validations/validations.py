import re
from .formatting import formatPostalCode

def validationArea(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the area code.
    
    Parameters:
        input (str): A sub-string of the area portion of the postal code
    
    Returns:
        Bool: Returns true if a valid area code, false otherwise
    """
    regex = r"^[ABCDEFGHIJKLMNOPRSTUWYZ][ABCDEFGHKLMNOPQRSTUVWXY]?$"
    return bool(re.fullmatch(regex, input.replace(" ", "").upper()))

def validationDistrict(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the district code.
    
    Parameters:
        input (str): A sub-string of the district portion of the postal code
    
    Returns:
        Bool: Returns true if a valid district code, false otherwise
    """
    regex = r"^[0-9][0-9ABCDEFGHJKPSTUW]?$"
    return bool(re.fullmatch(regex, input.replace(" ", "").upper()))

def validationSector(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the sector code.
    
    Parameters:
        input (str): A sub-string of the sector portion of the postal code
    
    Returns:
        Bool: Returns true if a valid sector code, false otherwise
    """
    regex = r"^[0-9]$"
    return bool(re.fullmatch(regex, input.replace(" ", "").upper()))

def validationUnit(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the unit code.
    
    Parameters:
        input (str): A sub-string of the unit portion of the postal code
    
    Returns:
        Bool: Returns true if a valid unit code, false otherwise
    """
    regex = r"^[ABDEFGHJLNPQRSTUVWXY]{2}$"
    return bool(re.fullmatch(regex, input.replace(" ", "").upper()))

def validationOutwardCode(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the outward code.
    
    Parameters:
        input (str): A sub-string of the outward portion of the postal code
    
    Returns:
        Bool: Returns true if a valid outward code, false otherwise
    """
    # Lets loop through the input and slice at certain intervals for validation, instead of creating a new nasty regex
    for i in range(1, len(input)):
        # Init
        dingle_digit_districts = ["BL", "BR", "FY", "HA", "HD", "HG", "HR", "HS", "HX", "JE", "LD", "SM", "SR", "WC", "WN", "ZE"]
        double_digit_districts = ["AB", "LL", "SO"]
        zeros_digit_areas = ["BL", "BS", "CM", "CR", "FY", "HA", "PR", "SL", "SS"]

        # Convert to upper, and remove spaces
        input = input.replace(" ", "").upper()

        # Declarations
        area = input[:i]
        district = input[i:]

        # Validate
        if validationArea(area) and validationDistrict(district):
            # Lets check for the edge cases (i only did the ones that were clear from the documentation, there one or two that were a bit unclear)
            # Single digit districts
            if area in dingle_digit_districts and len(district) != 1:
                return False
            # Double digit districs
            if area in double_digit_districts and len(district) != 2:
                return False
            # Zeros areas
            if district == "0" and area not in zeros_digit_areas:
                return False
            
            return True
        
    return False

def validationInwardCode(input:str) -> bool:
    """
    Validates a UK postal code sub-string, specific to the inward code.
    
    Parameters:
        input (str): A sub-string of the inward portion of the postal code
    
    Returns:
        Bool: Returns true if a valid inward code, false otherwise
    """    
    # Convert to upper, and remove spaces
    input = input.replace(" ", "").upper()

    # Lets loop through the input and slice at certain intervals for validation, instead of creating a new nasty regex
    for i in range(1, len(input)):
        # Declarations
        sector = input[:i]
        unit = input[i:]

        # Validate
        if validationSector(sector) and validationUnit(unit):
            return True
        
    return False

def validationUKPostalCode(input:str) -> bool:
    """
    Validates a UK postal code string.
    
    Parameters:
        input (str): A string of a UK postal code
    
    Returns:
        Bool: Returns true if a valid, false otherwise
    """
    # Clean the input
    cleaned_input = formatPostalCode(input)

    # Assuming there is a " ", else will result in an invalidation
    sub_strings = cleaned_input.split(" ")

    # Validate before we proceed
    if len(sub_strings) != 2:
        return False
    
    # Deconstruct our sections
    outwards, inwards = sub_strings

    # Validate and return
    return validationOutwardCode(outwards) and validationInwardCode(inwards)
    