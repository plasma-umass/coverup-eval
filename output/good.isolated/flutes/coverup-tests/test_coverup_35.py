# file flutes/structure.py:74-96
# lines [83, 85, 90]
# branches ['82->83', '84->85', '87->90']

import pytest
from flutes.structure import map_structure

class NoMapType:
    pass

_NO_MAP_TYPES = {NoMapType}
_NO_MAP_INSTANCE_ATTR = "_no_map"

def test_map_structure_no_map_types_and_attributes(mocker):
    # Mock the function to be used in map_structure
    mock_fn = mocker.Mock(return_value="mapped")

    # Test for _NO_MAP_TYPES
    no_map_type_instance = NoMapType()
    result = map_structure(mock_fn, no_map_type_instance)
    mock_fn.assert_called_once_with(no_map_type_instance)
    assert result == "mapped"

    # Reset mock for next test
    mock_fn.reset_mock()

    # Test for _NO_MAP_INSTANCE_ATTR
    class WithNoMapAttr:
        _no_map = True

    with_no_map_attr_instance = WithNoMapAttr()
    result = map_structure(mock_fn, with_no_map_attr_instance)
    mock_fn.assert_called_once_with(with_no_map_attr_instance)
    assert result == "mapped"

    # Reset mock for next test
    mock_fn.reset_mock()

    # Test for list
    list_instance = [1, 2, 3]
    result = map_structure(mock_fn, list_instance)
    assert mock_fn.call_count == 3
    assert result == ["mapped", "mapped", "mapped"]

    # Reset mock for next test
    mock_fn.reset_mock()

    # Test for tuple
    tuple_instance = (1, 2, 3)
    result = map_structure(mock_fn, tuple_instance)
    assert mock_fn.call_count == 3
    assert result == ("mapped", "mapped", "mapped")
