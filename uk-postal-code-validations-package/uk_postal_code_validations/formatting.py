import re

def formatPostalCode(input:str) -> str:
    """
    Formats a UK postal code, that might be supplied differently. Doesnt perform validations.

    - Removes trailing spaces
    - Removed double white spaces
    - Converts to uppercase
    
    Parameters:
        input (str): A string of the postal code
    
    Returns:
        str: Returns a formatted postal code
    """
    return re.sub(r'\s+', " ", input.strip()).upper()