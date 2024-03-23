# file lib/ansible/plugins/inventory/ini.py:318-334
# lines [324, 326, 327, 328, 329, 331, 332, 334]
# branches ['326->327', '326->329', '329->331', '329->334', '331->329', '331->332']

import pytest
from ansible.errors import AnsibleParserError
from ansible.plugins.inventory.ini import InventoryModule

def test_expand_hostpattern_with_colon(mocker):
    # Mock the parent class method to return a specific value
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin._expand_hostpattern', return_value=(['testhost'], None))
    
    inventory_module = InventoryModule()

    # Test with a host pattern ending with ':'
    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module._expand_hostpattern('testhost:')
    assert "ending in ':' is not allowed" in str(excinfo.value)

def test_expand_hostpattern_with_yaml_indicator(mocker):
    # Mock the parent class method to return a specific value
    mocker.patch('ansible.plugins.inventory.ini.BaseFileInventoryPlugin._expand_hostpattern', return_value=(['---'], None))
    
    inventory_module = InventoryModule()

    # Test with a host pattern that is '---'
    with pytest.raises(AnsibleParserError) as excinfo:
        inventory_module._expand_hostpattern('---')
    assert "is normally a sign this is a YAML file" in str(excinfo.value)
