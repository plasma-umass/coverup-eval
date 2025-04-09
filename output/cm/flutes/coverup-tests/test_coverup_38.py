# file flutes/structure.py:74-96
# lines [83]
# branches ['82->83']

import pytest
from flutes.structure import map_structure

class NoMapType:
    pass

_NO_MAP_TYPES = {NoMapType}
_NO_MAP_INSTANCE_ATTR = "_no_map"

def test_map_structure_no_map_type():
    # Setup: Create an instance of NoMapType
    obj = NoMapType()

    # Test: Apply map_structure with a function that returns a constant
    result = map_structure(lambda x: 42, obj)

    # Verify: The result should be the output of the function applied directly
    assert result == 42

    # Cleanup: Not needed as no external state was modified

def test_map_structure_no_map_instance_attr(mocker):
    # Setup: Create a mock object with the _NO_MAP_INSTANCE_ATTR
    obj = mocker.Mock()
    setattr(obj, _NO_MAP_INSTANCE_ATTR, True)

    # Test: Apply map_structure with a function that returns a constant
    result = map_structure(lambda x: 42, obj)

    # Verify: The result should be the output of the function applied directly
    assert result == 42

    # Cleanup: Not needed as no external state was modified
