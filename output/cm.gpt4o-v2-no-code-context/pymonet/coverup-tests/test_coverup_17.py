# file: pymonet/monad_try.py:40-51
# asked: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}
# gained: {"lines": [40, 49, 50, 51], "branches": [[49, 50], [49, 51]]}

import pytest
from pymonet.monad_try import Try

def test_try_map_success():
    # Create a successful Try instance
    success_try = Try(10, True)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Apply the map function
    mapped_try = success_try.map(mapper)
    
    # Assert the mapped value is correct
    assert mapped_try.is_success
    assert mapped_try.value == 20

def test_try_map_failure():
    # Create a failed Try instance
    failure_try = Try(10, False)
    
    # Define a mapper function
    def mapper(x):
        return x * 2
    
    # Apply the map function
    mapped_try = failure_try.map(mapper)
    
    # Assert the value remains the same and is still a failure
    assert not mapped_try.is_success
    assert mapped_try.value == 10
