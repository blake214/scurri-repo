def numbers(array:list) -> str | int:
    """
    Process an array of numbers and print specific outputs based on certain conditions:
    
    - Prints "ThreeFive" if a number is modulo 3 and 5
    - Prints "Three" if a number is modulo 3
    - Prints "Five" if a number is modulo 5
    - Prints the number itself if no conditions met
    
    Parameters:
        array (list): A list of integers
    
    Returns:
        None: This funciton doesnt return anything, prints only
    """
    for number in array:
        if number % 3 == 0 and number % 5 == 0:
            print("ThreeFive")
        elif number % 3 == 0:
            print("Three")
        elif number % 5 == 0:
            print("Five")
        else:
            print(number)

numbers(list(range(1,100)))