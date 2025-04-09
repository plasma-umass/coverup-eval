# file: string_utils/validation.py:641-657
# asked: {"lines": [641, 656, 657], "branches": []}
# gained: {"lines": [641, 656, 657], "branches": []}

import pytest
from string_utils.validation import is_isbn
from string_utils.errors import InvalidInputError

def test_is_isbn_valid_13():
    assert is_isbn('9780312498580') == True

def test_is_isbn_valid_10():
    assert is_isbn('1506715214') == True

def test_is_isbn_invalid_length():
    assert is_isbn('123456789') == False

def test_is_isbn_invalid_characters():
    assert is_isbn('97803124985X0') == False

def test_is_isbn_with_hyphens():
    assert is_isbn('978-0-312-49858-0') == True

def test_is_isbn_without_normalize():
    assert is_isbn('978-0-312-49858-0', normalize=False) == False

def test_is_isbn_invalid_input_type():
    with pytest.raises(InvalidInputError):
        is_isbn(1234567890)
