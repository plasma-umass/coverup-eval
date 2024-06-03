# file sanic/cookies.py:99-106
# lines [99, 100, 101, 102, 103, 104, 105, 106]
# branches ['100->101', '100->102', '102->103', '102->104']

import pytest
from sanic.cookies import Cookie

def _is_legal_key(key):
    # Mock implementation of _is_legal_key for testing purposes
    return all(c.isalnum() or c in '-._' for c in key)

@pytest.fixture
def mock_is_legal_key(mocker):
    return mocker.patch('sanic.cookies._is_legal_key', side_effect=_is_legal_key)

def test_cookie_reserved_word(mock_is_legal_key):
    reserved_keys = ['reserved1', 'reserved2']
    Cookie._keys = reserved_keys
    with pytest.raises(KeyError, match="Cookie name is a reserved word"):
        Cookie('reserved1', 'value')

def test_cookie_illegal_key(mock_is_legal_key):
    Cookie._keys = []
    with pytest.raises(KeyError, match="Cookie key contains illegal characters"):
        Cookie('illegal key!', 'value')

def test_cookie_creation(mock_is_legal_key):
    Cookie._keys = []
    cookie = Cookie('valid_key', 'value')
    assert cookie.key == 'valid_key'
    assert cookie.value == 'value'
    assert isinstance(cookie, dict)
