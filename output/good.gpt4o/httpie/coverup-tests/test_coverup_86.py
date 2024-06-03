# file httpie/context.py:104-114
# lines [110, 111, 112, 113]
# branches ['109->110']

import pytest
from unittest.mock import Mock, patch
from httpie.context import Environment, Config, ConfigFileError

@pytest.fixture
def mock_environment(mocker):
    env = Environment()
    env._config = None
    env.config_dir = '/non/existent/dir'
    env.log_error = Mock()
    return env

def test_environment_config_load_error(mock_environment, mocker):
    mock_config = mocker.patch('httpie.context.Config', autospec=True)
    mock_config_instance = mock_config.return_value
    mock_config_instance.is_new.return_value = False
    mock_config_instance.load.side_effect = ConfigFileError('Test error')

    with patch.object(mock_environment, '_config', mock_config_instance):
        config = mock_environment.config

    mock_config_instance.load.assert_called_once()
    mock_environment.log_error.assert_called_once_with(mock_config_instance.load.side_effect, level='warning')
    assert config == mock_config_instance
