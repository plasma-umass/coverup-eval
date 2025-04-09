# file: string_utils/validation.py:368-390
# asked: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}
# gained: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}

import pytest
from string_utils.validation import is_uuid

def test_is_uuid_valid_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

def test_is_uuid_invalid_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf') == False

def test_is_uuid_valid_hex_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True

def test_is_uuid_invalid_string():
    assert is_uuid('invalid-uuid-string') == False

def test_is_uuid_empty_string():
    assert is_uuid('') == False

def test_is_uuid_none_input():
    assert is_uuid(None) == False

def test_is_uuid_integer_input():
    assert is_uuid(123456) == False

def test_is_uuid_valid_uuid_with_braces():
    assert is_uuid('{6f8aa2f9-686c-4ac3-8766-5712354a04cf}') == False

def test_is_uuid_valid_hex_uuid_with_braces():
    assert is_uuid('{6f8aa2f9686c4ac387665712354a04cf}', allow_hex=True) == False
