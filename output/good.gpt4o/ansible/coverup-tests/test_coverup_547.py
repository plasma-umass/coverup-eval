# file lib/ansible/cli/inventory.py:284-290
# lines [284, 286, 287, 288, 290]
# branches ['287->288', '287->290']

import pytest
from ansible.cli.inventory import InventoryCLI
from ansible.errors import AnsibleOptionsError
from unittest.mock import patch

@pytest.fixture
def mock_cliargs():
    with patch('ansible.cli.inventory.context.CLIARGS', {'pattern': 'all'}):
        yield

@pytest.fixture
def mock_get_group():
    with patch.object(InventoryCLI, '_get_group', return_value='all') as mock_method:
        yield mock_method

@pytest.fixture
def mock_graph_group():
    with patch.object(InventoryCLI, '_graph_group', return_value=['group1', 'group2']) as mock_method:
        yield mock_method

def test_inventory_graph_valid_group(mock_cliargs, mock_get_group, mock_graph_group):
    cli = InventoryCLI(args=['inventory'])
    result = cli.inventory_graph()
    assert result == 'group1\ngroup2'
    mock_get_group.assert_called_once_with('all')
    mock_graph_group.assert_called_once_with('all')

def test_inventory_graph_invalid_group(mock_cliargs):
    with patch.object(InventoryCLI, '_get_group', return_value=None):
        cli = InventoryCLI(args=['inventory'])
        with pytest.raises(AnsibleOptionsError, match="Pattern must be valid group name when using --graph"):
            cli.inventory_graph()
