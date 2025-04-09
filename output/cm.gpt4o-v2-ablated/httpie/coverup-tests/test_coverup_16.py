# file: httpie/sessions.py:58-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}

import pytest
from pathlib import Path
from httpie.sessions import Session

@pytest.fixture
def session_path(tmp_path):
    return tmp_path / "session.json"

def test_session_initialization(session_path):
    session = Session(session_path)
    
    assert isinstance(session, Session)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }

def test_session_path_initialization_with_str(session_path):
    session = Session(str(session_path))
    
    assert isinstance(session, Session)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }

def test_session_path_initialization_with_path(session_path):
    session = Session(session_path)
    
    assert isinstance(session, Session)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }
