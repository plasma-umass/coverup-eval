# file: lib/ansible/plugins/inventory/ini.py:336-352
# asked: {"lines": [336, 337, 342, 343, 346, 348, 349, 351, 352], "branches": []}
# gained: {"lines": [336, 337, 342, 343, 346, 348, 349, 351, 352], "branches": []}

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
        ("True", True),  # boolean
        ("None", None),  # NoneType
        ("malformed_string", "malformed_string"),  # ValueError case
        ("{'key': 'value'", "{'key': 'value'"),  # SyntaxError case
    ])
    def test_parse_value(self, input_value, expected_output):
        result = InventoryModule._parse_value(input_value)
        assert result == to_text(expected_output, nonstring='passthru', errors='surrogate_or_strict')
