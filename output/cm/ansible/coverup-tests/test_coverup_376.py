# file lib/ansible/inventory/data.py:245-256
# lines [245, 248, 249, 250, 251, 253, 255, 256]
# branches ['248->249', '248->250', '250->251', '250->253']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.data import InventoryData
from ansible.inventory.group import Group
from ansible.inventory.host import Host
from ansible.utils.display import Display

# Mock the display object to prevent actual printing
@pytest.fixture
def mock_display(mocker):
    mock = mocker.patch('ansible.inventory.data.display', new_callable=Display)
    mock.debug = mocker.MagicMock()
    return mock

# Test function to cover setting variable for a group
def test_set_variable_for_group(mock_display):
    inventory_data = InventoryData()
    group_name = 'test_group'
    varname = 'test_var'
    value = 'test_value'
    
    # Create a group and add it to the inventory
    test_group = Group(name=group_name)
    inventory_data.groups[group_name] = test_group
    
    # Set variable for the group
    inventory_data.set_variable(group_name, varname, value)
    
    # Assert the variable was set correctly
    assert test_group.get_vars()[varname] == value
    mock_display.debug.assert_called_with('set %s for %s' % (varname, group_name))

# Test function to cover setting variable for a host
def test_set_variable_for_host(mock_display):
    inventory_data = InventoryData()
    host_name = 'test_host'
    varname = 'test_var'
    value = 'test_value'
    
    # Create a host and add it to the inventory
    test_host = Host(name=host_name)
    inventory_data.hosts[host_name] = test_host
    
    # Set variable for the host
    inventory_data.set_variable(host_name, varname, value)
    
    # Assert the variable was set correctly
    assert test_host.get_vars()[varname] == value
    mock_display.debug.assert_called_with('set %s for %s' % (varname, host_name))

# Test function to cover the error case when entity is neither a group nor a host
def test_set_variable_for_unknown_entity():
    inventory_data = InventoryData()
    entity = 'unknown_entity'
    varname = 'test_var'
    value = 'test_value'
    
    # Attempt to set variable for an unknown entity and assert that it raises an error
    with pytest.raises(AnsibleError) as excinfo:
        inventory_data.set_variable(entity, varname, value)
    assert "Could not identify group or host named %s" % entity in str(excinfo.value)
