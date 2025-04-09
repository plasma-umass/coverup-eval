# file: httpie/sessions.py:158-161
# asked: {"lines": [158, 159, 160, 161], "branches": [[159, 0], [159, 160], [160, 159], [160, 161]]}
# gained: {"lines": [158, 159, 160, 161], "branches": [[159, 0], [159, 160], [160, 159], [160, 161]]}

import pytest
from httpie.sessions import Session
from pathlib import Path

@pytest.fixture
def session_with_cookies(tmp_path):
    session = Session(tmp_path / "session.json")
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    return session

def test_remove_cookies(session_with_cookies):
    session = session_with_cookies
    session.remove_cookies(['cookie1'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' in session['cookies']

def test_remove_nonexistent_cookie(session_with_cookies):
    session = session_with_cookies
    session.remove_cookies(['nonexistent_cookie'])
    assert 'cookie1' in session['cookies']
    assert 'cookie2' in session['cookies']

def test_remove_all_cookies(session_with_cookies):
    session = session_with_cookies
    session.remove_cookies(['cookie1', 'cookie2'])
    assert 'cookie1' not in session['cookies']
    assert 'cookie2' not in session['cookies']
