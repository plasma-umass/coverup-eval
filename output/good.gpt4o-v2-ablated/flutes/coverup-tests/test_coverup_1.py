# file: flutes/structure.py:39-46
# asked: {"lines": [39, 46], "branches": []}
# gained: {"lines": [39, 46], "branches": []}

import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

def test_register_no_map_class():
    class CustomContainer:
        pass

    # Ensure the class is not in _NO_MAP_TYPES before registration
    assert CustomContainer not in _NO_MAP_TYPES

    # Register the class
    register_no_map_class(CustomContainer)

    # Ensure the class is now in _NO_MAP_TYPES
    assert CustomContainer in _NO_MAP_TYPES

    # Clean up by removing the class from _NO_MAP_TYPES
    _NO_MAP_TYPES.remove(CustomContainer)
    assert CustomContainer not in _NO_MAP_TYPES
