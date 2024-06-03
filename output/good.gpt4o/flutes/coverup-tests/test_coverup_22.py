# file flutes/structure.py:99-127
# lines [114]
# branches ['113->114']

import pytest
from flutes.structure import map_structure_zip

class NoMapType:
    pass

def test_map_structure_zip_no_map_instance_attr(mocker):
    obj1 = NoMapType()
    obj2 = NoMapType()
    objs = [obj1, obj2]

    def dummy_fn(*args):
        return "mapped"

    # Add the attribute to trigger the condition
    setattr(obj1, '_no_map_instance_attr', True)

    result = map_structure_zip(dummy_fn, objs)
    assert result == "mapped"

    # Clean up
    delattr(obj1, '_no_map_instance_attr')

def test_map_structure_zip_no_map_type_class(mocker):
    class NoMapTypeClass:
        pass

    obj1 = NoMapTypeClass()
    obj2 = NoMapTypeClass()
    objs = [obj1, obj2]

    def dummy_fn(*args):
        return "mapped"

    # Mock _NO_MAP_TYPES to include NoMapTypeClass
    mocker.patch('flutes.structure._NO_MAP_TYPES', {NoMapTypeClass})

    result = map_structure_zip(dummy_fn, objs)
    assert result == "mapped"
