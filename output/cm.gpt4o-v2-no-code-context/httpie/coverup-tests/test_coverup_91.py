# file: httpie/sessions.py:124-151
# asked: {"lines": [126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144], [143, 151]]}
# gained: {"lines": [126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151], "branches": [[127, 128], [127, 130], [143, 144]]}

import pytest
from unittest.mock import Mock, patch
from httpie.sessions import Session
from requests.auth import AuthBase

@pytest.fixture
def session():
    return Session(path='dummy_path')

def test_auth_no_auth(session):
    session['auth'] = None
    assert session.auth is None

def test_auth_no_auth_type(session):
    session['auth'] = {'type': None}
    assert session.auth is None

@patch('httpie.sessions.plugin_manager')
def test_auth_new_style(mock_plugin_manager, session):
    mock_plugin = Mock()
    mock_plugin.raw_auth = 'user:pass'
    mock_plugin.auth_parse = True
    mock_plugin_manager.get_auth_plugin.return_value = lambda: mock_plugin

    session['auth'] = {'type': 'basic', 'raw_auth': 'user:pass'}
    auth = session.auth

    mock_plugin_manager.get_auth_plugin.assert_called_once_with('basic')
    assert auth is not None
    assert mock_plugin.raw_auth == 'user:pass'

@patch('httpie.sessions.plugin_manager')
def test_auth_old_style(mock_plugin_manager, session):
    mock_plugin = Mock()
    mock_plugin.auth_parse = False
    mock_plugin_manager.get_auth_plugin.return_value = lambda: mock_plugin

    session['auth'] = {'type': 'basic', 'username': 'user', 'password': 'pass'}
    auth = session.auth

    mock_plugin_manager.get_auth_plugin.assert_called_once_with('basic')
    assert auth is not None
    assert mock_plugin.get_auth.call_args[1] == {'username': 'user', 'password': 'pass'}

@patch('httpie.sessions.plugin_manager')
@patch('httpie.cli.argtypes.parse_auth')
def test_auth_new_style_with_parse(mock_parse_auth, mock_plugin_manager, session):
    mock_plugin = Mock()
    mock_plugin.raw_auth = 'user:pass'
    mock_plugin.auth_parse = True
    mock_plugin_manager.get_auth_plugin.return_value = lambda: mock_plugin
    mock_parse_auth.return_value = Mock(key='user', value='pass')

    session['auth'] = {'type': 'basic', 'raw_auth': 'user:pass'}
    auth = session.auth

    mock_plugin_manager.get_auth_plugin.assert_called_once_with('basic')
    mock_parse_auth.assert_called_once_with('user:pass')
    assert auth is not None
    assert mock_plugin.get_auth.call_args[1] == {'username': 'user', 'password': 'pass'}
