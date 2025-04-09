# file: string_utils/validation.py:368-390
# asked: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}
# gained: {"lines": [368, 385, 387, 388, 390], "branches": [[387, 388], [387, 390]]}

import pytest
from string_utils.validation import is_uuid

def test_is_uuid_valid_uuid():
    assert is_uuid('6f8aa2f9-686c-4ac3-8766-5712354a04cf') == True

def test_is_uuid_invalid_uuid():
    assert is_uuid('invalid-uuid-string') == False

def test_is_uuid_valid_hex_uuid():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=True) == True

def test_is_uuid_invalid_hex_uuid():
    assert is_uuid('invalidhexstring', allow_hex=True) == False

def test_is_uuid_valid_uuid_with_allow_hex_false():
    assert is_uuid('6f8aa2f9686c4ac387665712354a04cf', allow_hex=False) == False

def test_is_uuid_non_string_input():
    assert is_uuid(123456) == False
    assert is_uuid(None) == False
    assert is_uuid(['6f8aa2f9-686c-4ac3-8766-5712354a04cf']) == False

@pytest.fixture(autouse=True)
def setup_and_teardown(monkeypatch):
    # Setup: Mock the UUID_HEX_OK_RE and UUID_RE regex patterns
    import re
    monkeypatch.setattr('string_utils.validation.UUID_HEX_OK_RE', re.compile(r'^[0-9a-fA-F]{32}$'))
    monkeypatch.setattr('string_utils.validation.UUID_RE', re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'))
    yield
    # Teardown: No specific teardown steps needed
