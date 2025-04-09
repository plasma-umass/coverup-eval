# file lib/ansible/plugins/loader.py:69-99
# lines [81, 82]
# branches ['77->92', '85->92', '86->85']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import shell_loader

# Mocking string_types for compatibility with different Python versions
try:
    string_types = (str, unicode)
except NameError:
    string_types = (str,)

def test_get_shell_plugin_with_executable_string(mocker):
    from ansible.plugins.loader import get_shell_plugin

    mocker.patch('os.path.basename', return_value='bash')
    mock_shell_loader_get = mocker.patch.object(shell_loader, 'get', side_effect=[None, MagicMock(SHELL_FAMILY='sh', COMPATIBLE_SHELLS=['bash'])])
    mock_shell_loader_all = mocker.patch.object(shell_loader, 'all', return_value=[MagicMock(SHELL_FAMILY='sh', COMPATIBLE_SHELLS=['bash'])])

    shell = get_shell_plugin(executable='/bin/bash')

    assert shell is not None
    assert shell.SHELL_FAMILY == 'sh'
    assert shell.executable == '/bin/bash'
    mock_shell_loader_get.assert_called_with('sh')
    mock_shell_loader_all.assert_called_once()

def test_get_shell_plugin_with_invalid_executable(mocker):
    from ansible.plugins.loader import get_shell_plugin

    mocker.patch('os.path.basename', return_value='invalid_shell')
    mock_shell_loader_get = mocker.patch.object(shell_loader, 'get', side_effect=[Exception, None])
    mock_shell_loader_all = mocker.patch.object(shell_loader, 'all', return_value=[])

    with pytest.raises(AnsibleError, match="Could not find the shell plugin required"):
        get_shell_plugin(executable='/bin/invalid_shell')

    mock_shell_loader_get.assert_any_call('invalid_shell')
    mock_shell_loader_get.assert_any_call('sh')
    mock_shell_loader_all.assert_called_once()
