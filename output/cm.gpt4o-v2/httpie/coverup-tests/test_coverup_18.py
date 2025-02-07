# file: httpie/context.py:104-114
# asked: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [107, 114], [109, 110], [109, 114]]}
# gained: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [109, 110], [109, 114]]}

import pytest
from unittest.mock import Mock, patch
from httpie.context import Environment
from httpie.config import Config, ConfigFileError

@pytest.fixture
def environment():
    return Environment()

def test_config_loads_existing_config(environment, monkeypatch):
    mock_config = Mock(spec=Config)
    mock_config.is_new.return_value = False
    monkeypatch.setattr(environment, '_config', None)
    monkeypatch.setattr(environment, 'config_dir', '/mock/dir')
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)

    environment.config

    mock_config.load.assert_called_once()

def test_config_handles_config_file_error(environment, monkeypatch):
    mock_config = Mock(spec=Config)
    mock_config.is_new.return_value = False
    mock_config.load.side_effect = ConfigFileError('mock error')
    mock_log_error = Mock()
    monkeypatch.setattr(environment, '_config', None)
    monkeypatch.setattr(environment, 'config_dir', '/mock/dir')
    monkeypatch.setattr(environment, 'log_error', mock_log_error)
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)

    environment.config

    mock_log_error.assert_called_once()
    assert isinstance(mock_log_error.call_args[0][0], ConfigFileError)
    assert mock_log_error.call_args[1] == {'level': 'warning'}

def test_config_creates_new_config(environment, monkeypatch):
    mock_config = Mock(spec=Config)
    mock_config.is_new.return_value = True
    monkeypatch.setattr(environment, '_config', None)
    monkeypatch.setattr(environment, 'config_dir', '/mock/dir')
    monkeypatch.setattr('httpie.context.Config', lambda directory: mock_config)

    config = environment.config

    assert config is mock_config
    mock_config.load.assert_not_called()
