# file flutes/structure.py:39-46
# lines [39, 46]
# branches []

import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

def test_register_no_map_class():
    class CustomContainer:
        pass

    # Ensure the type is not in _NO_MAP_TYPES before registration
    assert CustomContainer not in _NO_MAP_TYPES

    # Register the custom container type
    register_no_map_class(CustomContainer)

    # Verify that the type is now in _NO_MAP_TYPES
    assert CustomContainer in _NO_MAP_TYPES

    # Clean up by removing the type from _NO_MAP_TYPES
    _NO_MAP_TYPES.remove(CustomContainer)

    # Verify that the type has been removed
    assert CustomContainer not in _NO_MAP_TYPES
