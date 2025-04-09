# file lib/ansible/plugins/inventory/ini.py:354-392
# lines [369, 370, 377, 385, 386, 391]
# branches []

import pytest
import re
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_compile_patterns(inventory_module):
    inventory_module._compile_patterns()
    section_pattern = inventory_module.patterns['section']
    groupname_pattern = inventory_module.patterns['groupname']

    # Test section pattern
    assert section_pattern.match('[groupname]')
    assert section_pattern.match('[somegroup:vars]')
    assert section_pattern.match('[naughty:children] # only get coal in their stockings')
    assert not section_pattern.match('[invalid group: ] trailing space')
    assert not section_pattern.match('nosection')

    # Test groupname pattern
    assert groupname_pattern.match('groupname')
    assert groupname_pattern.match('somegroup # with comment')
    assert not groupname_pattern.match('invalid group:')
    assert not groupname_pattern.match('')

    # Clean up after test
    del inventory_module.patterns['section']
    del inventory_module.patterns['groupname']
