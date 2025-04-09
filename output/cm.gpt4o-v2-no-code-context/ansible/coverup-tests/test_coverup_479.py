# file: lib/ansible/plugins/shell/powershell.py:113-118
# asked: {"lines": [113, 114, 115, 116, 118], "branches": [[115, 116], [115, 118]]}
# gained: {"lines": [113, 114, 115, 116, 118], "branches": [[115, 116], [115, 118]]}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_remove_with_recurse(shell_module, mocker):
    mocker.patch.object(shell_module, '_escape', return_value='escaped_path')
    mocker.patch.object(shell_module, '_unquote', return_value='unquoted_path')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.remove('some_path', recurse=True)

    shell_module._escape.assert_called_once_with('unquoted_path')
    shell_module._unquote.assert_called_once_with('some_path')
    shell_module._encode_script.assert_called_once_with("Remove-Item 'escaped_path' -Force -Recurse;")
    assert result == 'encoded_script'

def test_remove_without_recurse(shell_module, mocker):
    mocker.patch.object(shell_module, '_escape', return_value='escaped_path')
    mocker.patch.object(shell_module, '_unquote', return_value='unquoted_path')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.remove('some_path', recurse=False)

    shell_module._escape.assert_called_once_with('unquoted_path')
    shell_module._unquote.assert_called_once_with('some_path')
    shell_module._encode_script.assert_called_once_with("Remove-Item 'escaped_path' -Force;")
    assert result == 'encoded_script'
