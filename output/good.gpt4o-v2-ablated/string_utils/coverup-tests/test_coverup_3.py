# file: string_utils/manipulation.py:282-297
# asked: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}

import pytest
from string_utils.manipulation import reverse, InvalidInputError

def is_string(input_string):
    return isinstance(input_string, str)

def test_reverse_valid_string():
    assert reverse('hello') == 'olleh'
    assert reverse('world') == 'dlrow'
    assert reverse('') == ''
    assert reverse('a') == 'a'

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(123)
    with pytest.raises(InvalidInputError):
        reverse(None)
    with pytest.raises(InvalidInputError):
        reverse([1, 2, 3])

def test_reverse_edge_cases():
    assert reverse(' ') == ' '
    assert reverse('  ') == '  '
    assert reverse('!@#') == '#@!'
