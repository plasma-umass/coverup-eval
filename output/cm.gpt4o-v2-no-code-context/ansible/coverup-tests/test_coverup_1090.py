# file: lib/ansible/plugins/inventory/ini.py:336-352
# asked: {"lines": [348], "branches": []}
# gained: {"lines": [348], "branches": []}

import pytest
import ast
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

class TestInventoryModule:
    @pytest.mark.parametrize("input_value, expected_output", [
        ("123", 123),  # int
        ("{'key': 'value'}", {'key': 'value'}),  # dict
        ("[1, 2, 3]", [1, 2, 3]),  # list
        ("'string'", 'string'),  # string
        ("malformed_value", "malformed_value"),  # ValueError case
        ("{'key': 'value'", "{'key': 'value'"),  # SyntaxError case
    ])
    def test_parse_value(self, input_value, expected_output):
        result = InventoryModule._parse_value(input_value)
        assert result == expected_output

    def test_parse_value_cleanup(self, monkeypatch):
        # Ensure no state pollution
        monkeypatch.undo()
