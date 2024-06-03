# file flutes/structure.py:16-32
# lines [16, 32]
# branches []

import pytest
from flutes.structure import reverse_map

def test_reverse_map():
    # Test with a simple dictionary
    d = {'a': 2, 'b': 0, 'c': 1}
    result = reverse_map(d)
    assert result == ['b', 'c', 'a']

    # Test with an empty dictionary
    d = {}
    result = reverse_map(d)
    assert result == []

    # Test with a larger dictionary
    d = {chr(97 + i): i for i in range(10)}
    result = reverse_map(d)
    assert result == [chr(97 + i) for i in range(10)]

    # Test with non-string keys
    d = {1: 2, 2: 0, 3: 1}
    result = reverse_map(d)
    assert result == [2, 3, 1]

    # Test with non-integer values (should raise an error)
    d = {'a': 2, 'b': '0', 'c': 1}
    with pytest.raises(TypeError):
        reverse_map(d)
