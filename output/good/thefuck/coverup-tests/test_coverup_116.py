# file thefuck/shells/generic.py:149-154
# lines [149, 150, 151, 152, 153, 154]
# branches []

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import MagicMock, patch
from collections import namedtuple
from pathlib import Path

# Defining ShellConfiguration as a namedtuple for testing purposes
ShellConfiguration = namedtuple('ShellConfiguration', 'content path reload can_configure_automatically')

# Mocking Path.exists to control the return value
@pytest.fixture
def mock_path_exists(mocker):
    mock = mocker.patch('pathlib.Path.exists')
    mock.return_value = True
    return mock

# Test function to cover the missing lines/branches
def test_create_shell_configuration_with_existing_path(mock_path_exists):
    generic_shell = Generic()
    content = 'some content'
    path = '/some/path'
    reload = True

    # Mocking the ShellConfiguration to avoid ImportError
    with patch('thefuck.shells.generic.ShellConfiguration', ShellConfiguration):
        shell_config = generic_shell._create_shell_configuration(content, path, reload)

    assert isinstance(shell_config, ShellConfiguration)
    assert shell_config.content == content
    assert shell_config.path == path
    assert shell_config.reload == reload
    assert shell_config.can_configure_automatically == True
    mock_path_exists.assert_called_once_with()

# Test function to cover the case where the path does not exist
def test_create_shell_configuration_with_non_existing_path(mocker):
    mocker.patch('pathlib.Path.exists', return_value=False)
    generic_shell = Generic()
    content = 'some content'
    path = '/some/nonexistent/path'
    reload = False

    # Mocking the ShellConfiguration to avoid ImportError
    with patch('thefuck.shells.generic.ShellConfiguration', ShellConfiguration):
        shell_config = generic_shell._create_shell_configuration(content, path, reload)

    assert isinstance(shell_config, ShellConfiguration)
    assert shell_config.content == content
    assert shell_config.path == path
    assert shell_config.reload == reload
    assert shell_config.can_configure_automatically == False
