# file httpie/sessions.py:58-66
# lines [58, 59, 60, 61, 62, 63, 64, 65]
# branches []

import pytest
from pathlib import Path
from httpie.sessions import Session

def test_session_initialization(tmp_path):
    session_path = tmp_path / "session.json"
    session = Session(session_path)

    # Ensure the session file is created
    session.save()

    assert session_path.exists()
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }
