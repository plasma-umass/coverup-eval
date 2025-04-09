# file: httpie/sessions.py:124-151
# asked: {"lines": [124, 125, 126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144], [143, 151]]}
# gained: {"lines": [124, 125, 126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144]]}

import pytest
from unittest.mock import Mock, patch
from httpie.sessions import Session
from httpie.plugins.registry import plugin_manager
from requests.auth import AuthBase

class MockAuthPlugin(AuthBase):
    def __init__(self):
        self.raw_auth = None
        self.auth_parse = True

    def get_auth(self, username, password):
        return (username, password)

@pytest.fixture
def session():
    return Session(path='test_session.json')

def test_auth_property_new_style(monkeypatch, session):
    mock_plugin = MockAuthPlugin()
    monkeypatch.setattr(plugin_manager, 'get_auth_plugin', lambda x: lambda: mock_plugin)
    session['auth'] = {'type': 'mock', 'raw_auth': 'user:pass'}
    
    auth = session.auth
    assert auth == ('user', 'pass')

def test_auth_property_old_style(monkeypatch, session):
    mock_plugin = MockAuthPlugin()
    monkeypatch.setattr(plugin_manager, 'get_auth_plugin', lambda x: lambda: mock_plugin)
    session['auth'] = {'type': 'mock', 'username': 'user', 'password': 'pass'}
    
    auth = session.auth
    assert auth == ('user', 'pass')

def test_auth_property_no_auth_type(session):
    session['auth'] = {'type': None, 'username': 'user', 'password': 'pass'}
    
    auth = session.auth
    assert auth is None

def test_auth_property_missing_auth_key(session):
    session['auth'] = {}
    
    auth = session.auth
    assert auth is None
