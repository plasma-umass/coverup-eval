# file httpie/sessions.py:113-122
# lines [113, 114, 116, 117, 118, 119, 120, 121]
# branches ['118->exit', '118->119']

import pytest
from httpie.sessions import Session
from requests.cookies import RequestsCookieJar, create_cookie

def test_session_cookies_setter(tmp_path):
    # Create a RequestsCookieJar and add a cookie to it
    jar = RequestsCookieJar()
    cookie = create_cookie(name='test_cookie', value='test_value', path='/', secure=True, expires=1234567890)
    jar.set_cookie(cookie)

    # Create a Session instance and set the cookies
    session = Session(path=str(tmp_path / 'session.json'))
    session.cookies = jar

    # Verify that the cookies have been set correctly
    assert 'test_cookie' in session['cookies']
    assert session['cookies']['test_cookie']['value'] == 'test_value'
    assert session['cookies']['test_cookie']['path'] == '/'
    assert session['cookies']['test_cookie']['secure'] is True
    assert session['cookies']['test_cookie']['expires'] == 1234567890
