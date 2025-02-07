# file: httpie/sessions.py:30-51
# asked: {"lines": [36, 37, 39, 40, 42, 45, 46, 47, 49, 50, 51], "branches": [[36, 37], [36, 39], [40, 42], [40, 45]]}
# gained: {"lines": [36, 37, 39, 40, 45, 46, 47, 49, 50, 51], "branches": [[36, 37], [36, 39], [40, 45]]}

import os
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest
from httpie.sessions import get_httpie_session, Session, SESSIONS_DIR_NAME

@pytest.fixture
def mock_session(monkeypatch):
    mock_session = MagicMock(spec=Session)
    monkeypatch.setattr('httpie.sessions.Session', mock_session)
    return mock_session

def test_get_httpie_session_with_path_separator(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = '~/mock/session'
    host = None
    url = 'http://example.com'

    session = get_httpie_session(config_dir, session_name, host, url)

    mock_session.return_value.load.assert_called_once()
    assert session == mock_session.return_value
    mock_session.assert_called_with(os.path.expanduser(session_name))

def test_get_httpie_session_without_hostname(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mock_session'
    host = None
    url = 'http+unix://%2Fvar%2Frun%2Fsocket'

    session = get_httpie_session(config_dir, session_name, host, url)

    mock_session.return_value.load.assert_called_once()
    assert session == mock_session.return_value
    expected_path = config_dir / SESSIONS_DIR_NAME / '%2Fvar%2Frun%2Fsocket' / f'{session_name}.json'
    mock_session.assert_called_with(expected_path)

def test_get_httpie_session_with_hostname(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mock_session'
    host = None
    url = 'http://example.com:8080'

    session = get_httpie_session(config_dir, session_name, host, url)

    mock_session.return_value.load.assert_called_once()
    assert session == mock_session.return_value
    expected_path = config_dir / SESSIONS_DIR_NAME / 'example.com_8080' / f'{session_name}.json'
    mock_session.assert_called_with(expected_path)

def test_get_httpie_session_with_host_parameter(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mock_session'
    host = 'customhost'
    url = 'http://example.com'

    session = get_httpie_session(config_dir, session_name, host, url)

    mock_session.return_value.load.assert_called_once()
    assert session == mock_session.return_value
    expected_path = config_dir / SESSIONS_DIR_NAME / 'customhost' / f'{session_name}.json'
    mock_session.assert_called_with(expected_path)
