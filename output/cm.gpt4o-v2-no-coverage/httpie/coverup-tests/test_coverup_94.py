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
    monkeypatch.setattr('httpie.sessions.Session', lambda path: mock_session)
    return mock_session

def test_get_httpie_session_with_path_in_session_name(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mock/session/name'
    host = None
    url = 'http://example.com'

    with patch('os.path.expanduser', return_value='/expanded/mock/session/name') as expanduser_mock:
        session = get_httpie_session(config_dir, session_name, host, url)
        expanduser_mock.assert_called_once_with(session_name)
        mock_session.load.assert_called_once()
        assert session == mock_session

def test_get_httpie_session_without_host(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mocksession'
    host = None
    url = 'http+unix://%2Fvar%2Frun%2Fsocket'

    session = get_httpie_session(config_dir, session_name, host, url)
    expected_path = config_dir / SESSIONS_DIR_NAME / 'localhost' / f'{session_name}.json'
    assert mock_session.load.called
    assert session == mock_session

def test_get_httpie_session_with_host(mock_session):
    config_dir = Path('/mock/config/dir')
    session_name = 'mocksession'
    host = 'example.com:8080'
    url = 'http://example.com'

    session = get_httpie_session(config_dir, session_name, host, url)
    expected_path = config_dir / SESSIONS_DIR_NAME / 'example_com_8080' / f'{session_name}.json'
    assert mock_session.load.called
    assert session == mock_session
