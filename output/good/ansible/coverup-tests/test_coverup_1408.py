# file lib/ansible/plugins/shell/powershell.py:81-88
# lines [83, 88]
# branches []

import ntpath
import pytest
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def powershell_shell():
    return ShellModule()

def test_join_path_with_backslashes(powershell_shell, mocker):
    # Mocking _unquote to just return the value passed to it
    mocker.patch.object(powershell_shell, '_unquote', side_effect=lambda x: x)

    # Test data with backslashes at the start of the second part
    path1 = "C:\\Path\\To"
    path2 = "\\Directory\\File"

    # Expected result should handle the backslashes correctly
    expected_path = ntpath.join(path1, path2.strip('\\'))

    # Call the method under test
    result = powershell_shell.join_path(path1, path2)

    # Assert that the result is as expected
    assert result == expected_path

    # Assert that the mocked _unquote method was called for each argument
    powershell_shell._unquote.assert_has_calls([mocker.call(path1), mocker.call(path2)])
