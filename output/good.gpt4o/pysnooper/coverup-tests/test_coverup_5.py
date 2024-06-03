# file pysnooper/utils.py:50-56
# lines [50, 51, 52, 53, 54, 55, 56]
# branches ['51->52', '51->56', '52->53', '52->54', '54->51', '54->55']

import pytest
from pysnooper.utils import get_repr_function

def test_get_repr_function():
    # Test case where custom_repr has a type condition
    custom_repr = [(int, lambda x: f"int: {x}")]
    assert get_repr_function(5, custom_repr)(5) == "int: 5"
    
    # Test case where custom_repr has a lambda condition
    custom_repr = [(lambda x: x == 5, lambda x: f"five: {x}")]
    assert get_repr_function(5, custom_repr)(5) == "five: 5"
    
    # Test case where no condition matches
    custom_repr = [(lambda x: x == 10, lambda x: f"ten: {x}")]
    assert get_repr_function(5, custom_repr)(5) == repr(5)
    
    # Test case where custom_repr is empty
    custom_repr = []
    assert get_repr_function(5, custom_repr)(5) == repr(5)
