# file thefuck/conf.py:17-34
# lines [17, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 34]
# branches []

import os
import pytest
from thefuck.conf import Settings
from thefuck.logs import exception


def test_settings_init_with_file_and_env_exceptions(mocker, tmp_path):
    # Mocking the exception method to assert it's called
    exception_mock = mocker.patch('thefuck.logs.exception')

    # Mocking the _setup_user_dir and _init_settings_file to do nothing
    mocker.patch.object(Settings, '_setup_user_dir')
    mocker.patch.object(Settings, '_init_settings_file')

    # Mocking the _settings_from_file to raise an exception
    mocker.patch.object(Settings, '_settings_from_file', side_effect=Exception("File error"))

    # Mocking the _settings_from_env to raise an exception
    mocker.patch.object(Settings, '_settings_from_env', side_effect=Exception("Env error"))

    # Mocking the _settings_from_args to return an empty dict
    mocker.patch.object(Settings, '_settings_from_args', return_value={})

    # Creating a Settings instance and initializing it
    settings = Settings()
    settings.init()

    # Asserting that the exception method was called for both file and env errors
    assert exception_mock.call_count == 2
    exception_mock.assert_any_call("Can't load settings from file", mocker.ANY)
    exception_mock.assert_any_call("Can't load settings from env", mocker.ANY)
