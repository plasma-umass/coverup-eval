# file pymonet/semigroups.py:120-137
# lines [126]
# branches []

import pytest
from pymonet.semigroups import Map

def test_map_str_representation():
    # Create an instance of Map with a specific value
    map_instance = Map({'a': 1, 'b': 2})

    # Call the __str__ method and assert the correct string representation
    assert str(map_instance) == 'Map[value={\'a\': 1, \'b\': 2}]'
