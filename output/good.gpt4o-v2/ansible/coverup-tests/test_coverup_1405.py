# file: lib/ansible/cli/inventory.py:266-282
# asked: {"lines": [], "branches": [[273, 279], [276, 274]]}
# gained: {"lines": [], "branches": [[276, 274]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def mock_group():
    group = MagicMock()
    group.name = 'test_group'
    group.child_groups = []
    group.hosts = []
    return group

@pytest.fixture
def mock_host():
    host = MagicMock()
    host.name = 'test_host'
    return host

@pytest.fixture
def mock_context():
    with patch('ansible.context.CLIARGS', {'show_vars': True, 'export': False, 'basedir': None}):
        yield

def test_graph_group_with_show_vars(mock_group, mock_host, mock_context):
    cli = InventoryCLI(MagicMock())
    mock_group.hosts = [mock_host]
    
    with patch.object(cli, '_graph_name', return_value='graph_name') as mock_graph_name, \
         patch.object(cli, '_show_vars', return_value=['var1', 'var2']) as mock_show_vars, \
         patch.object(cli, '_get_host_variables', return_value={'var': 'value'}) as mock_get_host_vars, \
         patch.object(cli, '_get_group_variables', return_value={'group_var': 'group_value'}) as mock_get_group_vars:
        
        result = cli._graph_group(mock_group)
        
        assert mock_graph_name.call_count == 2
        assert mock_show_vars.call_count == 2
        assert mock_get_host_vars.call_count == 1
        assert mock_get_group_vars.call_count == 1
        assert 'graph_name' in result
        assert 'var1' in result
        assert 'var2' in result

def test_graph_group_without_show_vars(mock_group, mock_host):
    with patch('ansible.context.CLIARGS', {'show_vars': False, 'export': False, 'basedir': None}):
        cli = InventoryCLI(MagicMock())
        mock_group.hosts = [mock_host]
        
        with patch.object(cli, '_graph_name', return_value='graph_name') as mock_graph_name, \
             patch.object(cli, '_show_vars', return_value=['var1', 'var2']) as mock_show_vars, \
             patch.object(cli, '_get_host_variables', return_value={'var': 'value'}) as mock_get_host_vars, \
             patch.object(cli, '_get_group_variables', return_value={'group_var': 'group_value'}) as mock_get_group_vars:
            
            result = cli._graph_group(mock_group)
            
            assert mock_graph_name.call_count == 2
            assert mock_show_vars.call_count == 0
            assert mock_get_host_vars.call_count == 0
            assert mock_get_group_vars.call_count == 0
            assert 'graph_name' in result
