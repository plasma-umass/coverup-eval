# file flutes/structure.py:99-127
# lines [99, 100, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 124, 125, 126, 127]
# branches ['113->114', '113->115', '115->116', '115->117', '117->118', '117->122', '118->119', '118->121', '122->124', '122->125', '125->126', '125->127']

import pytest
from collections import namedtuple
from flutes.structure import map_structure_zip

def test_map_structure_zip():
    # Test with simple list
    result = map_structure_zip(lambda x, y: x + y, [[1, 2, 3], [4, 5, 6]])
    assert result == [5, 7, 9]

    # Test with nested list
    result = map_structure_zip(lambda x, y: x + y, [[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    assert result == [[6, 8], [10, 12]]

    # Test with tuple
    result = map_structure_zip(lambda x, y: x + y, [(1, 2, 3), (4, 5, 6)])
    assert result == (5, 7, 9)

    # Test with namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    result = map_structure_zip(lambda x, y: x + y, [Point(1, 2), Point(3, 4)])
    assert result == Point(4, 6)

    # Test with dict
    result = map_structure_zip(lambda x, y: x + y, [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}])
    assert result == {'a': 4, 'b': 6}

    # Test with set (should raise ValueError)
    with pytest.raises(ValueError, match="Structures cannot contain `set` because it's unordered"):
        map_structure_zip(lambda x, y: x + y, [set([1, 2]), set([3, 4])])

    # Test with non-iterable
    result = map_structure_zip(lambda x, y: x + y, [1, 2])
    assert result == 3
