# file: httpie/sessions.py:113-122
# asked: {"lines": [113, 114, 116, 117, 118, 119, 120, 121], "branches": [[118, 0], [118, 119]]}
# gained: {"lines": [113, 114, 116, 117, 118, 119, 120, 121], "branches": [[118, 0], [118, 119]]}

import pytest
from httpie.sessions import Session
from requests.cookies import RequestsCookieJar, create_cookie

def test_session_cookies_setter(tmp_path):
    jar = RequestsCookieJar()
    cookie = create_cookie(name='test_cookie', value='test_value', path='/', secure=True, expires=None)
    jar.set_cookie(cookie)

    session = Session(path=str(tmp_path / 'session.json'))
    session.cookies = jar

    assert 'test_cookie' in session['cookies']
    assert session['cookies']['test_cookie']['value'] == 'test_value'
    assert session['cookies']['test_cookie']['path'] == '/'
    assert session['cookies']['test_cookie']['secure'] is True
    assert session['cookies']['test_cookie']['expires'] is None
