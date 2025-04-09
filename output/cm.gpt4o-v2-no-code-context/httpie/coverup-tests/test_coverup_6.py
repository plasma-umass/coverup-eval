# file: httpie/context.py:104-114
# asked: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [107, 114], [109, 110], [109, 114]]}
# gained: {"lines": [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114], "branches": [[107, 108], [109, 110], [109, 114]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the Environment and Config classes are imported from httpie.context
from httpie.context import Environment, Config, ConfigFileError

@pytest.fixture
def environment():
    env = Environment()
    env._config = None
    env.config_dir = '/fake/dir'
    return env

def test_config_property_new_config(monkeypatch, environment):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = True

    with patch('httpie.context.Config', return_value=mock_config):
        config = environment.config
        assert config is mock_config
        mock_config.is_new.assert_called_once()
        mock_config.load.assert_not_called()

def test_config_property_existing_config(monkeypatch, environment):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = False

    with patch('httpie.context.Config', return_value=mock_config):
        config = environment.config
        assert config is mock_config
        mock_config.is_new.assert_called_once()
        mock_config.load.assert_called_once()

def test_config_property_config_load_error(monkeypatch, environment):
    mock_config = MagicMock(spec=Config)
    mock_config.is_new.return_value = False
    mock_config.load.side_effect = ConfigFileError('Error loading config')

    with patch('httpie.context.Config', return_value=mock_config):
        with patch.object(environment, 'log_error') as mock_log_error:
            config = environment.config
            assert config is mock_config
            mock_config.is_new.assert_called_once()
            mock_config.load.assert_called_once()
            mock_log_error.assert_called_once_with(mock_config.load.side_effect, level='warning')
