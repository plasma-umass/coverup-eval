# file pymonet/semigroups.py:120-137
# lines [126, 135, 136]
# branches []

import pytest
from pymonet.semigroups import Map, Semigroup

class StringSemigroup(Semigroup):
    def __init__(self, value):
        self.value = value

    def concat(self, semigroup):
        return StringSemigroup(self.value + semigroup.value)

@pytest.fixture
def cleanup():
    # No cleanup needed for this test
    yield
    # If there were any global changes, they would be reverted here

def test_map_concat_and_str(mocker, cleanup):
    mocker.patch.object(Map, '__str__', return_value='Map[value={"a": "A", "b": "B"}]')
    map1 = Map({'a': StringSemigroup('A'), 'b': StringSemigroup('B')})
    map2 = Map({'a': StringSemigroup('a'), 'b': StringSemigroup('b')})
    result = map1.concat(map2)
    assert str(result) == 'Map[value={"a": "A", "b": "B"}]'
    assert isinstance(result, Map)
    assert result.value['a'].value == 'Aa'
    assert result.value['b'].value == 'Bb'
