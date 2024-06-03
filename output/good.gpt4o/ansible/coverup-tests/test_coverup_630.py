# file lib/ansible/plugins/shell/powershell.py:148-162
# lines [148, 149, 150, 161, 162]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_exists_path(shell_module, mocker):
    path = "C:\\test\\path"
    expected_script = '''
            If (Test-Path 'C:\\test\\path')
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
    mock_encode_script = mocker.patch.object(shell_module, '_encode_script', return_value="encoded_script")
    mock_unquote = mocker.patch.object(shell_module, '_unquote', return_value=path)
    mock_escape = mocker.patch.object(shell_module, '_escape', return_value=path)

    result = shell_module.exists(path)

    mock_unquote.assert_called_once_with(path)
    mock_escape.assert_called_once_with(path)
    mock_encode_script.assert_called_once_with(expected_script)
    assert result == "encoded_script"
