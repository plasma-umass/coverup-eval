# file: httpie/sessions.py:153-156
# asked: {"lines": [153, 154, 155, 156], "branches": []}
# gained: {"lines": [153, 154, 155, 156], "branches": []}

import pytest
from pathlib import Path
from httpie.sessions import Session

@pytest.fixture
def session_file(tmp_path):
    return tmp_path / "session.json"

@pytest.fixture
def session(session_file):
    return Session(session_file)

def test_session_auth_setter(session):
    # Test setting auth with correct keys
    auth_data = {'type': 'basic', 'raw_auth': 'user:pass'}
    session.auth = auth_data
    assert session['auth'] == auth_data

    # Test setting auth with incorrect keys
    with pytest.raises(AssertionError):
        session.auth = {'username': 'user', 'password': 'pass'}

def test_session_cleanup(session_file):
    # Ensure the session file is cleaned up
    session_file.unlink(missing_ok=True)
    assert not session_file.exists()
