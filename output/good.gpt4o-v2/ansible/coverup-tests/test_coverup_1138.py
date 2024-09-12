# file: lib/ansible/plugins/shell/powershell.py:266-287
# asked: {"lines": [268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}
# gained: {"lines": [268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}

import pytest
from unittest.mock import patch
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_encode_script_with_dash(shell_module):
    script = '-'
    _common_args = ['powershell']
    expected = _common_args + ['-Command', '-']
    
    with patch('ansible.plugins.shell.powershell._common_args', _common_args):
        result = shell_module._encode_script(script)
    
    assert result == ' '.join(expected)

def test_encode_script_with_strict_mode_and_preserve_rc(shell_module):
    script = 'Write-Output "Hello World"'
    _common_args = ['powershell']
    expected_start = 'powershell -EncodedCommand'
    
    with patch('ansible.plugins.shell.powershell._common_args', _common_args):
        result = shell_module._encode_script(script, strict_mode=True, preserve_rc=True)
    
    assert result.startswith(expected_start)
    assert 'UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACIA' in result

def test_encode_script_without_strict_mode(shell_module):
    script = 'Write-Output "Hello World"'
    _common_args = ['powershell']
    expected_start = 'powershell -EncodedCommand'
    
    with patch('ansible.plugins.shell.powershell._common_args', _common_args):
        result = shell_module._encode_script(script, strict_mode=False, preserve_rc=True)
    
    assert result.startswith(expected_start)
    assert 'UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACIA' not in result

def test_encode_script_without_preserve_rc(shell_module):
    script = 'Write-Output "Hello World"'
    _common_args = ['powershell']
    expected_start = 'powershell -EncodedCommand'
    
    with patch('ansible.plugins.shell.powershell._common_args', _common_args):
        result = shell_module._encode_script(script, strict_mode=True, preserve_rc=False)
    
    assert result.startswith(expected_start)
    assert 'UwBlAHQALQBTAHQAcgBpAGMAdABNAG8AZABlACAALQBWAGUAcgBzAGkAbwBuACAATABhAHQAZQBzAHQACgBXAHIAaQB0AGUALQBPAHUAdABwAHUAdAAgACIA' in result
    assert 'SQBmICgtbm90ICQ/KSAg' not in result

def test_encode_script_as_list(shell_module):
    script = 'Write-Output "Hello World"'
    _common_args = ['powershell']
    
    with patch('ansible.plugins.shell.powershell._common_args', _common_args):
        result = shell_module._encode_script(script, as_list=True)
    
    assert isinstance(result, list)
    assert result[0] == 'powershell'
    assert '-EncodedCommand' in result
