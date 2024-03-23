# file httpie/sessions.py:158-161
# lines [158, 159, 160, 161]
# branches ['159->exit', '159->160', '160->159', '160->161']

import pytest
from httpie.sessions import Session
from unittest.mock import MagicMock

@pytest.fixture
def session(tmp_path):
    session_path = tmp_path / "session.json"
    s = Session(path=session_path)
    s['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    yield s
    s['cookies'].clear()

def test_remove_cookies(session):
    assert 'cookie1' in session['cookies']
    assert 'cookie2' in session['cookies']
    
    session.remove_cookies(['cookie1', 'nonexistent_cookie'])
    
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' in session['cookies']
