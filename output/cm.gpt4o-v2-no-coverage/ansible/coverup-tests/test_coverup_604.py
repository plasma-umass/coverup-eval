# file: lib/ansible/plugins/inventory/ini.py:256-266
# asked: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}
# gained: {"lines": [256, 262, 263, 264, 266], "branches": [[263, 264], [263, 266]]}

import pytest
import re
from ansible.errors import AnsibleError
from ansible.plugins.inventory.ini import InventoryModule

class MockedInventoryModule(InventoryModule):
    def __init__(self):
        self.patterns = {'groupname': re.compile(r'^\[(.+)\]$')}
        self._filename = 'mocked_file.ini'
        self.lineno = 1

def test_parse_group_name_success():
    inventory = MockedInventoryModule()
    line = "[group1]"
    group_name = inventory._parse_group_name(line)
    assert group_name == "group1"

def test_parse_group_name_failure():
    inventory = MockedInventoryModule()
    line = "not_a_group"
    with pytest.raises(AnsibleError, match="Expected group name, got: not_a_group"):
        inventory._parse_group_name(line)
