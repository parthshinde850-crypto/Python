from typing import list, Tuple, Dict, Union

# List of integers
numbers : list[int] = [ 1, 2, 3, 4, 5]

# Tuple of a string and an integer
persons : Tuple[str, int] = ("Parth", 100)

# Dictionary with string Keys and integer value 
scores : Dict[str, int] = {"parth" : 100 , "Bob" : 98}

# Union type for variables that can hold multiple types
identifiers : Union[int, str] = "IF123"
identifiers = "1234"  #also valid