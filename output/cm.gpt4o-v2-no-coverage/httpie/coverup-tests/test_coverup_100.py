# file: httpie/context.py:104-114
# asked: {"lines": [110, 111, 112, 113], "branches": [[109, 110]]}
# gained: {"lines": [110, 111, 112, 113], "branches": [[109, 110]]}

import pytest
from unittest.mock import MagicMock, patch
from httpie.context import Environment
from httpie.config import Config, ConfigFileError

@pytest.fixture
def environment():
    env = Environment()
    env._config = None
    env.config_dir = '/non/existent/directory'
    env.log_error = MagicMock()
    return env

def test_config_new_file(environment):
    with patch('httpie.config.Path.exists', return_value=False):
        config = environment.config
        assert isinstance(config, Config)
        assert config.is_new()
        environment.log_error.assert_not_called()

def test_config_existing_file(environment):
    with patch('httpie.config.Path.exists', return_value=True), \
         patch('httpie.config.Config.load', return_value=None):
        config = environment.config
        assert isinstance(config, Config)
        assert not config.is_new()
        environment.log_error.assert_not_called()

def test_config_load_error(environment):
    with patch('httpie.config.Path.exists', return_value=True), \
         patch('httpie.config.Config.load', side_effect=ConfigFileError('error')):
        config = environment.config
        assert isinstance(config, Config)
        assert not config.is_new()
        environment.log_error.assert_called_once()
        call_args = environment.log_error.call_args
        assert isinstance(call_args[0][0], ConfigFileError)
        assert call_args[0][0].args[0] == 'error'
        assert call_args[1]['level'] == 'warning'
