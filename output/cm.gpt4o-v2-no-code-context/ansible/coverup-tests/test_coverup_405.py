# file: lib/ansible/plugins/inventory/ini.py:336-352
# asked: {"lines": [336, 337, 342, 343, 346, 348, 349, 351, 352], "branches": []}
# gained: {"lines": [336, 337, 342, 343, 346, 349, 351, 352], "branches": []}

import pytest
import ast
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

@pytest.mark.parametrize("input_value, expected_output", [
    ("123", 123),  # int
    ("{'key': 'value'}", {'key': 'value'}),  # dict
    ("[1, 2, 3]", [1, 2, 3]),  # list
    ("'string'", 'string'),  # string
    ("malformed{dict", "malformed{dict"),  # ValueError
    ("malformed[dict", "malformed[dict"),  # SyntaxError
])
def test_parse_value(input_value, expected_output):
    result = InventoryModule._parse_value(input_value)
    assert result == expected_output

def test_parse_value_cleanup(monkeypatch):
    # Ensure no state pollution
    monkeypatch.undo()
