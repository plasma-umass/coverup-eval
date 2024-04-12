# file dataclasses_json/core.py:234-238
# lines [234, 235, 236, 237, 238]
# branches []

import pytest
from dataclasses_json.core import _is_supported_generic
from enum import Enum
from typing import Union, Optional, List

# Define a mock Enum for testing
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Define a test function to cover the missing branches
def test_is_supported_generic():
    # Test with a non-str collection type
    assert _is_supported_generic(List[int])

    # Test with an optional type
    assert _is_supported_generic(Optional[int])

    # Test with a union type
    assert _is_supported_generic(Union[int, str])

    # Test with an enum type
    assert _is_supported_generic(Color)

    # Test with a type that is not supported
    assert not _is_supported_generic(str)
