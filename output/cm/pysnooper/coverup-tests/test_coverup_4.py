# file pysnooper/utils.py:62-64
# lines [62, 64]
# branches []

import re
import pytest
from pysnooper.utils import normalize_repr

DEFAULT_REPR_RE = re.compile(r' at 0x[0-9A-Fa-f]+')

def test_normalize_repr():
    # Test with a string that contains a memory address
    item_with_memory_address = "<some_object at 0x16D04C70>"
    normalized = normalize_repr(item_with_memory_address)
    assert normalized == "<some_object>"

    # Test with a string that does not contain a memory address
    item_without_memory_address = "<some_other_object>"
    normalized = normalize_repr(item_without_memory_address)
    assert normalized == "<some_other_object>"

    # Test with a string that contains multiple memory addresses
    item_with_multiple_memory_addresses = "<obj1 at 0x16D04C70> <obj2 at 0x16D04C71>"
    normalized = normalize_repr(item_with_multiple_memory_addresses)
    assert normalized == "<obj1> <obj2>"

    # Test with a string that contains no memory address but has 'at' in it
    item_with_at_in_text = "<object at the rate of>"
    normalized = normalize_repr(item_with_at_in_text)
    assert normalized == "<object at the rate of>"

    # Test with an empty string
    empty_string = ""
    normalized = normalize_repr(empty_string)
    assert normalized == ""
