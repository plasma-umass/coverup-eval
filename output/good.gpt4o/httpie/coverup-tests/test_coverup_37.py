# file httpie/sessions.py:124-151
# lines [124, 125, 126, 127, 128, 130, 132, 133, 135, 136, 138, 139, 140, 143, 144, 145, 146, 147, 148, 151]
# branches ['127->128', '127->130', '143->144', '143->151']

import pytest
from unittest.mock import Mock, patch
from httpie.sessions import Session
from requests.auth import AuthBase

@pytest.fixture
def mock_plugin_manager(mocker):
    return mocker.patch('httpie.sessions.plugin_manager')

@pytest.fixture
def mock_parse_auth(mocker):
    return mocker.patch('httpie.cli.argtypes.parse_auth')

@pytest.fixture
def mock_session(mocker):
    mocker.patch('httpie.sessions.BaseConfigDict.__init__', return_value=None)
    return Session('mock_path')

def test_session_auth_new_style(mock_plugin_manager, mock_parse_auth, mock_session):
    mock_plugin = Mock()
    mock_plugin_manager.get_auth_plugin.return_value = lambda: mock_plugin
    mock_plugin.auth_parse = True
    mock_plugin.get_auth.return_value = Mock(username='user', password='pass')
    mock_parse_auth.return_value = Mock(key='user', value='pass')

    session = mock_session
    session['auth'] = {
        'type': 'test',
        'raw_auth': 'user:pass'
    }

    auth = session.auth

    mock_plugin_manager.get_auth_plugin.assert_called_once_with('test')
    mock_parse_auth.assert_called_once_with('user:pass')
    assert auth is not None
    assert auth.username == 'user'
    assert auth.password == 'pass'

def test_session_auth_old_style(mock_plugin_manager, mock_session):
    mock_plugin = Mock()
    mock_plugin_manager.get_auth_plugin.return_value = lambda: mock_plugin
    mock_plugin.auth_parse = False
    mock_plugin.get_auth.return_value = Mock(username='user', password='pass')

    session = mock_session
    session['auth'] = {
        'type': 'test',
        'username': 'user',
        'password': 'pass'
    }

    auth = session.auth

    mock_plugin_manager.get_auth_plugin.assert_called_once_with('test')
    assert auth is not None
    assert auth.username == 'user'
    assert auth.password == 'pass'

def test_session_auth_no_type(mock_plugin_manager, mock_session):
    session = mock_session
    session['auth'] = {
        'type': None
    }

    auth = session.auth

    assert auth is None

def test_session_auth_no_auth(mock_plugin_manager, mock_session):
    session = mock_session

    auth = session.auth

    assert auth is None
