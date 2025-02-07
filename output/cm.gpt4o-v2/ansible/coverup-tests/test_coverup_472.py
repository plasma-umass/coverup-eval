# file: lib/ansible/plugins/inventory/ini.py:336-352
# asked: {"lines": [336, 337, 342, 343, 346, 348, 349, 351, 352], "branches": []}
# gained: {"lines": [336, 337, 342, 343, 346, 348, 349, 351, 352], "branches": []}

import pytest
from ansible.plugins.inventory.ini import InventoryModule

def test_parse_value_int():
    result = InventoryModule._parse_value("123")
    assert result == 123

def test_parse_value_dict():
    result = InventoryModule._parse_value("{'key': 'value'}")
    assert result == {'key': 'value'}

def test_parse_value_list():
    result = InventoryModule._parse_value("['a', 'b', 'c']")
    assert result == ['a', 'b', 'c']

def test_parse_value_valueerror():
    result = InventoryModule._parse_value("invalid_literal")
    assert result == "invalid_literal"

def test_parse_value_syntaxerror():
    result = InventoryModule._parse_value("{'key': 'value'")
    assert result == "{'key': 'value'"
