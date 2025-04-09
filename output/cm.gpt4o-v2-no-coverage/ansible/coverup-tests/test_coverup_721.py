# file: lib/ansible/plugins/shell/powershell.py:148-162
# asked: {"lines": [148, 149, 150, 161, 162], "branches": []}
# gained: {"lines": [148, 149, 150, 161, 162], "branches": []}

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_exists_path(shell_module, mocker):
    mock_escape = mocker.patch.object(shell_module, '_escape', return_value='escaped_path')
    mock_unquote = mocker.patch.object(shell_module, '_unquote', return_value='unquoted_path')
    mock_encode_script = mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.exists('test_path')

    mock_unquote.assert_called_once_with('test_path')
    mock_escape.assert_called_once_with('unquoted_path')
    expected_script = '''
            If (Test-Path 'escaped_path')
            {
                $res = 0;
            }
            Else
            {
                $res = 1;
            }
            Write-Output '$res';
            Exit $res;
         '''
    mock_encode_script.assert_called_once_with(expected_script)
    assert result == 'encoded_script'
