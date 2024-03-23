# file httpie/context.py:104-114
# lines [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]
# branches ['107->108', '107->114', '109->110', '109->114']

import pytest
from httpie.context import Environment
from httpie.config import ConfigFileError

# Mocking the Config class to raise ConfigFileError on load
class MockConfig:
    def __init__(self, directory):
        self.directory = directory

    def is_new(self):
        return False

    def load(self):
        raise ConfigFileError('Mock error')

# Test function to cover the exception branch
def test_environment_config_load_error(mocker):
    # Mock the Config class to raise ConfigFileError on load
    mocker.patch('httpie.context.Config', new=MockConfig)
    # Mock the log_error method to assert it was called with the correct parameters
    log_error_mock = mocker.patch('httpie.context.Environment.log_error')

    env = Environment()
    env.config_dir = 'mock_dir'
    env._config = None  # Ensure that the config is not already set
    # Access the config property to trigger the load and exception handling
    _ = env.config

    # Assert that log_error was called with the correct parameters
    log_error_mock.assert_called_once_with(
        mocker.ANY,  # This will match any first argument (the exception instance)
        level='warning'
    )
