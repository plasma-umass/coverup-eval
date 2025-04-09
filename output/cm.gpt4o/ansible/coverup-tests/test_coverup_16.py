# file lib/ansible/plugins/vars/host_group_vars.py:67-115
# lines [67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115]
# branches ['74->75', '74->77', '80->81', '80->115', '81->82', '81->83', '83->84', '83->86', '89->80', '89->90', '96->97', '96->100', '100->101', '100->108', '101->102', '101->106', '108->80', '108->109', '110->108', '110->111']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.errors import AnsibleParserError
from ansible.inventory.host import Host
from ansible.inventory.group import Group
import os

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_display():
    return MagicMock()

@pytest.fixture
def vars_module(mock_display):
    module = VarsModule()
    module._display = mock_display
    module._basedir = '/fake/base/dir'
    return module

def test_get_vars_with_invalid_entity(vars_module, mock_loader):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(mock_loader, '/fake/path', 'invalid_entity')

def test_get_vars_with_host_entity(vars_module, mock_loader):
    host = Host(name='test_host')
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', return_value=b'/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.to_text', return_value='/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        mock_loader.find_vars_files.return_value = ['/fake/base/dir/host_vars/test_host']
        mock_loader.load_from_file.return_value = {'key': 'value'}
        
        result = vars_module.get_vars(mock_loader, '/fake/path', [host])
        
        assert result == {'key': 'value'}
        mock_loader.find_vars_files.assert_called_once_with('/fake/base/dir/host_vars', 'test_host')
        mock_loader.load_from_file.assert_called_once_with('/fake/base/dir/host_vars/test_host', cache=True, unsafe=True)

def test_get_vars_with_group_entity(vars_module, mock_loader):
    group = Group(name='test_group')
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', return_value=b'/fake/base/dir/group_vars'), \
         patch('ansible.plugins.vars.host_group_vars.to_text', return_value='/fake/base/dir/group_vars'), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        mock_loader.find_vars_files.return_value = ['/fake/base/dir/group_vars/test_group']
        mock_loader.load_from_file.return_value = {'key': 'value'}
        
        result = vars_module.get_vars(mock_loader, '/fake/path', [group])
        
        assert result == {'key': 'value'}
        mock_loader.find_vars_files.assert_called_once_with('/fake/base/dir/group_vars', 'test_group')
        mock_loader.load_from_file.assert_called_once_with('/fake/base/dir/group_vars/test_group', cache=True, unsafe=True)

def test_get_vars_with_nonexistent_path(vars_module, mock_loader):
    host = Host(name='test_host')
    with patch('os.path.exists', return_value=False), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', return_value=b'/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.to_text', return_value='/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        result = vars_module.get_vars(mock_loader, '/fake/path', [host])
        
        assert result == {}
        mock_loader.find_vars_files.assert_not_called()
        mock_loader.load_from_file.assert_not_called()
