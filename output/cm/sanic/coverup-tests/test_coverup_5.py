# file sanic/cookies.py:99-106
# lines [99, 100, 101, 102, 103, 104, 105, 106]
# branches ['100->101', '100->102', '102->103', '102->104']

import pytest
from sanic.cookies import Cookie
from sanic.cookies import _is_legal_key

# Assuming _is_legal_key function is defined as follows:
# def _is_legal_key(key):
#     return all(char.isalnum() or char in "-._" for char in key)

@pytest.fixture
def cleanup():
    # Fixture to clean up any global state if necessary
    yield
    # Here you would clean up any global state if the Cookie class affected it

def test_cookie_initialization_with_reserved_key(cleanup):
    reserved_key = "reserved"
    with pytest.raises(KeyError) as exc_info:
        Cookie._keys = {reserved_key}  # Mocking the reserved keys
        Cookie(reserved_key, "value")
    assert "Cookie name is a reserved word" in str(exc_info.value)

def test_cookie_initialization_with_illegal_characters(cleanup):
    illegal_key = "illegal@key"
    with pytest.raises(KeyError) as exc_info:
        Cookie(illegal_key, "value")
    assert "Cookie key contains illegal characters" in str(exc_info.value)

def test_cookie_initialization_with_legal_key(cleanup):
    legal_key = "legal-key"
    value = "value"
    cookie = Cookie(legal_key, value)
    assert cookie.key == legal_key
    assert cookie.value == value
