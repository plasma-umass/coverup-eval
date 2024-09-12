# file: lib/ansible/plugins/vars/host_group_vars.py:67-115
# asked: {"lines": [75, 97], "branches": [[74, 75], [89, 80], [96, 97], [110, 108]]}
# gained: {"lines": [75, 97], "branches": [[74, 75], [96, 97], [110, 108]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_text
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars

@pytest.fixture
def loader():
    return MagicMock()

@pytest.fixture
def path():
    return "/some/path"

@pytest.fixture
def host():
    return Host(name="test_host")

@pytest.fixture
def group():
    return Group(name="test_group")

@pytest.fixture
def vars_module():
    return VarsModule()

def test_get_vars_single_entity(vars_module, loader, path, host):
    with patch('ansible.plugins.vars.host_group_vars.os.path.exists', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.realpath', return_value=b'/real/path'), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', side_effect=to_bytes), \
         patch('ansible.plugins.vars.host_group_vars.to_text', side_effect=to_text), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(loader, 'find_vars_files', return_value=['/real/path/vars_file']), \
         patch.object(loader, 'load_from_file', return_value={'var1': 'value1'}):
        
        result = vars_module.get_vars(loader, path, host)
        assert result == {'var1': 'value1'}

def test_get_vars_multiple_entities(vars_module, loader, path, host, group):
    with patch('ansible.plugins.vars.host_group_vars.os.path.exists', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.realpath', return_value=b'/real/path'), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', side_effect=to_bytes), \
         patch('ansible.plugins.vars.host_group_vars.to_text', side_effect=to_text), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(loader, 'find_vars_files', return_value=['/real/path/vars_file']), \
         patch.object(loader, 'load_from_file', return_value={'var1': 'value1'}):
        
        result = vars_module.get_vars(loader, path, [host, group])
        assert result == {'var1': 'value1'}

def test_get_vars_cache_hit(vars_module, loader, path, host):
    with patch('ansible.plugins.vars.host_group_vars.os.path.exists', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.realpath', return_value=b'/real/path'), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', side_effect=to_bytes), \
         patch('ansible.plugins.vars.host_group_vars.to_text', side_effect=to_text), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {'test_host./real/path': ['/real/path/vars_file']}), \
         patch.object(loader, 'load_from_file', return_value={'var1': 'value1'}):
        
        result = vars_module.get_vars(loader, path, host)
        assert result == {'var1': 'value1'}

def test_get_vars_empty_file(vars_module, loader, path, host):
    with patch('ansible.plugins.vars.host_group_vars.os.path.exists', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.os.path.realpath', return_value=b'/real/path'), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', side_effect=to_bytes), \
         patch('ansible.plugins.vars.host_group_vars.to_text', side_effect=to_text), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(loader, 'find_vars_files', return_value=['/real/path/vars_file']), \
         patch.object(loader, 'load_from_file', return_value={}):
        
        result = vars_module.get_vars(loader, path, host)
        assert result == {}

def test_get_vars_invalid_entity(vars_module, loader, path):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(loader, path, "invalid_entity")
