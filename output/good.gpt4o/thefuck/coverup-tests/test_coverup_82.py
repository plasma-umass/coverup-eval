# file thefuck/shells/generic.py:42-44
# lines [42, 43, 44]
# branches []

import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

def test_instant_mode_alias(mocker):
    generic_shell = Generic()
    alias_name = "test_alias"

    # Mock the warn function to ensure it is called
    warn_mock = mocker.patch('thefuck.shells.generic.warn')

    # Mock the app_alias function to ensure it is called and returns a specific value
    app_alias_mock = mocker.patch.object(Generic, 'app_alias', return_value='app_alias_return_value')

    result = generic_shell.instant_mode_alias(alias_name)

    # Assert that warn was called with the correct message
    warn_mock.assert_called_once_with("Instant mode not supported by your shell")

    # Assert that app_alias was called with the correct alias_name
    app_alias_mock.assert_called_once_with(alias_name)

    # Assert that the result of instant_mode_alias is the return value of app_alias
    assert result == 'app_alias_return_value'
