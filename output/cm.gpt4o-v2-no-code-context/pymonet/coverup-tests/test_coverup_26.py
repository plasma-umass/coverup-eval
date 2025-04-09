# file: pymonet/monad_try.py:92-105
# asked: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from pymonet.monad_try import Try

def test_try_filter_success_true():
    # Create a successful Try instance
    try_instance = Try(10, True)
    
    # Define a filter function that returns True
    def filter_func(value):
        return value > 5
    
    # Apply the filter method
    result = try_instance.filter(filter_func)
    
    # Assert that the result is a successful Try instance with the same value
    assert result.is_success
    assert result.value == 10

def test_try_filter_success_false():
    # Create a successful Try instance
    try_instance = Try(10, True)
    
    # Define a filter function that returns False
    def filter_func(value):
        return value < 5
    
    # Apply the filter method
    result = try_instance.filter(filter_func)
    
    # Assert that the result is a failed Try instance with the same value
    assert not result.is_success
    assert result.value == 10

def test_try_filter_failure():
    # Create a failed Try instance
    try_instance = Try(10, False)
    
    # Define a filter function (it should not matter what it returns)
    def filter_func(value):
        return value > 5
    
    # Apply the filter method
    result = try_instance.filter(filter_func)
    
    # Assert that the result is a failed Try instance with the same value
    assert not result.is_success
    assert result.value == 10
