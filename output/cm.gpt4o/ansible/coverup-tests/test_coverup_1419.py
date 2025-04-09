# file lib/ansible/plugins/vars/host_group_vars.py:67-115
# lines [97, 106, 113, 114]
# branches ['89->80', '96->97', '101->106', '110->108']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.errors import AnsibleParserError
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars

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

def test_get_vars_with_non_list_entities(vars_module, mock_loader):
    host = Host(name='testhost')
    result = vars_module.get_vars(mock_loader, None, host)
    assert isinstance(result, dict)

def test_get_vars_with_invalid_entity(vars_module, mock_loader):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(mock_loader, None, object())

def test_get_vars_with_host_entity(vars_module, mock_loader):
    host = Host(name='testhost')
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=False), \
         patch('os.path.realpath', return_value='/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.to_bytes', return_value=b'/fake/base/dir/host_vars'), \
         patch('ansible.plugins.vars.host_group_vars.to_text', return_value='/fake/base/dir/host_vars'):
        vars_module.get_vars(mock_loader, None, [host])
        vars_module._display.warning.assert_called_with("Found host_vars that is not a directory, skipping: /fake/base/dir/host_vars")

def test_get_vars_with_group_entity(vars_module, mock_loader):
    group = Group(name='testgroup')
    with patch('os.path.exists', return_value=True), \
         patch('os.path.isdir', return_value=True), \
         patch('ansible.plugins.vars.host_group_vars.FOUND', {}), \
         patch.object(mock_loader, 'find_vars_files', return_value=['/fake/vars/file']), \
         patch.object(mock_loader, 'load_from_file', return_value={'key': 'value'}):
        result = vars_module.get_vars(mock_loader, None, [group])
        assert result == {'key': 'value'}

def test_get_vars_with_exception(vars_module, mock_loader):
    host = Host(name='testhost')
    with patch('os.path.exists', side_effect=Exception('Test exception')):
        with pytest.raises(AnsibleParserError, match="Test exception"):
            vars_module.get_vars(mock_loader, None, [host])
