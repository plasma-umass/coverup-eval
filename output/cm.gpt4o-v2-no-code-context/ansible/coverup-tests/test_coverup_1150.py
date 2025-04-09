# file: lib/ansible/plugins/loader.py:69-99
# asked: {"lines": [81, 82, 85, 86, 87, 88, 90, 94], "branches": [[76, 90], [77, 92], [84, 85], [85, 86], [85, 92], [86, 85], [86, 87], [93, 94], [96, 99]]}
# gained: {"lines": [85, 86, 87, 88, 90, 94], "branches": [[76, 90], [84, 85], [85, 86], [85, 92], [86, 85], [86, 87], [93, 94]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import shell_loader

# Assuming the function get_shell_plugin is part of a module named 'loader'
from ansible.plugins.loader import get_shell_plugin

@pytest.fixture
def mock_shell_loader(monkeypatch):
    mock_loader = MagicMock()
    monkeypatch.setattr(shell_loader, 'get', mock_loader.get)
    monkeypatch.setattr(shell_loader, 'all', mock_loader.all)
    return mock_loader

def test_get_shell_plugin_no_shell_type_with_executable(mock_shell_loader):
    mock_shell_loader.get.side_effect = [None, MagicMock()]
    mock_shell_loader.all.return_value = [MagicMock(COMPATIBLE_SHELLS=['bash'], SHELL_FAMILY='sh')]
    shell = get_shell_plugin(executable='/bin/bash')
    assert shell is not None
    assert shell_loader.get.call_count == 2

def test_get_shell_plugin_executable_not_found(mock_shell_loader):
    mock_shell_loader.get.side_effect = [None, None]
    mock_shell_loader.all.return_value = [MagicMock(COMPATIBLE_SHELLS=[], SHELL_FAMILY='sh')]
    with pytest.raises(AnsibleError, match="Could not find the shell plugin required"):
        get_shell_plugin(executable='/bin/bash')

def test_get_shell_plugin_no_shell_type_no_executable_raises_error(mock_shell_loader):
    with pytest.raises(AnsibleError, match="Either a shell type or a shell executable must be provided"):
        get_shell_plugin()

def test_get_shell_plugin_shell_type_not_found(mock_shell_loader):
    mock_shell_loader.get.return_value = None
    with pytest.raises(AnsibleError, match="Could not find the shell plugin required"):
        get_shell_plugin(shell_type='nonexistent')

def test_get_shell_plugin_executable_set(mock_shell_loader):
    mock_shell = MagicMock()
    mock_shell_loader.get.return_value = mock_shell
    shell = get_shell_plugin(shell_type='sh', executable='/bin/bash')
    assert shell == mock_shell
    assert shell.executable == '/bin/bash'
    mock_shell_loader.get.assert_called_once_with('sh')
