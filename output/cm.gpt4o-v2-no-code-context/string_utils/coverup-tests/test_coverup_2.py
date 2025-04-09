# file: string_utils/manipulation.py:282-297
# asked: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}

import pytest
from string_utils.manipulation import reverse, InvalidInputError

def test_reverse_valid_string():
    assert reverse('hello') == 'olleh'
    assert reverse('world') == 'dlrow'
    assert reverse('') == ''

def test_reverse_invalid_input(monkeypatch):
    def mock_is_string(input_string):
        return False

    monkeypatch.setattr('string_utils.manipulation.is_string', mock_is_string)
    
    with pytest.raises(InvalidInputError):
        reverse('hello')
