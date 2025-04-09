# file: httpie/sessions.py:113-122
# asked: {"lines": [113, 114, 116, 117, 118, 119, 120, 121], "branches": [[118, 0], [118, 119]]}
# gained: {"lines": [113, 114, 116, 117, 118, 119, 120, 121], "branches": [[118, 0], [118, 119]]}

import pytest
from requests.cookies import RequestsCookieJar, create_cookie
from httpie.sessions import Session

def test_session_cookies_setter():
    # Create a RequestsCookieJar and add a cookie to it
    jar = RequestsCookieJar()
    cookie = create_cookie(name='test_cookie', value='test_value', path='/', secure=True, expires=None)
    jar.set_cookie(cookie)

    # Create a Session object
    session = Session(path='test_session.json')

    # Set the cookies using the setter
    session.cookies = jar

    # Verify that the cookies have been set correctly
    assert 'test_cookie' in session['cookies']
    assert session['cookies']['test_cookie']['value'] == 'test_value'
    assert session['cookies']['test_cookie']['path'] == '/'
    assert session['cookies']['test_cookie']['secure'] is True
    assert session['cookies']['test_cookie']['expires'] is None

    # Clean up
    del session

