# file lib/ansible/plugins/shell/powershell.py:266-287
# lines [268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287]
# branches ['270->271', '270->274', '274->275', '274->278', '278->279', '278->281', '285->286', '285->287']

import pytest
from ansible.plugins.shell.powershell import ShellModule
from ansible.module_utils._text import to_text
import base64

@pytest.fixture
def shell_module():
    class TestShellModule(ShellModule):
        _common_args = ['PowerShell', '-NoProfile', '-NonInteractive', '-ExecutionPolicy', 'Unrestricted']
    return TestShellModule()

def test_encode_script_with_dash(shell_module):
    script = '-'
    result = shell_module._encode_script(script)
    assert result == ' '.join(shell_module._common_args + ['-Command', '-'])

def test_encode_script_with_strict_mode_and_preserve_rc(shell_module):
    script = 'Write-Output "Hello, World!"'
    result = shell_module._encode_script(script, strict_mode=True, preserve_rc=True)
    expected_script = (
        'Set-StrictMode -Version Latest\r\n'
        'Write-Output "Hello, World!"\r\n'
        'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    )
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = to_text(base64.b64encode(expected_script.encode('utf-16-le')), 'utf-8')
    expected_result = ' '.join(shell_module._common_args + ['-EncodedCommand', encoded_script])
    assert result == expected_result

def test_encode_script_without_strict_mode(shell_module):
    script = 'Write-Output "Hello, World!"'
    result = shell_module._encode_script(script, strict_mode=False, preserve_rc=True)
    expected_script = (
        'Write-Output "Hello, World!"\r\n'
        'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    )
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = to_text(base64.b64encode(expected_script.encode('utf-16-le')), 'utf-8')
    expected_result = ' '.join(shell_module._common_args + ['-EncodedCommand', encoded_script])
    assert result == expected_result

def test_encode_script_as_list(shell_module):
    script = 'Write-Output "Hello, World!"'
    result = shell_module._encode_script(script, as_list=True, strict_mode=True, preserve_rc=True)
    expected_script = (
        'Set-StrictMode -Version Latest\r\n'
        'Write-Output "Hello, World!"\r\n'
        'If (-not $?) { If (Get-Variable LASTEXITCODE -ErrorAction SilentlyContinue) { exit $LASTEXITCODE } Else { exit 1 } }\r\n'
    )
    expected_script = '\n'.join([x.strip() for x in expected_script.splitlines() if x.strip()])
    encoded_script = to_text(base64.b64encode(expected_script.encode('utf-16-le')), 'utf-8')
    expected_result = shell_module._common_args + ['-EncodedCommand', encoded_script]
    assert result == expected_result
