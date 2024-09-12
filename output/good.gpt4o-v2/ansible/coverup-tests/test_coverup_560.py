# file: lib/ansible/plugins/inventory/ini.py:354-392
# asked: {"lines": [354, 369, 370, 377, 385, 386, 391], "branches": []}
# gained: {"lines": [354, 369, 370, 377, 385, 386, 391], "branches": []}

import pytest
import re
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_compile_patterns(inventory_module):
    inventory_module.patterns = {}
    inventory_module._compile_patterns()

    assert 'section' in inventory_module.patterns
    assert 'groupname' in inventory_module.patterns

    section_pattern = inventory_module.patterns['section']
    groupname_pattern = inventory_module.patterns['groupname']

    assert section_pattern.match('[groupname]')
    assert section_pattern.match('[somegroup:vars]')
    assert section_pattern.match('[naughty:children] # only get coal in their stockings')
    assert not section_pattern.match('groupname')
    assert not section_pattern.match('[groupname')

    assert groupname_pattern.match('groupname')
    assert groupname_pattern.match('groupname # comment')
    assert not groupname_pattern.match('groupname:vars')
    assert not groupname_pattern.match('[groupname]')
