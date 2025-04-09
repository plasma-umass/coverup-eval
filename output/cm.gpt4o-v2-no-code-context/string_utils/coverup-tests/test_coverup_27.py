# file: string_utils/validation.py:368-390
# asked: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}
# gained: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}

import pytest
from string_utils.validation import is_uuid

def test_is_uuid_valid_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') is True

def test_is_uuid_invalid_uuid():
    assert is_uuid('invalid-uuid-string') is False

def test_is_uuid_valid_hex_with_allow_hex():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) is True

def test_is_uuid_invalid_hex_without_allow_hex():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=False) is False

def test_is_uuid_invalid_hex_with_allow_hex():
    assert is_uuid('invalidhexstring', allow_hex=True) is False

def test_is_uuid_empty_string():
    assert is_uuid('') is False

def test_is_uuid_none_input():
    assert is_uuid(None) is False

def test_is_uuid_integer_input():
    assert is_uuid(1234567890) is False

def test_is_uuid_valid_uuid_with_braces():
    assert is_uuid('{6f8aa2f9-686c-4ac3-8766-5712354a04cf}') is False
