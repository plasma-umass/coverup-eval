# file pysnooper/utils.py:62-64
# lines [62, 64]
# branches []

import pytest
import re
from pysnooper.utils import normalize_repr

DEFAULT_REPR_RE = re.compile(r'\b0x[0-9a-fA-F]+\b')

def test_normalize_repr():
    # Test case where the memory address is present
    item_repr_with_address = "<object at 0x7f8b2c3d4e50>"
    normalized_repr = normalize_repr(item_repr_with_address)
    assert normalized_repr == "<object at >" or normalized_repr == "<object>"

    # Test case where there is no memory address
    item_repr_without_address = "<object at some_location>"
    normalized_repr = normalize_repr(item_repr_without_address)
    assert normalized_repr == item_repr_without_address

    # Test case with multiple memory addresses
    item_repr_multiple_addresses = "<object at 0x7f8b2c3d4e50> and <object at 0x7f8b2c3d4e51>"
    normalized_repr = normalize_repr(item_repr_multiple_addresses)
    assert normalized_repr == "<object at > and <object at >" or normalized_repr == "<object> and <object>"

    # Test case with no 'at' keyword
    item_repr_no_at = "<object 0x7f8b2c3d4e50>"
    normalized_repr = normalize_repr(item_repr_no_at)
    assert normalized_repr == "<object 0x7f8b2c3d4e50>"

    # Test case with empty string
    item_repr_empty = ""
    normalized_repr = normalize_repr(item_repr_empty)
    assert normalized_repr == ""

    # Test case with None
    item_repr_none = None
    with pytest.raises(TypeError):
        normalize_repr(item_repr_none)
