# file: lib/ansible/vars/manager.py:80-108
# asked: {"lines": [104, 107, 108], "branches": []}
# gained: {"lines": [104, 107, 108], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.vars.manager import VariableManager

@pytest.fixture
def mock_loader():
    return MagicMock()

@pytest.fixture
def mock_inventory():
    return MagicMock()

@pytest.fixture
def mock_version_info():
    return MagicMock()

def test_fact_cache_initialization_with_error(mock_loader, mock_inventory, mock_version_info):
    with patch('ansible.vars.manager.FactCache', side_effect=AnsibleError("Test Error")) as mock_fact_cache, \
         patch('ansible.vars.manager.display.warning') as mock_warning:
        vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
        mock_fact_cache.assert_called_once()
        mock_warning.assert_called_once_with("Test Error")
        assert vm._fact_cache == {}

def test_fact_cache_initialization_success(mock_loader, mock_inventory, mock_version_info):
    with patch('ansible.vars.manager.FactCache') as mock_fact_cache:
        vm = VariableManager(loader=mock_loader, inventory=mock_inventory, version_info=mock_version_info)
        mock_fact_cache.assert_called_once()
        assert isinstance(vm._fact_cache, MagicMock)
