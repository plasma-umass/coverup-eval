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
def loader():
    return MagicMock()

@pytest.fixture
def path():
    return "/some/path"

@pytest.fixture
def host():
    host = Host(name="testhost")
    return host

@pytest.fixture
def group():
    group = Group(name="testgroup")
    return group

@pytest.fixture
def vars_module():
    return VarsModule()

def test_get_vars_with_host(vars_module, loader, path, host):
    with patch("os.path.realpath", return_value=b"/real/path/host_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}), \
         patch.object(loader, "find_vars_files", return_value=["/real/path/host_vars/testhost"]), \
         patch.object(loader, "load_from_file", return_value={"key": "value"}):
        
        data = vars_module.get_vars(loader, path, [host])
        assert data == {"key": "value"}

def test_get_vars_with_group(vars_module, loader, path, group):
    with patch("os.path.realpath", return_value=b"/real/path/group_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=True), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}), \
         patch.object(loader, "find_vars_files", return_value=["/real/path/group_vars/testgroup"]), \
         patch.object(loader, "load_from_file", return_value={"key": "value"}):
        
        data = vars_module.get_vars(loader, path, [group])
        assert data == {"key": "value"}

def test_get_vars_with_invalid_entity(vars_module, loader, path):
    with pytest.raises(AnsibleParserError, match="Supplied entity must be Host or Group"):
        vars_module.get_vars(loader, path, ["invalid_entity"])

def test_get_vars_with_nonexistent_path(vars_module, loader, path, host):
    with patch("os.path.realpath", return_value=b"/real/path/host_vars"), \
         patch("os.path.exists", return_value=False):
        
        data = vars_module.get_vars(loader, path, [host])
        assert data == {}

def test_get_vars_with_non_directory_path(vars_module, loader, path, host):
    with patch("os.path.realpath", return_value=b"/real/path/host_vars"), \
         patch("os.path.exists", return_value=True), \
         patch("os.path.isdir", return_value=False), \
         patch("ansible.plugins.vars.host_group_vars.FOUND", {}), \
         patch.object(vars_module._display, "warning") as mock_warning:
        
        data = vars_module.get_vars(loader, path, [host])
        assert data == {}
        mock_warning.assert_called_once_with("Found host_vars that is not a directory, skipping: /real/path/host_vars")

def test_get_vars_with_exception(vars_module, loader, path, host):
    with patch("os.path.realpath", return_value=b"/real/path/host_vars"), \
         patch("os.path.exists", side_effect=Exception("Test exception")):
        
        with pytest.raises(AnsibleParserError, match="Test exception"):
            vars_module.get_vars(loader, path, [host])
