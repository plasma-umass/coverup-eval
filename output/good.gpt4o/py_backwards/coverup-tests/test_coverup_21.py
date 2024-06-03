# file py_backwards/utils/helpers.py:32-36
# lines [32, 34, 35, 36]
# branches []

import pytest
from py_backwards.utils.helpers import get_source
from inspect import getsource
import re

def test_get_source(mocker):
    def sample_function():
        return "Hello, World!"

    mocker.patch('py_backwards.utils.helpers.getsource', return_value="    def sample_function():\n        return 'Hello, World!'")
    
    expected_source = "def sample_function():\n    return 'Hello, World!'"
    actual_source = get_source(sample_function)
    
    assert actual_source == expected_source
