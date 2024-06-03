# file lib/ansible/plugins/shell/powershell.py:266-287
# lines []
# branches ['278->281']

import pytest
import base64
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def decode_base64_ps_command(encoded_command):
    encoded_part = encoded_command.split('-EncodedCommand ')[1]
    decoded_bytes = base64.b64decode(encoded_part)
    return decoded_bytes.decode('utf-16-le')

def test_encode_script_with_preserve_rc(shell_module):
    script = "Write-Output 'Hello World'"
    encoded_command = shell_module._encode_script(script, as_list=False, strict_mode=True, preserve_rc=True)
    decoded_command = decode_base64_ps_command(encoded_command)
    
    assert "Set-StrictMode -Version Latest" in decoded_command
    assert "If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }" in decoded_command
    assert "Write-Output 'Hello World'" in decoded_command

def test_encode_script_without_preserve_rc(shell_module):
    script = "Write-Output 'Hello World'"
    encoded_command = shell_module._encode_script(script, as_list=False, strict_mode=True, preserve_rc=False)
    decoded_command = decode_base64_ps_command(encoded_command)
    
    assert "Set-StrictMode -Version Latest" in decoded_command
    assert "If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }" not in decoded_command
    assert "Write-Output 'Hello World'" in decoded_command
