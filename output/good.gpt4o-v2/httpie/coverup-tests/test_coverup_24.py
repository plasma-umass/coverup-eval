# file: httpie/sessions.py:58-66
# asked: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}
# gained: {"lines": [58, 59, 60, 61, 62, 63, 64, 65], "branches": []}

import pytest
from pathlib import Path
from httpie.sessions import Session

def test_session_init_with_str_path():
    path = 'test_path'
    session = Session(path)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}

def test_session_init_with_pathlib_path():
    path = Path('test_path')
    session = Session(path)
    assert session['headers'] == {}
    assert session['cookies'] == {}
    assert session['auth'] == {'type': None, 'username': None, 'password': None}
