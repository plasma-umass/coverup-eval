# file: py_backwards/utils/helpers.py:32-36
# asked: {"lines": [32, 34, 35, 36], "branches": []}
# gained: {"lines": [32, 34, 35, 36], "branches": []}

import pytest
from inspect import getsource
import re
from typing import Any, Callable
from py_backwards.utils.helpers import get_source

def test_get_source():
    def sample_function():
        return "sample"

    expected_source = "def sample_function():\n    return \"sample\"\n"
    assert get_source(sample_function) == expected_source

    def another_function(x):
        if x > 0:
            return x
        else:
            return -x

    expected_source = "def another_function(x):\n    if x > 0:\n        return x\n    else:\n        return -x\n"
    assert get_source(another_function) == expected_source

    def empty_function():
        pass

    expected_source = "def empty_function():\n    pass\n"
    assert get_source(empty_function) == expected_source

    with pytest.raises(TypeError):
        get_source(123)  # Passing an invalid type to getsource should raise a TypeError
