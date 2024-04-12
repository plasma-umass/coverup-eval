# file flutes/structure.py:99-127
# lines [114, 116, 121]
# branches ['113->114', '115->116', '118->121']

import pytest
from flutes.structure import map_structure_zip

_NO_MAP_TYPES = (int, float, str, bytes)
_NO_MAP_INSTANCE_ATTR = "_no_map"

class NoMapClass:
    _no_map = True

def test_map_structure_zip():
    # Test for line 114
    def fn(*args):
        return args[0]  # Return the first argument to avoid TypeError

    no_map_instance = NoMapClass()
    result = map_structure_zip(fn, [no_map_instance, no_map_instance])
    assert result == no_map_instance

    # Test for line 116
    def sum_fn(*args):
        return sum(args)

    result = map_structure_zip(sum_fn, [[1, 2], [3, 4]])
    assert result == [4, 6]

    # Test for line 121
    result = map_structure_zip(sum_fn, [(1, 2), (3, 4)])
    assert result == (4, 6)

@pytest.fixture
def mock_hasattr(mocker):
    mocker.patch('flutes.structure.hasattr', return_value=True)

def test_map_structure_zip_with_mock_hasattr(mock_hasattr):
    # Test for line 114 with mock
    def fn(*args):
        return sum(args)

    result = map_structure_zip(fn, [1, 2])
    assert result == 3
