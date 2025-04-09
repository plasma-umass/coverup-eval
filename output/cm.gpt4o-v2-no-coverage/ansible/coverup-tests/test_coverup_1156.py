# file: lib/ansible/plugins/vars/host_group_vars.py:67-115
# asked: {"lines": [75, 97, 113, 114], "branches": [[74, 75], [89, 80], [96, 97], [110, 108]]}
# gained: {"lines": [75, 113, 114], "branches": [[74, 75]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars import BaseVarsPlugin
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars
from ansible.plugins.vars.host_group_vars import VarsModule

class TestVarsModule:
    
    @pytest.fixture
    def vars_module(self):
        return VarsModule()
    
    @pytest.fixture
    def mock_loader(self):
        return MagicMock()
    
    @pytest.fixture
    def mock_host(self):
        host = MagicMock(spec=Host)
        host.name = "test_host"
        return host
    
    @pytest.fixture
    def mock_group(self):
        group = MagicMock(spec=Group)
        group.name = "test_group"
        return group
    
    @patch('ansible.plugins.vars.host_group_vars.os.path.exists')
    @patch('ansible.plugins.vars.host_group_vars.os.path.isdir')
    @patch('ansible.plugins.vars.host_group_vars.os.path.realpath')
    @patch('ansible.plugins.vars.host_group_vars.to_bytes')
    @patch('ansible.plugins.vars.host_group_vars.to_text')
    def test_get_vars_host(self, mock_to_text, mock_to_bytes, mock_realpath, mock_isdir, mock_exists, vars_module, mock_loader, mock_host):
        mock_to_bytes.return_value = b'/mocked/path/host_vars'
        mock_realpath.return_value = b'/mocked/path/host_vars'
        mock_to_text.return_value = '/mocked/path/host_vars'
        mock_exists.return_value = True
        mock_isdir.return_value = True
        mock_loader.find_vars_files.return_value = ['file1', 'file2']
        mock_loader.load_from_file.side_effect = [{'var1': 'value1'}, {'var2': 'value2'}]
        
        vars_module._basedir = '/mocked/path'
        vars_module._display = MagicMock()
        
        result = vars_module.get_vars(mock_loader, '/mocked/path', [mock_host])
        
        assert result == {'var1': 'value1', 'var2': 'value2'}
        mock_loader.find_vars_files.assert_called_once_with('/mocked/path/host_vars', 'test_host')
        mock_loader.load_from_file.assert_any_call('file1', cache=True, unsafe=True)
        mock_loader.load_from_file.assert_any_call('file2', cache=True, unsafe=True)
    
    @patch('ansible.plugins.vars.host_group_vars.os.path.exists')
    @patch('ansible.plugins.vars.host_group_vars.os.path.isdir')
    @patch('ansible.plugins.vars.host_group_vars.os.path.realpath')
    @patch('ansible.plugins.vars.host_group_vars.to_bytes')
    @patch('ansible.plugins.vars.host_group_vars.to_text')
    def test_get_vars_group(self, mock_to_text, mock_to_bytes, mock_realpath, mock_isdir, mock_exists, vars_module, mock_loader, mock_group):
        mock_to_bytes.return_value = b'/mocked/path/group_vars'
        mock_realpath.return_value = b'/mocked/path/group_vars'
        mock_to_text.return_value = '/mocked/path/group_vars'
        mock_exists.return_value = True
        mock_isdir.return_value = True
        mock_loader.find_vars_files.return_value = ['file1', 'file2']
        mock_loader.load_from_file.side_effect = [{'var1': 'value1'}, {'var2': 'value2'}]
        
        vars_module._basedir = '/mocked/path'
        vars_module._display = MagicMock()
        
        result = vars_module.get_vars(mock_loader, '/mocked/path', [mock_group])
        
        assert result == {'var1': 'value1', 'var2': 'value2'}
        mock_loader.find_vars_files.assert_called_once_with('/mocked/path/group_vars', 'test_group')
        mock_loader.load_from_file.assert_any_call('file1', cache=True, unsafe=True)
        mock_loader.load_from_file.assert_any_call('file2', cache=True, unsafe=True)
    
    def test_get_vars_invalid_entity(self, vars_module, mock_loader):
        with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
            vars_module.get_vars(mock_loader, '/mocked/path', "invalid_entity")
    
    @patch('ansible.plugins.vars.host_group_vars.os.path.exists')
    @patch('ansible.plugins.vars.host_group_vars.os.path.isdir')
    @patch('ansible.plugins.vars.host_group_vars.os.path.realpath')
    @patch('ansible.plugins.vars.host_group_vars.to_bytes')
    @patch('ansible.plugins.vars.host_group_vars.to_text')
    def test_get_vars_exception_handling(self, mock_to_text, mock_to_bytes, mock_realpath, mock_isdir, mock_exists, vars_module, mock_loader, mock_host):
        mock_to_bytes.return_value = b'/mocked/path/host_vars'
        mock_realpath.return_value = b'/mocked/path/host_vars'
        mock_to_text.return_value = '/mocked/path/host_vars'
        mock_exists.return_value = True
        mock_isdir.return_value = True
        mock_loader.find_vars_files.side_effect = Exception("Test exception")
        
        vars_module._basedir = '/mocked/path'
        vars_module._display = MagicMock()
        
        with pytest.raises(AnsibleParserError, match="Test exception"):
            vars_module.get_vars(mock_loader, '/mocked/path', [mock_host])
