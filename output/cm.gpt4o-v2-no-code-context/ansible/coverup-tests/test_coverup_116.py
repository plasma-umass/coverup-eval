# file: lib/ansible/plugins/shell/powershell.py:266-287
# asked: {"lines": [266, 268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}
# gained: {"lines": [266, 268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}

import pytest
import base64
from ansible.plugins.shell.powershell import ShellModule

_common_args = ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted']

@pytest.fixture
def shell_module():
    return ShellModule()

def test_encode_script_with_dash(shell_module):
    script = '-'
    result = shell_module._encode_script(script)
    expected = ' '.join(_common_args + ['-Command', '-'])
    assert result == expected

def test_encode_script_with_strict_mode_and_preserve_rc(shell_module):
    script = 'Write-Output "Hello World"'
    result = shell_module._encode_script(script, strict_mode=True, preserve_rc=True)
    expected_script = 'Set-StrictMode -Version Latest\r\nWrite-Output "Hello World"\r\nIf (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = base64.b64encode(expected_script.encode('utf-16-le')).decode('utf-8')
    expected = ' '.join(_common_args + ['-EncodedCommand', encoded_script])
    assert result == expected

def test_encode_script_without_strict_mode(shell_module):
    script = 'Write-Output "Hello World"'
    result = shell_module._encode_script(script, strict_mode=False, preserve_rc=True)
    expected_script = 'Write-Output "Hello World"\r\nIf (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = base64.b64encode(expected_script.encode('utf-16-le')).decode('utf-8')
    expected = ' '.join(_common_args + ['-EncodedCommand', encoded_script])
    assert result == expected

def test_encode_script_without_preserve_rc(shell_module):
    script = 'Write-Output "Hello World"'
    result = shell_module._encode_script(script, strict_mode=True, preserve_rc=False)
    expected_script = 'Set-StrictMode -Version Latest\r\nWrite-Output "Hello World"'
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = base64.b64encode(expected_script.encode('utf-16-le')).decode('utf-8')
    expected = ' '.join(_common_args + ['-EncodedCommand', encoded_script])
    assert result == expected

def test_encode_script_as_list(shell_module):
    script = 'Write-Output "Hello World"'
    result = shell_module._encode_script(script, as_list=True, strict_mode=True, preserve_rc=True)
    expected_script = 'Set-StrictMode -Version Latest\r\nWrite-Output "Hello World"\r\nIf (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = base64.b64encode(expected_script.encode('utf-16-le')).decode('utf-8')
    expected = _common_args + ['-EncodedCommand', encoded_script]
    assert result == expected
