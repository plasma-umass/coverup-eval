# file lib/ansible/plugins/shell/powershell.py:266-287
# lines [268, 270, 271, 274, 275, 278, 279, 280, 281, 282, 283, 285, 286, 287]
# branches ['270->271', '270->274', '274->275', '274->278', '278->279', '278->281', '285->286', '285->287']

import pytest
import base64
from ansible.plugins.shell.powershell import ShellModule

# Mock the _common_args to avoid dependencies on the actual environment
_common_args = ["powershell", "-NoProfile", "-NonInteractive"]

# Test function to cover lines 268-287
def test_encode_script(mocker):
    # Patch the ShellModule to include the mocked _common_args
    mocker.patch('ansible.plugins.shell.powershell._common_args', new=_common_args)
    shell_module = ShellModule()

    # Test with strict_mode and preserve_rc set to True
    script = "Write-Host 'Hello, World!'"
    encoded_script = shell_module._encode_script(script)
    assert isinstance(encoded_script, str)
    assert "powershell" in encoded_script
    assert "-EncodedCommand" in encoded_script
    decoded_script = base64.b64decode(encoded_script.split()[-1]).decode('utf-16-le')
    assert "Set-StrictMode -Version Latest" in decoded_script
    assert "If (-not $?) {" in decoded_script

    # Test with strict_mode set to False
    encoded_script_no_strict = shell_module._encode_script(script, strict_mode=False)
    decoded_script_no_strict = base64.b64decode(encoded_script_no_strict.split()[-1]).decode('utf-16-le')
    assert "Set-StrictMode -Version Latest" not in decoded_script_no_strict

    # Test with preserve_rc set to False
    encoded_script_no_preserve = shell_module._encode_script(script, preserve_rc=False)
    decoded_script_no_preserve = base64.b64decode(encoded_script_no_preserve.split()[-1]).decode('utf-16-le')
    assert "If (-not $?) {" not in decoded_script_no_preserve

    # Test with as_list set to True
    cmd_parts_list = shell_module._encode_script(script, as_list=True)
    assert isinstance(cmd_parts_list, list)
    assert "powershell" in cmd_parts_list
    assert "-EncodedCommand" in cmd_parts_list

    # Test with script set to '-'
    cmd_parts_dash = shell_module._encode_script('-', as_list=True)
    assert cmd_parts_dash == _common_args + ['-Command', '-']
