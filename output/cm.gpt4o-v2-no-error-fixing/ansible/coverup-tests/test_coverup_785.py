# file: lib/ansible/plugins/shell/powershell.py:120-133
# asked: {"lines": [123, 124, 125, 126, 128, 132, 133], "branches": [[123, 124], [123, 125]]}
# gained: {"lines": [123, 124, 125, 126, 128, 132, 133], "branches": [[123, 124], [123, 125]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.shell.powershell import ShellModule

@pytest.fixture
def shell_module():
    return ShellModule()

def test_mkdtemp_no_basefile(shell_module):
    with patch.object(ShellModule, '_generate_temp_dir_name', return_value='temp_dir_name') as mock_generate_temp_dir_name, \
         patch.object(shell_module, '_escape', return_value='escaped_temp_dir_name') as mock_escape, \
         patch.object(shell_module, '_unquote', return_value='unquoted_temp_dir_name') as mock_unquote, \
         patch.object(shell_module, 'get_option', return_value='remote_tmp_dir') as mock_get_option, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        
        result = shell_module.mkdtemp()
        
        mock_generate_temp_dir_name.assert_called_once()
        mock_unquote.assert_called_once_with('temp_dir_name')
        mock_escape.assert_called_once_with('unquoted_temp_dir_name')
        mock_get_option.assert_called_once_with('remote_tmp')
        mock_encode_script.assert_called_once()
        
        assert result == 'encoded_script'

def test_mkdtemp_with_basefile(shell_module):
    with patch.object(shell_module, '_escape', return_value='escaped_basefile') as mock_escape, \
         patch.object(shell_module, '_unquote', return_value='unquoted_basefile') as mock_unquote, \
         patch.object(shell_module, 'get_option', return_value='remote_tmp_dir') as mock_get_option, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        
        result = shell_module.mkdtemp(basefile='basefile')
        
        mock_unquote.assert_called_once_with('basefile')
        mock_escape.assert_called_once_with('unquoted_basefile')
        mock_get_option.assert_called_once_with('remote_tmp')
        mock_encode_script.assert_called_once()
        
        assert result == 'encoded_script'

def test_mkdtemp_with_tmpdir(shell_module):
    with patch.object(shell_module, '_escape', return_value='escaped_basefile') as mock_escape, \
         patch.object(shell_module, '_unquote', return_value='unquoted_basefile') as mock_unquote, \
         patch.object(shell_module, '_encode_script', return_value='encoded_script') as mock_encode_script:
        
        result = shell_module.mkdtemp(basefile='basefile', tmpdir='custom_tmpdir')
        
        mock_unquote.assert_called_once_with('basefile')
        mock_escape.assert_called_once_with('unquoted_basefile')
        mock_encode_script.assert_called_once()
        
        assert result == 'encoded_script'
