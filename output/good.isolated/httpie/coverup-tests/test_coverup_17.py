# file httpie/sessions.py:113-122
# lines [113, 114, 116, 117, 118, 119, 120, 121]
# branches ['118->exit', '118->119']

import pytest
from httpie.sessions import Session
from requests.cookies import RequestsCookieJar, create_cookie

@pytest.fixture
def cookie_jar():
    jar = RequestsCookieJar()
    jar.set_cookie(create_cookie('test_cookie', 'test_value', path='/test', secure=True, expires=123456789))
    return jar

def test_session_cookies_setter(cookie_jar, tmp_path):
    session = Session(str(tmp_path / 'session.json'))
    session.cookies = cookie_jar
    assert 'test_cookie' in session['cookies']
    assert session['cookies']['test_cookie']['value'] == 'test_value'
    assert session['cookies']['test_cookie']['path'] == '/test'
    assert session['cookies']['test_cookie']['secure'] is True
    assert session['cookies']['test_cookie']['expires'] == 123456789
