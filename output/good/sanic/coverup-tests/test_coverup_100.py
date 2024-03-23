# file sanic/cookies.py:44-80
# lines [66, 69, 70, 71, 73, 75, 76, 77, 78, 79, 80]
# branches ['59->66', '69->70', '69->73', '76->77', '76->79', '77->76', '77->78']

import pytest
from sanic.cookies import CookieJar
from sanic.response import BaseHTTPResponse


@pytest.fixture
def mock_headers():
    return BaseHTTPResponse().headers


def test_cookiejar_setitem_and_delitem(mock_headers):
    jar = CookieJar(mock_headers)
    jar['test_cookie'] = 'test_value'
    assert 'test_cookie' in jar
    assert jar['test_cookie'].value == 'test_value'
    assert any('Set-Cookie' in header for header in mock_headers.keys())

    # Update the cookie value to trigger the missing branch
    jar['test_cookie'] = 'new_value'
    assert jar['test_cookie'].value == 'new_value'

    # Delete the cookie to trigger the missing branch
    del jar['test_cookie']
    assert 'test_cookie' not in jar
    assert 'test_cookie' not in jar.cookie_headers
    assert not any('test_cookie' in header for header in mock_headers.values())

    # Attempt to delete a non-existent cookie should not raise a KeyError
    # because the __delitem__ method is designed to set a cookie with an empty
    # value and a max-age of 0 if the cookie does not exist.
    jar['non_existent_cookie'] = 'value'
    del jar['non_existent_cookie']
    assert 'non_existent_cookie' not in jar
    assert 'non_existent_cookie' not in jar.cookie_headers
