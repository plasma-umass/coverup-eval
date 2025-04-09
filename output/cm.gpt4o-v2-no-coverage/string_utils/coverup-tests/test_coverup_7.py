# file: string_utils/manipulation.py:282-297
# asked: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}
# gained: {"lines": [282, 294, 295, 297], "branches": [[294, 295], [294, 297]]}

import pytest
from string_utils.manipulation import reverse
from string_utils.errors import InvalidInputError

def test_reverse_valid_string():
    assert reverse("hello") == "olleh"
    assert reverse("world") == "dlrow"
    assert reverse("") == ""

def test_reverse_invalid_input():
    with pytest.raises(InvalidInputError) as exc_info:
        reverse(123)
    assert str(exc_info.value) == 'Expected "str", received "int"'

    with pytest.raises(InvalidInputError) as exc_info:
        reverse(None)
    assert str(exc_info.value) == 'Expected "str", received "NoneType"'
