# file: httpie/context.py:104-114
# asked: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [107, 114], [109, 110], [109, 114]]}
# gained: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [109, 110], [109, 114]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.context import Environment
from httpie.config import Config, ConfigFileError

@pytest.fixture
def environment():
    env = Environment()
    env._config = None
    env.config_dir = '/non/existent/path'
    return env

def test_config_loads_existing_config(environment, monkeypatch):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = False
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)

    environment.config

    mock_config.load.assert_called_once()

def test_config_handles_config_file_error(environment, monkeypatch):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = False
    mock_config.load.side_effect = ConfigFileError('error')
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)
    mock_log_error = MagicMock()
    monkeypatch.setattr(environment, 'log_error', mock_log_error)

    environment.config

    mock_log_error.assert_called_once_with(mock_config.load.side_effect, level='warning')

def test_config_creates_new_config(environment, monkeypatch):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = True
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)

    config = environment.config

    assert config == mock_config
    mock_config.load.assert_not_called()
