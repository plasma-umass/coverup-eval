# file: flutes/structure.py:39-46
# asked: {"lines": [39, 46], "branches": []}
# gained: {"lines": [39, 46], "branches": []}

import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

def test_register_no_map_class():
    class CustomContainer:
        pass

    # Ensure the class is not already in the set
    assert CustomContainer not in _NO_MAP_TYPES

    # Register the class
    register_no_map_class(CustomContainer)

    # Verify the class is now in the set
    assert CustomContainer in _NO_MAP_TYPES

    # Clean up after the test
    _NO_MAP_TYPES.remove(CustomContainer)
    assert CustomContainer not in _NO_MAP_TYPES
