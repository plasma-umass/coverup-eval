# file: lib/ansible/plugins/shell/powershell.py:148-162
# asked: {"lines": [148, 149, 150, 161, 162], "branches": []}
# gained: {"lines": [148, 149, 150, 161, 162], "branches": []}

import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_exists_path(shell_module):
    path = "C:\\test\\path"
    
    with patch.object(shell_module, '_unquote', return_value=path) as mock_unquote, \
         patch.object(shell_module, '_escape', return_value=path) as mock_escape, \
         patch.object(shell_module, '_encode_script', return_value="encoded_script") as mock_encode_script:
        
        result = shell_module.exists(path)
        
        mock_unquote.assert_called_once_with(path)
        mock_escape.assert_called_once_with(path)
        expected_script = '''
            If (Test-Path '{}')
            {{
                $res = 0;
            }}
            Else
            {{
                $res = 1;
            }}
            Write-Output '$res';
            Exit $res;
         '''.format(path)
        mock_encode_script.assert_called_once_with(expected_script)
        assert result == "encoded_script"
