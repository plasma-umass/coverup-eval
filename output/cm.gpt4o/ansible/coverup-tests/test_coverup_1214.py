# file lib/ansible/vars/hostvars.py:92-96
# lines [93, 94, 95, 96]
# branches ['94->95', '94->96']

import pytest
from unittest.mock import MagicMock, patch
from ansible.vars.hostvars import HostVars, AnsibleUndefined, HostVarsVars

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_variable_manager():
    return MagicMock()

@pytest.fixture
def hostvars(mock_inventory, mock_variable_manager, mock_loader):
    hv = HostVars(mock_inventory, mock_variable_manager, mock_loader)
    return hv

def test_hostvars_getitem_with_undefined(hostvars):
    host_name = 'undefined_host'
    with patch.object(hostvars, 'raw_get', return_value=AnsibleUndefined()):
        result = hostvars[host_name]
        assert isinstance(result, AnsibleUndefined)

def test_hostvars_getitem_with_defined_data(hostvars):
    host_name = 'defined_host'
    mock_data = {'key': 'value'}
    with patch.object(hostvars, 'raw_get', return_value=mock_data):
        result = hostvars[host_name]
        assert isinstance(result, HostVarsVars)
        assert result._vars == mock_data
        assert result._loader == hostvars._loader
