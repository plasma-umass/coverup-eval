# file: pysnooper/utils.py:62-64
# asked: {"lines": [64], "branches": []}
# gained: {"lines": [64], "branches": []}

import re
import pytest
from pysnooper.utils import normalize_repr

DEFAULT_REPR_RE = re.compile(' at 0x[a-f0-9A-F]{4,}')

def test_normalize_repr():
    # Test case where the memory address is present
    item_repr_with_address = "<object at 0x1234abcd>"
    expected_result = "<object>"
    assert normalize_repr(item_repr_with_address) == expected_result

    # Test case where the memory address is not present
    item_repr_without_address = "<object>"
    assert normalize_repr(item_repr_without_address) == item_repr_without_address

    # Test case with different format
    item_repr_with_different_format = "<object at 0xDEADBEEF>"
    expected_result_different_format = "<object>"
    assert normalize_repr(item_repr_with_different_format) == expected_result_different_format

    # Test case with no 'at' keyword
    item_repr_no_at = "<object 0x1234abcd>"
    assert normalize_repr(item_repr_no_at) == item_repr_no_at
