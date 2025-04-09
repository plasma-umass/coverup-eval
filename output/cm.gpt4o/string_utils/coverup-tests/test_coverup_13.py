# file string_utils/manipulation.py:282-297
# lines [282, 294, 295, 297]
# branches ['294->295', '294->297']

import pytest
from string_utils.manipulation import reverse, InvalidInputError

def is_string(input_string):
    return isinstance(input_string, str)

def test_reverse_valid_string():
    assert reverse('hello') == 'olleh'
    assert reverse('world') == 'dlrow'
    assert reverse('') == ''

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError):
        reverse(123)
    with pytest.raises(InvalidInputError):
        reverse(None)
    with pytest.raises(InvalidInputError):
        reverse(['a', 'b', 'c'])

@pytest.fixture(autouse=True)
def mock_is_string(mocker):
    mocker.patch('string_utils.manipulation.is_string', side_effect=is_string)
