# file string_utils/generation.py:21-38
# lines [21, 33, 35, 36, 38]
# branches ['35->36', '35->38']

import pytest
from string_utils.generation import uuid
from unittest.mock import patch
from uuid import UUID

@pytest.fixture
def mock_uuid4():
    with patch('string_utils.generation.uuid4') as mock:
        mock.return_value = UUID('12345678123456781234567812345678')
        yield mock

def test_uuid_default(mock_uuid4):
    result = uuid()
    assert result == '12345678-1234-5678-1234-567812345678'
    mock_uuid4.assert_called_once()

def test_uuid_as_hex(mock_uuid4):
    result = uuid(as_hex=True)
    assert result == '12345678123456781234567812345678'
    mock_uuid4.assert_called_once()
