# file: pysnooper/utils.py:62-64
# asked: {"lines": [62, 64], "branches": []}
# gained: {"lines": [62, 64], "branches": []}

import pytest
import re
from pysnooper.utils import normalize_repr

def test_normalize_repr():
    # Test case where the memory address is present in the string
    item_repr_with_address = "<object at 0x1234abcd>"
    expected_result = "<object>"
    assert normalize_repr(item_repr_with_address) == expected_result

    # Test case where there is no memory address in the string
    item_repr_without_address = "<object>"
    expected_result = "<object>"
    assert normalize_repr(item_repr_without_address) == expected_result

    # Test case where the memory address is in a different format
    item_repr_with_different_address = "<object at 0xDEADBEEF>"
    expected_result = "<object>"
    assert normalize_repr(item_repr_with_different_address) == expected_result

    # Test case where the string is empty
    item_repr_empty = ""
    expected_result = ""
    assert normalize_repr(item_repr_empty) == expected_result

    # Test case where the string does not match the pattern at all
    item_repr_no_match = "random string"
    expected_result = "random string"
    assert normalize_repr(item_repr_no_match) == expected_result
