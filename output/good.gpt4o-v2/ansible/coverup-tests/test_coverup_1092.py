# file: lib/ansible/cli/inventory.py:328-363
# asked: {"lines": [330, 332, 333, 336, 339, 340, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 354, 355, 356, 357, 359, 361, 363], "branches": [[340, 341], [340, 345], [341, 340], [341, 342], [346, 347], [346, 354], [347, 348], [347, 354], [349, 350], [349, 352], [354, 355], [354, 359], [356, 357], [356, 359]]}
# gained: {"lines": [330, 332, 333, 336, 339, 340, 341, 342, 345, 346, 347, 348, 349, 350, 351, 352, 354, 355, 356, 357, 359, 361, 363], "branches": [[340, 341], [340, 345], [341, 342], [346, 347], [347, 348], [347, 354], [349, 350], [354, 355], [356, 357]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.inventory import InventoryCLI

@pytest.fixture
def mock_context():
    with patch('ansible.context.CLIARGS', {'export': True, 'basedir': None}):
        yield

@pytest.fixture
def inventory_cli():
    return InventoryCLI(args=['test'])

def test_yaml_inventory(mock_context, inventory_cli):
    # Mocking the group and host objects
    host1 = MagicMock()
    host1.name = 'host1'
    host1.get_vars.return_value = {'var1': 'value1'}

    host2 = MagicMock()
    host2.name = 'host2'
    host2.get_vars.return_value = {'var2': 'value2'}

    subgroup = MagicMock()
    subgroup.name = 'subgroup'
    subgroup.child_groups = []
    subgroup.hosts = [host2]
    subgroup.get_vars.return_value = {'subvar': 'subvalue'}

    top_group = MagicMock()
    top_group.name = 'top'
    top_group.child_groups = [subgroup]
    top_group.hosts = [host1]
    top_group.get_vars.return_value = {'topvar': 'topvalue'}

    inventory_cli._get_host_variables = MagicMock(side_effect=lambda host: host.get_vars())
    inventory_cli._get_group_variables = MagicMock(side_effect=lambda group: group.get_vars())
    inventory_cli._remove_empty = MagicMock()

    result = inventory_cli.yaml_inventory(top_group)

    expected_result = {
        'top': {
            'children': {
                'subgroup': {
                    'children': {},
                    'hosts': {
                        'host2': {'var2': 'value2'}
                    },
                    'vars': {'subvar': 'subvalue'}
                }
            },
            'hosts': {
                'host1': {'var1': 'value1'}
            },
            'vars': {'topvar': 'topvalue'}
        }
    }

    assert result == expected_result
    inventory_cli._remove_empty.assert_called()
