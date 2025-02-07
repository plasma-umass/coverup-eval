# file: lib/ansible/plugins/loader.py:69-99
# asked: {"lines": [69, 71, 73, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 92, 93, 94, 96, 97, 99], "branches": [[71, 73], [71, 92], [76, 77], [76, 90], [77, 78], [77, 92], [84, 85], [84, 92], [85, 86], [85, 92], [86, 85], [86, 87], [93, 94], [93, 96], [96, 97], [96, 99]]}
# gained: {"lines": [69, 71, 73, 76, 77, 78, 79, 80, 84, 85, 86, 87, 88, 90, 92, 93, 94, 96, 97, 99], "branches": [[71, 73], [71, 92], [76, 77], [76, 90], [77, 78], [84, 85], [85, 86], [85, 92], [86, 87], [93, 94], [93, 96], [96, 97], [96, 99]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import get_shell_plugin

@pytest.fixture
def mock_shell_loader():
    with patch('ansible.plugins.loader.shell_loader') as mock_loader:
        yield mock_loader

def test_get_shell_plugin_default_shell(mock_shell_loader):
    mock_shell = MagicMock()
    mock_shell_loader.get.return_value = mock_shell

    shell = get_shell_plugin(shell_type='sh')
    assert shell == mock_shell
    mock_shell_loader.get.assert_called_once_with('sh')

def test_get_shell_plugin_with_executable(mock_shell_loader):
    mock_shell = MagicMock()
    mock_shell_loader.get.side_effect = [None, mock_shell]
    mock_shell_loader.all.return_value = [mock_shell]
    mock_shell.COMPATIBLE_SHELLS = ['bash']
    mock_shell.SHELL_FAMILY = 'bash'

    shell = get_shell_plugin(executable='/bin/bash')
    assert shell == mock_shell
    assert shell.executable == '/bin/bash'
    mock_shell_loader.get.assert_any_call('bash')
    mock_shell_loader.all.assert_called_once()

def test_get_shell_plugin_with_invalid_executable(mock_shell_loader):
    mock_shell_loader.get.side_effect = [None, None]
    mock_shell_loader.all.return_value = []

    with pytest.raises(AnsibleError, match="Could not find the shell plugin required"):
        get_shell_plugin(executable='/bin/invalid')

def test_get_shell_plugin_with_shell_type(mock_shell_loader):
    mock_shell = MagicMock()
    mock_shell_loader.get.return_value = mock_shell

    shell = get_shell_plugin(shell_type='bash')
    assert shell == mock_shell
    mock_shell_loader.get.assert_called_once_with('bash')

def test_get_shell_plugin_no_shell_type_or_executable():
    with pytest.raises(AnsibleError, match="Either a shell type or a shell executable must be provided"):
        get_shell_plugin(shell_type=None, executable=None)
