# file: httpie/sessions.py:124-151
# asked: {"lines": [126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144], [143, 151]]}
# gained: {"lines": [126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144]]}

import pytest
from unittest.mock import Mock, patch
from httpie.sessions import Session
from httpie.plugins.registry import plugin_manager
from httpie.cli.argtypes import parse_auth
from requests.auth import AuthBase

class MockAuthPlugin(AuthBase):
    def __init__(self):
        self.raw_auth = None
        self.auth_parse = True

    def get_auth(self, username, password):
        return (username, password)

@pytest.fixture
def mock_plugin_manager(monkeypatch):
    mock_manager = Mock()
    mock_manager.get_auth_plugin.return_value = MockAuthPlugin
    monkeypatch.setattr(plugin_manager, 'get_auth_plugin', mock_manager.get_auth_plugin)
    return mock_manager

@pytest.fixture
def mock_parse_auth(monkeypatch):
    mock_parse = Mock()
    mock_parse.return_value = Mock(key='user', value='pass')
    monkeypatch.setattr('httpie.cli.argtypes.parse_auth', mock_parse)
    return mock_parse

def test_auth_new_style(mock_plugin_manager, mock_parse_auth):
    session = Session(path='test_path')
    session['auth'] = {'type': 'mock', 'raw_auth': 'user:pass'}
    auth = session.auth
    assert auth == ('user', 'pass')
    mock_plugin_manager.get_auth_plugin.assert_called_once_with('mock')
    mock_parse_auth.assert_called_once_with('user:pass')

def test_auth_old_style(mock_plugin_manager):
    session = Session(path='test_path')
    session['auth'] = {'type': 'mock', 'username': 'user', 'password': 'pass'}
    auth = session.auth
    assert auth == ('user', 'pass')
    mock_plugin_manager.get_auth_plugin.assert_called_once_with('mock')

def test_auth_no_type():
    session = Session(path='test_path')
    session['auth'] = {'username': 'user', 'password': 'pass'}
    with pytest.raises(KeyError):
        auth = session.auth

def test_auth_no_auth():
    session = Session(path='test_path')
    auth = session.auth
    assert auth is None
