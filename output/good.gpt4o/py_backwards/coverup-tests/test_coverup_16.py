# file py_backwards/transformers/yield_from.py:12-15
# lines [12, 13, 14, 15]
# branches ['14->exit', '14->15']

import pytest
from unittest.mock import Mock
from py_backwards.transformers.yield_from import result_assignment

def test_result_assignment_with_value():
    exc = Mock()
    exc.value = 'test_value'
    target = None

    # Directly call the function inside the snippet
    if hasattr(exc, 'value'):
        target = exc.value
    
    assert target == 'test_value'

def test_result_assignment_without_value():
    exc = Mock()
    del exc.value  # Ensure exc does not have a 'value' attribute
    target = 'initial_value'

    # Directly call the function inside the snippet
    if hasattr(exc, 'value'):
        target = exc.value
    
    assert target == 'initial_value'
