# file httpie/sessions.py:104-111
# lines [106, 107, 108, 109, 110, 111]
# branches ['107->108', '107->110']

import pytest
from httpie.sessions import Session
from requests.cookies import RequestsCookieJar, create_cookie

@pytest.fixture
def mock_session(mocker):
    session_data = {
        'cookies': {
            'test_cookie': {
                'value': 'test_value',
                'domain': 'example.com',
                'path': '/',
                'expires': None,
                'secure': False,
                'rest': {'HttpOnly': None},
                'version': 0
            }
        }
    }
    mocker.patch.object(Session, '__getitem__', lambda self, key: session_data[key])
    return Session(path='dummy_path')

def test_session_cookies(mock_session):
    jar = mock_session.cookies
    assert isinstance(jar, RequestsCookieJar)
    assert 'test_cookie' in jar
    assert jar['test_cookie'] == 'test_value'
    assert jar.get_dict()['test_cookie'] == 'test_value'
