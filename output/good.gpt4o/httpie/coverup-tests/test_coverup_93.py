# file httpie/sessions.py:158-161
# lines [159, 160, 161]
# branches ['159->exit', '159->160', '160->159', '160->161']

import pytest
from httpie.sessions import Session

@pytest.fixture
def session_with_cookies(tmp_path):
    session = Session(path=tmp_path / 'session.json')
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    yield session
    session['cookies'].clear()

def test_remove_cookies(session_with_cookies):
    session = session_with_cookies
    session.remove_cookies(['cookie1', 'cookie3'])
    
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' in session['cookies']
    assert 'cookie3' not in session['cookies']
