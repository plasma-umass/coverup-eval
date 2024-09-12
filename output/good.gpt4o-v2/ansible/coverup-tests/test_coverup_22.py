# file: lib/ansible/plugins/vars/host_group_vars.py:67-115
# asked: {"lines": [67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115], "branches": [[74, 75], [74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 80], [89, 90], [96, 97], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 108], [110, 111]]}
# gained: {"lines": [67, 69, 71, 74, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115], "branches": [[74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 90], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 111]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_host():
    return Host(name="test_host")

@pytest.fixture
def mock_group():
    return Group(name="test_group")

@pytest.fixture
def vars_module():
    module = VarsModule()
    module._basedir = '/base/dir'
    module._display = MagicMock()
    return module

def test_get_vars_with_host(mock_loader, mock_host, vars_module):
    with patch('os.path.realpath', return_value=b'/real/path/host_vars'), \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        
        mock_loader.find_vars_files.return_value = ['file1']
        mock_loader.load_from_file.return_value = {'key': 'value'}
        
        result = vars_module.get_vars(mock_loader, '/some/path', [mock_host])
        
        assert result == {'key': 'value'}
        vars_module._display.debug.assert_called_with('\tprocessing dir /real/path/host_vars')

def test_get_vars_with_group(mock_loader, mock_group, vars_module):
    with patch('os.path.realpath', return_value=b'/real/path/group_vars'), \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        
        mock_loader.find_vars_files.return_value = ['file1']
        mock_loader.load_from_file.return_value = {'key': 'value'}
        
        result = vars_module.get_vars(mock_loader, '/some/path', [mock_group])
        
        assert result == {'key': 'value'}
        vars_module._display.debug.assert_called_with('\tprocessing dir /real/path/group_vars')

def test_get_vars_with_invalid_entity(mock_loader, vars_module):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(mock_loader, '/some/path', ['invalid_entity'])

def test_get_vars_with_nonexistent_path(mock_loader, mock_host, vars_module):
    with patch('os.path.realpath', return_value=b'/real/path/host_vars'), \
         patch('os.path.exists', return_value=False), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        
        result = vars_module.get_vars(mock_loader, '/some/path', [mock_host])
        
        assert result == {}

def test_get_vars_with_non_directory_path(mock_loader, mock_host, vars_module):
    with patch('os.path.realpath', return_value=b'/real/path/host_vars'), \
         patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=False), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        
        result = vars_module.get_vars(mock_loader, '/some/path', [mock_host])
        
        assert result == {}
        vars_module._display.warning.assert_called_with('Found host_vars that is not a directory, skipping: /real/path/host_vars')

def test_get_vars_with_exception(mock_loader, mock_host, vars_module):
    with patch('os.path.realpath', side_effect=Exception('Test exception')), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        
        with pytest.raises(AnsibleParserError, match="Test exception"):
            vars_module.get_vars(mock_loader, '/some/path', [mock_host])
