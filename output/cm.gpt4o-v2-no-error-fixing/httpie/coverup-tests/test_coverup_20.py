# file: httpie/sessions.py:58-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}

import pytest
from pathlib import Path
from httpie.sessions import Session

def test_session_init():
    # Create a temporary path for testing
    temp_path = Path('/tmp/test_session.json')

    # Initialize the Session object
    session = Session(temp_path)

    # Assertions to verify the postconditions
    assert session.path == temp_path
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}

    # Clean up
    if temp_path.exists():
        temp_path.unlink()
