# file lib/ansible/plugins/inventory/ini.py:336-352
# lines [336, 337, 342, 343, 346, 348, 349, 351, 352]
# branches []

import pytest
from ansible.plugins.inventory.ini import InventoryModule
from ansible.module_utils._text import to_text

def test_parse_value():
    # Test cases to cover different branches of _parse_value method
    test_cases = [
        ("123", 123),  # int
        ("{'key': 'value'}", {'key': 'value'}),  # dict
        ("[1, 2, 3]", [1, 2, 3]),  # list
        ("'string'", 'string'),  # string
        ("malformed{", "malformed{"),  # ValueError
        ("malformed=", "malformed="),  # SyntaxError
    ]

    for input_value, expected_output in test_cases:
        result = InventoryModule._parse_value(input_value)
        assert result == to_text(expected_output, nonstring='passthru', errors='surrogate_or_strict')

