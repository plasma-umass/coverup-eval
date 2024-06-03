# file lib/ansible/plugins/shell/powershell.py:60-76
# lines [60, 65, 67, 69, 70, 73]
# branches []

import pytest
from ansible.plugins.shell.powershell import ShellModule

def test_shell_module_attributes():
    shell_module = ShellModule()
    
    # Verify the class attributes
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS is True

@pytest.fixture
def mock_shell_module(mocker):
    mocker.patch('ansible.plugins.shell.powershell.ShellModule', autospec=True)
    yield
    mocker.stopall()

def test_shell_module_with_mock(mock_shell_module):
    shell_module = ShellModule()
    
    # Verify the class attributes with mock
    assert shell_module.COMPATIBLE_SHELLS == frozenset()
    assert shell_module.SHELL_FAMILY == 'powershell'
    assert shell_module._SHELL_REDIRECT_ALLNULL == '> $null'
    assert shell_module._SHELL_AND == ';'
    assert shell_module._IS_WINDOWS is True
