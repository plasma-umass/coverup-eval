# file flutes/structure.py:39-46
# lines [39, 46]
# branches []

import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

def test_register_no_map_class():
    class CustomContainer:
        pass

    assert CustomContainer not in _NO_MAP_TYPES
    register_no_map_class(CustomContainer)
    assert CustomContainer in _NO_MAP_TYPES
    _NO_MAP_TYPES.remove(CustomContainer)  # Clean up after the test
