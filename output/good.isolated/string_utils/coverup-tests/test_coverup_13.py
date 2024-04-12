# file string_utils/validation.py:368-390
# lines [368, 385, 387, 388, 390]
# branches ['387->388', '387->390']

import pytest
from string_utils.validation import is_uuid
from uuid import UUID

@pytest.fixture
def valid_uuid():
    return str(UUID('6f8aa2f9-686c-4ac3-8766-5712354a04cf'))

@pytest.fixture
def valid_uuid_hex():
    return '6f8aa2f9686c4ac387665712354a04cf'

@pytest.fixture
def invalid_uuid():
    return 'invalid-uuid-string'

def test_is_uuid_with_valid_uuid(valid_uuid):
    assert is_uuid(valid_uuid) == True

def test_is_uuid_with_invalid_uuid(invalid_uuid):
    assert is_uuid(invalid_uuid) == False

def test_is_uuid_with_valid_uuid_hex(valid_uuid_hex):
    assert is_uuid(valid_uuid_hex, allow_hex=True) == True

def test_is_uuid_with_valid_uuid_as_hex_without_allow_hex(valid_uuid_hex):
    assert is_uuid(valid_uuid_hex) == False

def test_is_uuid_with_invalid_uuid_hex(invalid_uuid):
    assert is_uuid(invalid_uuid, allow_hex=True) == False
