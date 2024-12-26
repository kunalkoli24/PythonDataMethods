# type hint module provide more advanced type hints 
# type such as list, union, tuple and dict 

# syntax: from typing import List, Tuple, Union, dict

from typing import List, Tuple, Union, Dict

# List of integers  
num : List[int] = [1,2,3,4,5]

# tuple of a string and an integer 

per : Tuple[str,int] = ("python",30)


# dict with string keys and integer values 

score : Dict[str,int] = {"python": 30 ,"java": 10}


# union type of Variable that can hold multiple values

un : Union[int,str] = "ID34"
un = 1234 # aslo valid 