# file: lib/ansible/plugins/shell/powershell.py:120-133
# asked: {"lines": [123, 124, 125, 126, 128, 132, 133], "branches": [[123, 124], [123, 125]]}
# gained: {"lines": [123, 124, 125, 126, 128, 132, 133], "branches": [[123, 124], [123, 125]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_mkdtemp_no_basefile(shell_module, mocker):
    mocker.patch.object(shell_module.__class__, '_generate_temp_dir_name', return_value='tempdir')
    mocker.patch.object(shell_module, '_escape', return_value='escaped_tempdir')
    mocker.patch.object(shell_module, '_unquote', return_value='unquoted_tempdir')
    mocker.patch.object(shell_module, 'get_option', return_value='remote_tmp')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.mkdtemp()

    assert result == 'encoded_script'
    shell_module.__class__._generate_temp_dir_name.assert_called_once()
    shell_module._escape.assert_called_once_with('unquoted_tempdir')
    shell_module._unquote.assert_called_once_with('tempdir')
    shell_module.get_option.assert_called_once_with('remote_tmp')
    shell_module._encode_script.assert_called_once()

def test_mkdtemp_with_basefile(shell_module, mocker):
    mocker.patch.object(shell_module, '_escape', return_value='escaped_basefile')
    mocker.patch.object(shell_module, '_unquote', return_value='unquoted_basefile')
    mocker.patch.object(shell_module, 'get_option', return_value='remote_tmp')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.mkdtemp(basefile='basefile')

    assert result == 'encoded_script'
    shell_module._escape.assert_called_once_with('unquoted_basefile')
    shell_module._unquote.assert_called_once_with('basefile')
    shell_module.get_option.assert_called_once_with('remote_tmp')
    shell_module._encode_script.assert_called_once()

def test_mkdtemp_with_tmpdir(shell_module, mocker):
    mocker.patch.object(shell_module, '_escape', return_value='escaped_basefile')
    mocker.patch.object(shell_module, '_unquote', return_value='unquoted_basefile')
    mocker.patch.object(shell_module, '_encode_script', return_value='encoded_script')

    result = shell_module.mkdtemp(basefile='basefile', tmpdir='custom_tmpdir')

    assert result == 'encoded_script'
    shell_module._escape.assert_called_once_with('unquoted_basefile')
    shell_module._unquote.assert_called_once_with('basefile')
    shell_module._encode_script.assert_called_once()
