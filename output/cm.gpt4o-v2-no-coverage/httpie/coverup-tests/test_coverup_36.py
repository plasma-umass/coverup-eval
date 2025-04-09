# file: httpie/sessions.py:58-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}

import pytest
from pathlib import Path
from httpie.sessions import Session

def test_session_init():
    # Test with string path
    session = Session('test_path')
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}
    assert isinstance(session.path, Path)

    # Test with Path object
    session = Session(Path('test_path'))
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}
    assert isinstance(session.path, Path)
