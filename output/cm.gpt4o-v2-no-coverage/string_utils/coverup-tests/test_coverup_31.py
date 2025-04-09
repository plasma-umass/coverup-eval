# file: string_utils/manipulation.py:246-248
# asked: {"lines": [246, 247, 248], "branches": []}
# gained: {"lines": [246, 247, 248], "branches": []}

import pytest
from uuid import uuid4
from string_utils.manipulation import __StringFormatter

def test_placeholder_key(monkeypatch):
    def mock_uuid4():
        class MockUUID:
            hex = '1234567890abcdef'
        return MockUUID()
    
    monkeypatch.setattr('string_utils.manipulation.uuid4', mock_uuid4)
    
    placeholder = __StringFormatter._StringFormatter__placeholder_key()
    assert placeholder == '$1234567890abcdef$'
