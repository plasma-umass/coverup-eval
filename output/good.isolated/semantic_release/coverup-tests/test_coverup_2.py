# file semantic_release/helpers.py:9-13
# lines [9, 10, 11, 13]
# branches ['10->11', '10->13']

import pytest
from semantic_release.helpers import format_arg

def test_format_arg_with_string():
    assert format_arg(" test ") == "'test'"

def test_format_arg_with_non_string():
    assert format_arg(123) == "123"
    assert format_arg(12.3) == "12.3"
    assert format_arg(True) == "True"
    assert format_arg(None) == "None"
