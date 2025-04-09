# file lib/ansible/plugins/shell/powershell.py:113-118
# lines [113, 114, 115, 116, 118]
# branches ['115->116', '115->118']

import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_remove_non_recursive(shell_module, mocker):
    mock_escape = mocker.patch.object(shell_module, '_escape', return_value='escaped_path')
    mock_unquote = mocker.patch.object(shell_module, '_unquote', return_value='unquoted_path')
    mock_encode_script = mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.remove('test_path', recurse=False)

    mock_escape.assert_called_once_with('unquoted_path')
    mock_unquote.assert_called_once_with('test_path')
    mock_encode_script.assert_called_once_with("Remove-Item 'escaped_path' -Force;")
    assert result == 'encoded_script'

def test_remove_recursive(shell_module, mocker):
    mock_escape = mocker.patch.object(shell_module, '_escape', return_value='escaped_path')
    mock_unquote = mocker.patch.object(shell_module, '_unquote', return_value='unquoted_path')
    mock_encode_script = mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.remove('test_path', recurse=True)

    mock_escape.assert_called_once_with('unquoted_path')
    mock_unquote.assert_called_once_with('test_path')
    mock_encode_script.assert_called_once_with("Remove-Item 'escaped_path' -Force -Recurse;")
    assert result == 'encoded_script'
