# file sanic/helpers.py:113-115
# lines [113, 115]
# branches []

import pytest
from sanic.helpers import is_entity_header

# Assuming _ENTITY_HEADERS is a set or list of headers considered to be entity headers.
# Since it's not provided in the question, I'll define a mock for the purpose of this test.
_ENTITY_HEADERS = {
    'allow', 'content-encoding', 'content-language', 'content-length',
    'content-location', 'content-md5', 'content-range', 'content-type',
    'expires', 'last-modified'
}

@pytest.fixture
def mock_entity_headers(mocker):
    mocker.patch('sanic.helpers._ENTITY_HEADERS', _ENTITY_HEADERS)

def test_is_entity_header_with_entity_header(mock_entity_headers):
    header = 'Content-Type'
    assert is_entity_header(header) is True

def test_is_entity_header_with_non_entity_header(mock_entity_headers):
    header = 'Host'
    assert is_entity_header(header) is False

def test_is_entity_header_with_mixed_case_header(mock_entity_headers):
    header = 'CoNtEnT-TyPe'
    assert is_entity_header(header) is True
