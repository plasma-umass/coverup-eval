# file: httpie/sessions.py:58-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}

import pytest
from httpie.sessions import Session
from pathlib import Path

def test_session_initialization():
    # Create a temporary path for the session
    temp_path = Path('temp_session.json')
    
    # Initialize the session
    session = Session(temp_path)
    
    # Assertions to verify the postconditions
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }

    # Clean up the temporary file
    if temp_path.exists():
        temp_path.unlink()

def test_session_initialization_with_str_path():
    # Create a temporary path for the session
    temp_path = 'temp_session.json'
    
    # Initialize the session
    session = Session(temp_path)
    
    # Assertions to verify the postconditions
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {
        'type': None,
        'username': None,
        'password': None
    }

    # Clean up the temporary file
    temp_path = Path(temp_path)
    if temp_path.exists():
        temp_path.unlink()
