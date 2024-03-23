# file lib/ansible/plugins/shell/powershell.py:148-162
# lines [148, 149, 150, 161, 162]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell():
    return ShellModule()

def test_exists_true(mocker, powershell_shell):
    # Mock the _escape and _unquote methods to return the input as is
    mocker.patch.object(powershell_shell, '_escape', return_value='C:\\path\\exists')
    mocker.patch.object(powershell_shell, '_unquote', return_value='C:\\path\\exists')
    # Mock the _encode_script method to just return the script for testing purposes
    mocker.patch.object(powershell_shell, '_encode_script', side_effect=lambda script: script)

    # Call the exists method with a path that is assumed to exist
    script = powershell_shell.exists('C:\\path\\exists')

    # Check if the script contains the expected lines
    assert "If (Test-Path 'C:\\path\\exists')" in script
    assert "$res = 0;" in script
    assert "Write-Output '$res';" in script
    assert "Exit $res;" in script

def test_exists_false(mocker, powershell_shell):
    # Mock the _escape and _unquote methods to return the input as is
    mocker.patch.object(powershell_shell, '_escape', return_value='C:\\path\\notexists')
    mocker.patch.object(powershell_shell, '_unquote', return_value='C:\\path\\notexists')
    # Mock the _encode_script method to just return the script for testing purposes
    mocker.patch.object(powershell_shell, '_encode_script', side_effect=lambda script: script)

    # Call the exists method with a path that is assumed not to exist
    script = powershell_shell.exists('C:\\path\\notexists')

    # Check if the script contains the expected lines
    assert "If (Test-Path 'C:\\path\\notexists')" in script
    assert "$res = 1;" in script
    assert "Write-Output '$res';" in script
    assert "Exit $res;" in script
