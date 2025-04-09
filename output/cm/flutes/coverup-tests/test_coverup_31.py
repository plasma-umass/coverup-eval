# file flutes/structure.py:74-96
# lines [74, 75, 82, 83, 84, 85, 86, 87, 88, 90, 91, 93, 94, 95, 96]
# branches ['82->83', '82->84', '84->85', '84->86', '86->87', '86->91', '87->88', '87->90', '91->93', '91->94', '94->95', '94->96']

import pytest
from flutes.structure import map_structure
from collections import namedtuple, OrderedDict

class NoMap:
    pass

def test_map_structure():
    # Test with a namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(x=1, y=2)
    fn = lambda x: x * 2 if not isinstance(x, NoMap) else x
    result = map_structure(fn, p)
    assert result == Point(x=2, y=4), "Failed to map function over namedtuple"

    # Test with an OrderedDict
    d = OrderedDict([('a', 1), ('b', 2)])
    result = map_structure(fn, d)
    assert isinstance(result, OrderedDict), "Result should be an OrderedDict"
    assert result == OrderedDict([('a', 2), ('b', 4)]), "Failed to map function over OrderedDict"

    # Test with a set
    s = {1, 2, 3}
    result = map_structure(fn, s)
    assert isinstance(result, set), "Result should be a set"
    assert result == {2, 4, 6}, "Failed to map function over set"

    # Test with a class that should not be mapped
    obj = NoMap()
    setattr(obj, '_no_map', True)
    result = map_structure(fn, obj)
    assert result == obj, "Function should not be applied to NoMap instances"

    # Clean up by removing the attribute
    delattr(obj, '_no_map')

@pytest.fixture(autouse=True)
def clean_up():
    # No cleanup needed for this test
    yield

# Run the test
def test_all():
    test_map_structure()
