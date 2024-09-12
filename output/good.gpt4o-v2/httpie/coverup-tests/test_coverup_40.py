# file: httpie/sessions.py:104-111
# asked: {"lines": [104, 105, 106, 107, 108, 109, 110, 111], "branches": [[107, 108], [107, 110]]}
# gained: {"lines": [104, 105, 106, 107, 108, 109, 110, 111], "branches": [[107, 108], [107, 110]]}

import pytest
from requests.cookies import RequestsCookieJar, create_cookie
from httpie.sessions import Session

@pytest.fixture
def session_with_cookies(tmp_path):
    session_path = tmp_path / "session.json"
    session = Session(session_path)
    session['cookies'] = {
        'cookie1': {'value': 'value1', 'path': '/', 'domain': 'example.com'},
        'cookie2': {'value': 'value2', 'path': '/', 'domain': 'example.com'}
    }
    return session

def test_session_cookies_property(session_with_cookies):
    session = session_with_cookies
    cookies = session.cookies

    assert isinstance(cookies, RequestsCookieJar)
    assert len(cookies) == 2
    assert cookies['cookie1'] == 'value1'
    assert cookies['cookie2'] == 'value2'

    # Ensure the original session cookies dict is not modified
    assert 'value' not in session['cookies']['cookie1']
    assert 'value' not in session['cookies']['cookie2']
