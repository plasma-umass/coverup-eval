# file: pymonet/semigroups.py:120-137
# asked: {"lines": [120, 121, 125, 126, 128, 135, 136], "branches": []}
# gained: {"lines": [120, 121, 125, 126, 128, 135, 136], "branches": []}

import pytest
from pymonet.semigroups import Map

def test_map_str():
    map_instance = Map({'a': 1, 'b': 2})
    assert str(map_instance) == 'Map[value={\'a\': 1, \'b\': 2}]'

def test_map_concat():
    class MockSemigroup:
        def __init__(self, value):
            self.value = value

        def concat(self, other):
            return MockSemigroup(self.value + other.value)

    map1 = Map({'a': MockSemigroup(1), 'b': MockSemigroup(2)})
    map2 = Map({'a': MockSemigroup(3), 'b': MockSemigroup(4)})

    result = map1.concat(map2)
    assert result.value['a'].value == 4
    assert result.value['b'].value == 6
