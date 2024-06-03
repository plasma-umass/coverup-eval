# file lib/ansible/plugins/loader.py:69-99
# lines [69, 71, 73, 76, 77, 78, 79, 80, 81, 82, 84, 85, 86, 87, 88, 90, 92, 93, 94, 96, 97, 99]
# branches ['71->73', '71->92', '76->77', '76->90', '77->78', '77->92', '84->85', '84->92', '85->86', '85->92', '86->85', '86->87', '93->94', '93->96', '96->97', '96->99']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import get_shell_plugin

@patch('ansible.plugins.loader.shell_loader')
def test_get_shell_plugin_default_sh(mock_shell_loader):
    mock_shell = MagicMock()
    mock_shell_loader.get.return_value = mock_shell
    mock_shell_loader.all.return_value = []

    shell = get_shell_plugin(shell_type='sh')
    assert shell == mock_shell
    mock_shell_loader.get.assert_called_with('sh')

@patch('ansible.plugins.loader.shell_loader')
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

@patch('ansible.plugins.loader.shell_loader')
def test_get_shell_plugin_no_shell_found(mock_shell_loader):
    mock_shell_loader.get.return_value = None

    with pytest.raises(AnsibleError, match="Could not find the shell plugin required"):
        get_shell_plugin(shell_type='nonexistent')

@patch('ansible.plugins.loader.shell_loader')
def test_get_shell_plugin_no_executable_provided(mock_shell_loader):
    with pytest.raises(AnsibleError, match="Either a shell type or a shell executable must be provided"):
        get_shell_plugin()
