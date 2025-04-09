# file sanic/cookies.py:83-98
# lines [83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 97]
# branches []

import pytest
from sanic.cookies import Cookie

def test_cookie_initialization():
    cookie = Cookie('test_key', 'test_value')
    assert isinstance(cookie, dict)
    assert hasattr(cookie, '_keys')
    assert hasattr(cookie, '_flags')

def test_cookie_keys():
    cookie = Cookie('test_key', 'test_value')
    for key in Cookie._keys:
        assert key in cookie._keys

def test_cookie_flags():
    cookie = Cookie('test_key', 'test_value')
    for flag in Cookie._flags:
        assert flag in cookie._flags

@pytest.fixture
def mock_cookie(mocker):
    mocker.patch('sanic.cookies.Cookie', autospec=True)
    yield
    mocker.stopall()

def test_cookie_with_mock(mock_cookie):
    cookie = Cookie('test_key', 'test_value')
    assert isinstance(cookie, Cookie)
