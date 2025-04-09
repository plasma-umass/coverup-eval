# file: lib/ansible/plugins/shell/powershell.py:266-287
# asked: {"lines": [266, 268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}
# gained: {"lines": [266, 268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287], "branches": [[270, 271], [270, 274], [274, 275], [274, 278], [278, 279], [278, 281], [285, 286], [285, 287]]}

import pytest
import base64
from ansible.module_utils._text import to_text
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    class MockShellModule(ShellModule):
        _common_args = ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted']
    return MockShellModule()

def test_encode_script_as_list(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, as_list=True)
    assert isinstance(result, list)
    assert '-EncodedCommand' in result

def test_encode_script_as_string(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, as_list=False)
    assert isinstance(result, str)
    assert '-EncodedCommand' in result

def test_encode_script_with_strict_mode(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, strict_mode=True)
    assert 'Set-StrictMode -Version Latest' in base64.b64decode(result.split()[-1]).decode('utf-16-le')

def test_encode_script_without_strict_mode(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, strict_mode=False)
    assert 'Set-StrictMode -Version Latest' not in base64.b64decode(result.split()[-1]).decode('utf-16-le')

def test_encode_script_with_preserve_rc(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, preserve_rc=True)
    decoded_script = base64.b64decode(result.split()[-1]).decode('utf-16-le')
    assert 'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }' in decoded_script

def test_encode_script_without_preserve_rc(shell_module):
    script = "Write-Output 'Hello, World!'"
    result = shell_module._encode_script(script, preserve_rc=False)
    decoded_script = base64.b64decode(result.split()[-1]).decode('utf-16-le')
    assert 'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }' not in decoded_script

def test_encode_script_dash(shell_module):
    script = "-"
    result = shell_module._encode_script(script)
    assert result == 'PowerShell -NoProfile -NonInteractive -ExecutionPolicy Unrestricted -Command -'
