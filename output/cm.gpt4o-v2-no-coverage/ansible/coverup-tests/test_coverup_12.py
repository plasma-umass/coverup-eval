# file: lib/ansible/plugins/vars/host_group_vars.py:67-115
# asked: {"lines": [67, 69, 71, 74, 75, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 113, 114, 115], "branches": [[74, 75], [74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 80], [89, 90], [96, 97], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 108], [110, 111]]}
# gained: {"lines": [67, 69, 71, 74, 77, 79, 80, 81, 82, 83, 84, 86, 89, 90, 91, 93, 94, 95, 96, 100, 101, 102, 103, 104, 106, 108, 109, 110, 111, 115], "branches": [[74, 77], [80, 81], [80, 115], [81, 82], [81, 83], [83, 84], [83, 86], [89, 90], [96, 100], [100, 101], [100, 108], [101, 102], [101, 106], [108, 80], [108, 109], [110, 111]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.plugins.vars.host_group_vars import VarsModule
from ansible.inventory.host import Host
from ansible.inventory.group import Group
from ansible.utils.vars import combine_vars

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_host():
    host = MagicMock(spec=Host)
    host.name = "test_host"
    return host

@pytest.fixture
def mock_group():
    group = MagicMock(spec=Group)
    group.name = "test_group"
    return group

@pytest.fixture
def vars_module():
    module = VarsModule()
    module._basedir = "/test_basedir"
    module._display = MagicMock()
    return module

def test_get_vars_with_host(vars_module, mock_loader, mock_host):
    with patch("os.path.realpath", return_value=b"/test_basedir/host_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}), \
         patch.object(mock_loader, "find_vars_files", return_value=["/test_basedir/host_vars/test_host.yml"]), \
         patch.object(mock_loader, "load_from_file", return_value={"key": "value"}):
        
        result = vars_module.get_vars(mock_loader, "/test_path", [mock_host])
        assert result == {"key": "value"}
        mock_loader.find_vars_files.assert_called_once_with("/test_basedir/host_vars", "test_host")
        mock_loader.load_from_file.assert_called_once_with("/test_basedir/host_vars/test_host.yml", cache=True, unsafe=True)

def test_get_vars_with_group(vars_module, mock_loader, mock_group):
    with patch("os.path.realpath", return_value=b"/test_basedir/group_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}), \
         patch.object(mock_loader, "find_vars_files", return_value=["/test_basedir/group_vars/test_group.yml"]), \
         patch.object(mock_loader, "load_from_file", return_value={"key": "value"}):
        
        result = vars_module.get_vars(mock_loader, "/test_path", [mock_group])
        assert result == {"key": "value"}
        mock_loader.find_vars_files.assert_called_once_with("/test_basedir/group_vars", "test_group")
        mock_loader.load_from_file.assert_called_once_with("/test_basedir/group_vars/test_group.yml", cache=True, unsafe=True)

def test_get_vars_with_invalid_entity(vars_module, mock_loader):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(mock_loader, "/test_path", ["invalid_entity"])

def test_get_vars_with_nonexistent_path(vars_module, mock_loader, mock_host):
    with patch("os.path.realpath", return_value=b"/test_basedir/host_vars"), \
         patch("os.path.exists", return_value=False), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}):
        
        result = vars_module.get_vars(mock_loader, "/test_path", [mock_host])
        assert result == {}
        mock_loader.find_vars_files.assert_not_called()
        mock_loader.load_from_file.assert_not_called()

def test_get_vars_with_non_directory_path(vars_module, mock_loader, mock_host):
    with patch("os.path.realpath", return_value=b"/test_basedir/host_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=False), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}):
        
        result = vars_module.get_vars(mock_loader, "/test_path", [mock_host])
        assert result == {}
        vars_module._display.warning.assert_called_once_with("Found host_vars that is not a directory, skipping: /test_basedir/host_vars")
        mock_loader.find_vars_files.assert_not_called()
        mock_loader.load_from_file.assert_not_called()
