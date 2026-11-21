"""
This function finds the length of the longest substring without repeating characters.


"""

def long_window(str : str) -> int:
    
    max_length = 0
    left = 0

    # use this dict to keep track of the count as the window is widen
    seen: dict[str,int] = {}
    # iterate through the string with the right pointer
    for right, char in enumerate(str):