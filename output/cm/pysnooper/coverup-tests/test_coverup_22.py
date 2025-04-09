# file pysnooper/utils.py:44-47
# lines [45, 46]
# branches []

import pytest
from pysnooper.utils import shitcode

def test_shitcode_with_non_ascii_characters():
    non_ascii_string = "Hello, 😊"
    expected_result = "Hello, ?"
    
    assert shitcode(non_ascii_string) == expected_result
