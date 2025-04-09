# file: httpie/sessions.py:153-156
# asked: {"lines": [153, 154, 155, 156], "branches": []}
# gained: {"lines": [153, 154, 155, 156], "branches": []}

import pytest
from httpie.sessions import Session

def test_session_auth_setter(monkeypatch):
    def mock_init(self, path):
        self['auth'] = None

    monkeypatch.setattr(Session, '__init__', mock_init)
    
    session = Session('mock_path')
    valid_auth = {'type': 'basic', 'raw_auth': 'user:pass'}
    
    session.auth = valid_auth
    
    assert session['auth'] == valid_auth

def test_session_auth_setter_invalid_keys(monkeypatch):
    def mock_init(self, path):
        self['auth'] = None

    monkeypatch.setattr(Session, '__init__', mock_init)
    
    session = Session('mock_path')
    invalid_auth = {'username': 'user', 'password': 'pass'}
    
    with pytest.raises(AssertionError):
        session.auth = invalid_auth
