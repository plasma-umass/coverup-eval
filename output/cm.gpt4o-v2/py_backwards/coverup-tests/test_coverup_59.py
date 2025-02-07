# file: py_backwards/utils/helpers.py:32-36
# asked: {"lines": [34, 35, 36], "branches": []}
# gained: {"lines": [34, 35, 36], "branches": []}

import pytest
from py_backwards.utils.helpers import get_source
from textwrap import dedent

def test_get_source():
    def sample_function():
        x = 1
        return x

    expected_source = dedent('''\
    def sample_function():
        x = 1
        return x
    ''')
    
    assert get_source(sample_function) == expected_source
