# file: pysnooper/utils.py:62-64
# asked: {"lines": [62, 64], "branches": []}
# gained: {"lines": [62, 64], "branches": []}

import re
import pytest
from pysnooper.utils import normalize_repr

DEFAULT_REPR_RE = re.compile(' at 0x[a-f0-9A-F]{4,}')

def test_normalize_repr():
    # Test case where the memory address is present
    input_repr = "<object at 0x1234ABCD>"
    expected_output = "<object>"
    assert normalize_repr(input_repr) == expected_output

    # Test case where the memory address is not present
    input_repr = "<object>"
    expected_output = "<object>"
    assert normalize_repr(input_repr) == expected_output

    # Test case with different memory address format
    input_repr = "<object at 0xDEADBEEF>"
    expected_output = "<object>"
    assert normalize_repr(input_repr) == expected_output

    # Test case with no 'at' keyword
    input_repr = "<object 0xDEADBEEF>"
    expected_output = "<object 0xDEADBEEF>"
    assert normalize_repr(input_repr) == expected_output
