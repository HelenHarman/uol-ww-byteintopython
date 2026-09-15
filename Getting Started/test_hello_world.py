"""Byte into Python: Getting Started.
    This file is to test the content of hello_world.py
"""

# we import the entire content of the hello_world.py script into this test script. 
from hello_world import *


def test_simple_sum_function():
    """ Tests the sum_two_values function returns the correct values"""
        
    # Here we call our sum_two_values function that is in hello_world.py
    #  We pass that function the values 1 and 4,
    #  and we save the value the function call returns into "result".
    result = sum_two_values(1, 4) 
    
    # assert statements are used in unit tests to check a value
    #  Here we check if the content of "result" is equal to 5
    #  If it doesn't equal 5, the test fails. 
    assert result == 5
    
    # we could have written the above two lines as one line:
    # assert sum_two_values(1, 4) == 5   
    
    # Another check on the same function but with different values:
    assert sum_two_values(43, 22) == 65
    
    # you could add some further assert statements here:
    
    
def test_sum_all_function():
    """ Tests the sum_all function returns the correct values"""
    
    assert sum_all([2,3,4,5]) == 14
    
    assert sum_all([1,30,4]) == 35
    
    
    
    

    
