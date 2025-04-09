# file: lib/ansible/plugins/inventory/ini.py:354-392
# asked: {"lines": [354, 369, 370, 377, 385, 386, 391], "branches": []}
# gained: {"lines": [354, 369, 370, 377, 385, 386, 391], "branches": []}

import pytest
import re
from ansible.plugins.inventory.ini import InventoryModule
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text

@pytest.fixture
def inventory_module():
    return InventoryModule()

def test_compile_patterns_section(inventory_module):
    inventory_module.patterns = {}
    inventory_module._compile_patterns()
    
    section_pattern = inventory_module.patterns['section']
    assert section_pattern.match('[groupname]')
    assert section_pattern.match('[somegroup:vars]')
    assert section_pattern.match('[naughty:children] # only get coal in their stockings')
    assert not section_pattern.match('[invalid group name]')
    assert not section_pattern.match('[groupname:invalid tag] extra text')

def test_compile_patterns_groupname(inventory_module):
    inventory_module.patterns = {}
    inventory_module._compile_patterns()
    
    groupname_pattern = inventory_module.patterns['groupname']
    assert groupname_pattern.match('groupname')
    assert groupname_pattern.match('groupname # with comment')
    assert not groupname_pattern.match('invalid group name')
    assert not groupname_pattern.match('groupname:invalid tag')

@pytest.fixture(autouse=True)
def cleanup_patterns(inventory_module):
    yield
    inventory_module.patterns = {}

