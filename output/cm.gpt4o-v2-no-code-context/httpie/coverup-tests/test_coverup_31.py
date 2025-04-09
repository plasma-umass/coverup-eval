# file: httpie/sessions.py:158-161
# asked: {"lines": [158, 159, 160, 161], "branches": [[159, 0], [159, 160], [160, 159], [160, 161]]}
# gained: {"lines": [158, 159, 160, 161], "branches": [[159, 0], [159, 160], [160, 159], [160, 161]]}

import pytest
from httpie.sessions import Session

@pytest.fixture
def session(tmp_path):
    return Session(path=tmp_path / 'session.json')

def test_remove_cookies(session):
    # Setup initial cookies
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2', 'cookie3': 'value3'}
    
    # Remove specific cookies
    session.remove_cookies(['cookie1', 'cookie3'])
    
    # Assertions to verify cookies are removed
    assert 'cookie1' not in session['cookies']
    assert 'cookie3' not in session['cookies']
    assert 'cookie2' in session['cookies']

def test_remove_nonexistent_cookie(session):
    # Setup initial cookies
    session['cookies'] = {'cookie1': 'value1', 'cookie2': 'value2'}
    
    # Attempt to remove a cookie that doesn't exist
    session.remove_cookies(['cookie3'])
    
    # Assertions to verify no cookies are removed
    assert 'cookie1' in session['cookies']
    assert 'cookie2' in session['cookies']
    assert 'cookie3' not in session['cookies']
