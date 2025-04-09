# file: lib/ansible/plugins/vars/host_group_vars.py:67-115
# asked: {"lines": [67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115], "branches": [[74, 75], [74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 80], [89, 90], [96, 97], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 108], [110, 111]]}
# gained: {"lines": [67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115], "branches": [[74, 75], [74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 90], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 111]]}

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
    module._basedir = "/fake/dir"
    return module

def test_get_vars_with_non_list_entities(vars_module, mock_loader):
    entity = Host(name="host1")
    result = vars_module.get_vars(mock_loader, None, entity)
    assert isinstance(result, dict)

def test_get_vars_with_host_entity(vars_module, mock_loader):
    entity = Host(name="host1")
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(mock_loader, 'find_vars_files', return_value=['/fake/dir/host_vars/host1']), \
         patch.object(mock_loader, 'load_from_file', return_value={'key': 'value'}):
        result = vars_module.get_vars(mock_loader, None, [entity])
        assert result == {'key': 'value'}

def test_get_vars_with_group_entity(vars_module, mock_loader):
    entity = Group(name="group1")
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(mock_loader, 'find_vars_files', return_value=['/fake/dir/group_vars/group1']), \
         patch.object(mock_loader, 'load_from_file', return_value={'key': 'value'}):
        result = vars_module.get_vars(mock_loader, None, [entity])
        assert result == {'key': 'value'}

def test_get_vars_with_invalid_entity(vars_module, mock_loader):
    entity = "invalid_entity"
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(mock_loader, None, [entity])

def test_get_vars_with_non_existing_path(vars_module, mock_loader):
    entity = Host(name="host1")
    with patch('os.path.exists', return_value=False), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        result = vars_module.get_vars(mock_loader, None, [entity])
        assert result == {}

def test_get_vars_with_non_directory_path(vars_module, mock_loader):
    entity = Host(name="host1")
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=False), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch('os.path.realpath', return_value='/fake/dir/host_vars'):
        result = vars_module.get_vars(mock_loader, None, [entity])
        assert result == {}
        vars_module._display.warning.assert_called_once_with("Found host_vars that is not a directory, skipping: /fake/dir/host_vars")

def test_get_vars_with_exception(vars_module, mock_loader):
    entity = Host(name="host1")
    with patch('os.path.exists', side_effect=Exception("Test exception")), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}):
        with pytest.raises(AnsibleParserError, match="Test exception"):
            vars_module.get_vars(mock_loader, None, [entity])
